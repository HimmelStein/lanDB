"""
postgres database: langauge_graph
tables: chbible, debible, enbible, ldc200201_back, ldc2002t01, pons, pons_back
"""

"""
connect to postgres database
rows = db.query("SELECT tablename from pg_tables where schemaname='public'")
"""

psqlDataBase = 'postgres://localhost/language_graph'

"""
connect to sqlite database
rows = db.query("select * from sqlite_master where type ='table'")
"""

sqliteDataBase = 'sqlite:///data/PONS.db'


table_kdic = [
    {"lan": "de",  "table": "pons",  "snt": "de_snt",  "ldg": "de_ldg"},
    {"lan": "ch", "table": "pons", "snt": "ch_snt", "ldg": "ch_ldg"},
    {"lan": "ch", "table": "ldc2002t01", "snt": "ch_snt", "ldg": "ch_ldg"},
    {"lan": "en",  "table": "ldc2002t01", "snt": "en_snt",  "ldg": "en_ldg"},
    {"lan": "de", "table": "debible", "snt": "snt", "ldg": "snt_lg"},
    {"lan": "ch", "table": "chbible", "snt": "snt", "ldg": "snt_lg"},
    {"lan": "en", "table": "enbible", "snt": "snt", "ldg": "snt_lg"},
    ]

psqlTables = {
    "bigraph_map" : {
        'cols': ['id', 'cgraph1', 'ccg1', 'cgraph2', 'ccg2', 'map_cgraph', 'map_subg']
    },
    "ch_pat": {
        'cols': ['id', 'words', 'pat', 'pat1', 'snt', 'count']
    },
    "chbible": {
        'cols': ['id', 'bbid', 'snt', 'snt_lg', 'snt_sdg']
    },
    "chde_snt": {
        'cols': ['id', 'ch_snt', 'de_snt', 'ch_ldg', 'ch_sdg', 'de_ldg', 'de_sdg']
    },
    "de_pat": {
        'cols': ['id', 'words', 'pat', 'pat1', 'snt', 'count']
    },
    "debible": {
        'cols': ['id', 'bbid', 'snt', 'snt_lg', 'snt_sdg']
    },
    "dech_snt": {
        'cols': ['id', 'ch_snt', 'de_snt', 'ch_ldg', 'ch_sdg', 'de_ldg', 'de_sdg']
    },
    "deen_snt": {
        'cols': ['id', 'en_snt', 'en_ldg', 'de_snt', 'de_ldg']
    },
    "ed_snt": {
        'cols': ['id', 'en_snt', 'en_ldg', 'de_snt', 'de_ldg']
    },
    "ed_words": {
        'cols': ['id', 'en_words', 'en_ldg', 'de_words', 'de_ldg']
    },
    "en_pat": {
        'cols': ['id', 'words', 'pat', 'pat1', 'snt', 'count']
    },
    "en_pat0": {
        'cols': ['id', 'words', 'pat', 'snt', 'count']
    },
    "ende_dicleo": {
        'cols': ['id', 'word', 'en', 'de']
    },
    "ende_snt": {
        'cols': ['id', 'en_snt', 'en_ldg', 'de_snt', 'de_ldg']
    },
    "ende_words": {
        'cols': ['id', 'en_words', 'en_ldg', 'de_words', 'de_ldg']
    },
    "ldc2002t01": {
        'cols': ['id', 'fname', 'en_sub', 'ch_snt', 'en_snt', 'seg_id', 'ch_ldg', 'ch_sdg', 'en_ldg', 'en_sdg ']
    },
    "pons": {
        'cols': ['id', 'ch_snt', 'de_snt', 'ch_ldg', 'ch_sdg', 'de_ldg', 'de_sdg']
    },
    "pons_back": {
        'cols': ['id', 'ch_snt', 'de_snt', 'ch_ldg', 'ch_sdg', 'de_ldg', 'de_sdg']
    }
}