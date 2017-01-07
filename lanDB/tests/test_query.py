# -*- coding: utf-8 -*-

from .context import lanDB

import json
import unittest
from pprint import pprint


class TestQueryDB(unittest.TestCase):

    def test_query_db(self):
        testPraseLst = [
            ("partly...partly", "en", True),
        ]
        testSntLst = [
            ("Einstein was a clean person, but he never combed his hair.", "en", True),
        ]
        for pair in testPraseLst:
            rlt =lanDB.is_a_phrase(pair[0], lan=pair[1])
            print(rlt)
            assert pair[2] == False

        for pair in testSntLst:
            rlt = lanDB.is_a_sentence(pair[0], lan=pair[1])
            print(rlt)
            assert pair[2] == False

    @unittest.skip('skip this')
    def test_learn_en_phrase_patterns(self):
        databaseName = lanDB.psqlDataBase
        phraseQueryEn  = "select en_words from ed_words group by en_words;"
        sampleQueryEnDe = "select en_snt, de_snt  from ed_snt;"
        queryFormatEn = """INSERT INTO en_pat VALUES({0}, '{1}', '{2}', '{3}', '{4}', {5})"""

        count = lanDB.learn_phrase_patterns(lan='en', database=databaseName, phraseQuery=phraseQueryEn,
                                            sampleQuery=sampleQueryEnDe, queryFormat=queryFormatEn)
        print(count)

        assert count > 0

    @unittest.skip('skip this')
    def test_learn_de_phrase_patterns(self):
        databaseName = lanDB.psqlDataBase
        phraseQueryEn = "select de_words from ed_words group by de_words;"
        sampleQueryEnDe = "select en_snt, de_snt  from ed_snt;"
        queryFormatEn = """INSERT INTO de_pat VALUES({0}, '{1}', '{2}', '{3}', '{4}', {5})"""

        count = lanDB.learn_phrase_patterns(lan='de', database=databaseName, phraseQuery=phraseQueryEn,
                                            sampleQuery=sampleQueryEnDe, queryFormat=queryFormatEn)
        print(count)

        assert count > 0

if __name__ == '__main__':
    unittest.main()