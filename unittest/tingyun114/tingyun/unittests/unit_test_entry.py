#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""used to load all the test in the unit test

"""

import unittest


def execute_test():
    test_suit = unittest.TestLoader().discover("./", "*.py")
    unittest.TextTestRunner().run(test_suit)

if __name__ == "__main__":
    execute_test()