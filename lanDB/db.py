import records
import codecs
import os
from .db_config import psqlDataBase, sqliteDataBase, table_kdic


def get_max_id_in_table(psqlDataBase, tableName):
    """
    :param psqlDataBase:
    :param tableName:
    :return:
    """
    db = records.Database(psqlDataBase)
    sqlStr = "SELECT id from " + tableName
    return max([rec['id'] for rec in db.query(sqlStr)])


def query_db(database, queryStr):
    """
    :param database:
    :param queryStr:
    :return: a list of records, each record is a list
    """
    db = records.Database(database)
    rlt = [list(map(lambda ele: ele.strip(), rd.as_dict().values())) for rd in db.query(queryStr)]
    return rlt


def sample_snt_to_ldg_in_table(id, db = psqlDataBase, table='pons', lan='ch'):
    """
    id range from the table
    :param id:
    :param table:
    :param lan:
    :return: a graph in cnll10 format
    """
    tableInfo = find_table(table=table, lan=lan)
    if tableInfo:
        db = records.Database(db)
        ldgColumn = tableInfo['ldg']
        sqlStr = "SELECT " + ldgColumn + " from " + table
        rows = db.query(sqlStr)
        try:
            return rows[id].get(ldgColumn)
        except:
            return ""
    return ""


def find_table(table='pons', lan='ch', dicLst = table_kdic):
    for dic in dicLst:
        if dic['lan'] == lan and dic['table'] == table:
            return dic
    return False


def get_raw_ldg_with_id_from_pons(id, table='PONS', lan='ch'):
    assert table == 'PONS'
    # global table_kdic, psqlDataBase, sqliteDataBase
    db = records.Database(psqlDataBase, user="Postgre")
    if table == 'PONS' and lan == 'ch':
        sql_str = "SELECT ch_snt, ch_ldg FROM "+ table + " where id="+str(id)
    elif table == 'PONS' and lan == 'de':
        sql_str = "SELECT de_snt, de_ldg FROM "+ table + " where id="+str(id)

    rows = db.query(sql_str)
    for row in rows:
        print(row[1].replace('*', '\n'))
        return row[1]
    return None


def check_database(dbname=sqliteDataBase):
    """
    check whether database exist, or contains tables
    :param dbname:
    :return: -1, if either database not exist, or does not have tables,
             n, number of tables it has
    """
    db = records.Database(dbname)
    tables = db.get_table_names()
    if len(tables) == 0:
        return -1
    else:
        return len(tables)


def list_tables(dbname=sqliteDataBase):
    """
    print all tables in the  database
    :param dbname: database name
    :return: a list of tables in the data base
             [], if it has not tables
    """
    db = records.Database(dbname)
    return db.get_table_names()





"""
def copy_sqlite_table_into_postgres():
    #
    # To do
    # load snt table into postgres
    # :return:
    #
    try:
        con = psycopg2.connect(host='localhost', database="language_graph", user="postgres")

        print('connecting postgre')
        cur = con.cursor()
        import sqlite3
        conn_sqlite = sqlite3.connect(os.path.join("..", 'PONS.db'))
        c_sqlite = conn_sqlite.cursor()
        for row in c_sqlite.execute("SELECT * FROM snt"):
            print(row)
            id = row[0]
            ch_snt = row[2]
            de_snt = row[1]
            sql_str = "INSERT INTO pons (id, ch_snt, de_snt) VALUES({0}, '{1}', '{2}')".format(id,  ch_snt, de_snt)
            print(sql_str)
            cur.execute(sql_str)
        con.commit()
    except psycopg2.DatabaseError:
        if con:
            con.rollback()
        print('Error %s' % psycopg2.DatabaseError)
        sys.exit(1)
    finally:
        if con:
            con.close()

"""




def key_word_search(snt, lan=''):
    """
    search database by key-words.
    :param snt:
    :param lan:
    :return:
    """
    pass
