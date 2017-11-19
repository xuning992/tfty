#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""used to test the module plugins detect

"""

import unittest
from tingyun.embattle.inspection import take_control


class TestInspectionCase(unittest.TestCase):
    """
    """
    def setUp(self):
        unittest.TestCase.setUp(self)

    def tearDown(self):
        unittest.TestCase.tearDown(self)

    def test_none_config_file(self):
        """
        :return:
        """
        controller_tmp = take_control(None)
        controller = take_control(None)

        self.assertEqual(id(controller), id(controller_tmp), "")
        self.assertFalse(controller.execute(), "")


if __name__ == "__main__":
    unittest.main()
