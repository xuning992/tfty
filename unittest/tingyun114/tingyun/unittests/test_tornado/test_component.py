#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""used to test the tornado component data

"""

import unittest
import redis


class TestComponentCase(unittest.TestCase):
    """
    """
    def setUp(self):
        unittest.TestCase.setUp(self)

        rd = redis.Redis(host="192.168.2.43")

    def tearDown(self):
        unittest.TestCase.tearDown(self)
