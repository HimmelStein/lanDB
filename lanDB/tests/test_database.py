# -*- coding: utf-8 -*-

from .context import lanDB

import json
import unittest
from pprint import pprint


class TestDataBase(unittest.TestCase):

    @unittest.skip('')
    def test_get_all_en_de_conjunctions(self):
        rlt = graph2.get_all_en_de_conjunctions()
        pprint(rlt)
        assert len(rlt) > 10

    @unittest.skip('')
    def test_get_conjunction_sample(self):
        rlt = lanDB.get_conjunction_sample('en')
        pprint(rlt[:10])
        assert len(rlt) > 0

        rlt = lanDB.get_conjunction_sample('de')
        pprint(rlt[:10])
        assert len(rlt) > 0

    def test_all_POS(self):
        assert True

    def test_all_relations(self):
        assert True

if __name__ == '__main__':
    unittest.main()