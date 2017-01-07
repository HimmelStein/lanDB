import records
import psycopg2

psqlDataBase = 'postgres://localhost/language_graph'

"""
mapped phrase: select en_words, de_words from ed_words;

english phrase: select words, pat, pat1, snt, count from en_pat;

german phrase: select words, pat, pat1, snt, count from de_pat;

bi_cgraph_table structure: [cgraph1, ccg_ex1, cgraph2, ccg_ex2, map_cgraph, map_subg] TO DO
"""


def get_query_result(db=psqlDataBase, query=''):
    """
    note records lib has a bug, so use psycopg2 lib
    :param db:
    :param query:
    :return:
    """
    if db == psqlDataBase:
        conn_string = "host='localhost' dbname='language_graph' user='postgres'"
        conn = psycopg2.connect(conn_string)
        cursor = conn.cursor()
        cursor.execute(query)
        return cursor.fetchall()
    print('database not recognized\n')
    return []


def insert_to_bigraph_map(cgraph1, ccg_ex1, cgraph2, ccg_ex2, mapNodesOfCgraphs, mapRootOfSubgraphs,l1='en', l2='de'):
    """

    :param cgraph1:
    :param ccg_ex1:
    :param cgraph2:
    :param ccg_ex2:
    :param mapNodesOfCgraphs:
    :param mapRootOfSubgraphs:
    :return:
    """
    db = records.Database(psqlDataBase)

    tx = db.transaction()
    try:
        if l1=='en' and l2=='de':
            table = "bigraph_map"
        else:
            print('not en-->de\n')
            table = "bigraph_map" # TO DO
        sql_str = """INSERT INTO {0} (cgraph1, ccg1, cgraph2, ccg2, map_cgraph, map_subg) VALUES({1}, '{2}', '{3}', '{4}', '{5}', '{6}')"""\
            .format(table, cgraph1, ccg_ex1, cgraph2, ccg_ex2, mapNodesOfCgraphs, mapRootOfSubgraphs)
        print(sql_str)
        db.query(sql_str)
        tx.commit()
    except:
        tx.rollback()
    return True


def get_all_en_de_conjunctions():
    rlt=[]
    db = records.Database(psqlDataBase)
    sql_str = "select en_words, de_words from ed_words"
    for rec in db.query(sql_str):
        rlt.append((rec['en_words'], rec['de_words']))
    return rlt


def get_conjunction_sample(lan):
    """
    :param lan: en|de|ch
    :return: a list of ['words', 'pat', 'pat1', 'snt']
    """
    table =  ""
    if lan == 'en':
        table = "en_pat"
    elif lan == 'de':
        table = 'de_pat'
    assert table != ""
    rlt = []
    db = records.Database(psqlDataBase)
    sql_str = "select words, pat, pat1, snt, count from {}".format(table)
    for rec in db.query(sql_str):
        rlt.append((rec['words'], rec['pat'], rec['pat1'], rec['snt']))
    return rlt


def load_pair_to_db(qStrFormat, word, listOflist):
    db = records.Database(psqlDataBase)
    startid = 0
    for pair in listOflist:
        parLst = [word]
        for ele in pair:
            parLst.append(ele.replace("'","''"))
        tx = db.transaction()
        try:
            sql_str = qStrFormat.format(*parLst)
            print(sql_str)
            db.query(sql_str)
            startid += 1
            tx.commit()
        except:
            startid = 0
            tx.rollback()
    return startid


def get_all_POS(lan='de'):
    """

    :param lan:
    :return:
    """
    return []


def get_all_relations(lan='de'):
    """

    :param lan:
    :return:
    """
    return []
