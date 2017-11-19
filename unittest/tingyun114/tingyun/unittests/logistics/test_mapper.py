#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""used to test the mapper module of the agent

"""

import logging
import unittest

from tingyun.logistics import mapper


class TestMapperCase(unittest.TestCase):
    """
    """

    def setUp(self):
        unittest.TestCase.setUp(self)

    def tearDown(self):
        unittest.TestCase.tearDown(self)

    def test_map_log_level(self):
        """
        :return:
        """
        self.assertEqual(mapper.map_log_level('NOTSET'), logging.NOTSET, "info map error.")
        self.assertEqual(mapper.map_log_level('deBug'), logging.DEBUG, "info map error.")
        self.assertEqual(mapper.map_log_level('iNfo'), logging.INFO, "info map error.")
        self.assertEqual(mapper.map_log_level('WARNING'), logging.WARNING, "info map error.")
        self.assertEqual(mapper.map_log_level('WARN'), logging.WARN, "info map error.")
        self.assertEqual(mapper.map_log_level('error'), logging.ERROR, "error map error.")
        self.assertEqual(mapper.map_log_level('CRITICAL'), logging.CRITICAL, "info map error.")
        self.assertEqual(mapper.map_log_level('FATAL'), logging.FATAL, "error map error.")

        self.assertEqual(mapper.map_log_level('FATfAL'), None, "error map error.")
        self.assertEqual(mapper.map_log_level(311), None, "error map error.")

    def test_map_app_name(self):
        """
        :return:
        """
        self.assertEqual(mapper.map_app_name("hello world"), "hello world", "map app name error")
        self.assertEqual(mapper.map_app_name(""), None, "map app name error")

    def test_map_key_words(self):
        """
        :return:
        """
        self.assertTrue(mapper.map_key_words(True), "map key words error")
        self.assertFalse(mapper.map_key_words(False), "map key words error")
        self.assertTrue(mapper.map_key_words('True'), "map key words error")
        self.assertFalse(mapper.map_key_words('False'), "map key words error")
        self.assertTrue(mapper.map_key_words('TruE'), "map key words error")
        self.assertFalse(mapper.map_key_words('FaLse'), "map key words error")

        self.assertTrue(mapper.map_key_words('ON'), "map key words error")
        self.assertFalse(mapper.map_key_words('OFF'), "map key words error")
        self.assertTrue(mapper.map_key_words('On'), "map key words error")
        self.assertFalse(mapper.map_key_words('OfF'), "map key words error")

        self.assertEqual(mapper.map_key_words("fd"), None, "map key words error.")
        self.assertEqual(mapper.map_key_words(32), None, "map key words error.")


if __name__ == "__main__":
    unittest.main()
