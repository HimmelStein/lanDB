from .transaction import do_transaction
from .db_config import psqlDataBase
from .pickle_util import get_bible_pickle
from .db import get_max_id_in_table
import records
import os
import codecs


def insert_2snt_into_db_table(db='language_graph', dbuser='postgres', table='ldc2002t01',
                              id = 0, fname='', en_sub='', seg_id=0, ch_snt='', en_snt=''):
    """
        table ldc2002t01: id | fname | en_sub |  seg_id  |ch_snt | en_snt | ch_ldg | ch_sdg | en_ldg | en_sdg
    """
    db = records.Database(psqlDataBase)
    ch_snt = ch_snt.replace("'", "\'")
    en_snt = en_snt.replace("'", "''")
    sql_str = "INSERT INTO " + table + "(id, fname, en_sub,  seg_id, ch_snt, en_snt) VALUES({0}, '{1}', '{2}', {3}, '{4}', '{5}')".format(id, fname, en_sub, seg_id, ch_snt, en_snt)
    print(sql_str)
    db.query(sql_str)


def insert_snt_into_db_table(fname, encode='utf-8', db='language_graph', dbuser='postgres', table=''):
    """
    table ldc2002t01: id | fname | en_sub | ch_snt | en_snt | ch_ldg | ch_sdg | en_ldg | en_sdg
    table chbible: id | bbid | snt | snt_lg | snt_sdg
    table debible: id | bbid | snt | snt_lg | snt_sdg
    table enbible: id | bbid | snt | snt_lg | snt_sdg

    :param fname:
    :param encode:
    :param db:
    :param dbuser:
    :param table:
    :return:
    """
    db = records.Database(psqlDataBase)
    fhandle = codecs.open(os.path.join("..", fname), "r", encode)
    i = 0
    for line in fhandle.readlines():
            line = line.strip('\n').strip('\r')
            bbid = ''
            snt = ''
            lst = line.split(' ')
            if len(lst) < 3:
                bbid = lst[0] + ' ' + lst[1]
            elif ':' in lst[1]:
                bbid = lst[0] + ' ' + lst[1]
                snt = ' '.join(lst[2:])
            else:
                print('**', lst)
            print(bbid, snt)
            db.query("INSERT INTO "+table+"(id, bbid, snt) VALUES(%s, %s, %s)",(i, bbid, snt))
            i += 1


def insert_learned_phrase_patterns_into_db(lan='', id=-1, phrase='', cnllStr='', cnllStr1='', snt='', count=0):
        """

        :param id:
        :param phrase:
        :param cnllStr:
        :param cnllStr1:
        :param snt:
        :param count:
        :return:
        """
        if lan == 'de':
            tableName = 'de_pat'
            queryFormat = """INSERT INTO de_pat VALUES({0}, '{1}', '{2}', '{3}', '{4}', '{5}')"""
        elif lan == 'en':
            tableName = 'en_pat'
            queryFormat = """INSERT INTO en_pat VALUES({0}, '{1}', '{2}', '{3}', '{4}', '{5}')"""
        elif lan == 'ch':
            tableName = 'ch_pat'
            queryFormat = """INSERT INTO ch_pat VALUES({0}, '{1}', '{2}', '{3}', '{4}', '{5}')"""
        if id == -1:
            id = get_max_id_in_table(psqlDataBase, tableName)
        do_transaction(psqlDataBase, queryFormat.format(id, phrase, cnllStr, cnllStr1, snt, count))


#
# load LDG to three tables
#


def load_bible_ldg_into_table_from_pickle(lans=['de','ch','en']):
    """
    table 1: chbible: id | bbid | snt | snt_lg | snt_sdg
    table 2: debible: id | bbid | snt | snt_lg | snt_sdg
    table 3: enbible: id | bbid | snt | snt_lg | snt_sdg
    do in parallel
    :param lan:
    :return:
    """
    batch_lst = [
        {"lan": "ch", "table": "chbible", "snt": "snt", "ldg": "snt_lg"},
        {"lan": "de", "table": "debible", "snt": "snt", "ldg": "snt_lg"},
        {"lan": "en", "table": "enbible", "snt": "snt", "ldg": "snt_lg"}
    ]
    db = records.Database(psqlDataBase)
    print('connecting postgre')

    ch_lan = batch_lst[0]['lan']
    de_lan = batch_lst[1]['lan']
    en_lan = batch_lst[2]['lan']
    ch_table = batch_lst[0]['table']
    de_table = batch_lst[1]['table']
    en_table = batch_lst[2]['table']
    snt = batch_lst[0]['snt']
    ldg_col = batch_lst[0]['ldg']

    ch_rows = db.query("SELECT id," + snt + ", " + ldg_col + " FROM " + ch_table)
    de_rows = db.query("SELECT id," + snt + ", " + ldg_col + " FROM " + de_table)
    en_rows = db.query("SELECT id," + snt + ", " + ldg_col + " FROM " + en_table)

    dePickle = get_bible_pickle(lan='de')
    enPickle = get_bible_pickle(lan='en')
    chPickle = get_bible_pickle(lan='ch')

    count = 0

    if 'de' in lans:
        id = len(de_rows)
        tx = db.transaction()
        try:
            for key, ldg in dePickle.items():
                ldg = ldg.replace('\t', ' ').replace('\n', ' * ').replace("'", "''")
                snt = ' '.join([w[1] for w in [words.strip().split(' ') for words in ldg.split('*')]])
                sql_str = """INSERT INTO {0} VALUES({1}, '{2}', '{3}', '{4}')""".format(de_table, id, key, snt, ldg)
                print(sql_str)
                db.query(sql_str)

                id += 1
                count += 1
            tx.commit()
        except:
            tx.rollback()

    return count

