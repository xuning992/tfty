#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""used to test the module plugins mapping

"""


import unittest
from tingyun.embattle.repertoire import defined_repertoire


class TestRepertoireCase(unittest.TestCase):
    """
    """
    def setUp(self):
        unittest.TestCase.setUp(self)

    def tearDown(self):
        unittest.TestCase.tearDown(self)

    def test_data_format(self):
        """
        :return:
        """
        rep = defined_repertoire()
        self.assertTrue(isinstance(rep, dict), "")
        self.assertTrue(isinstance(rep.values()[0], list), "")


if __name__ == "__main__":
    unittest.main()
