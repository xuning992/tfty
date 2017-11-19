#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""used to test the attribution module of the agent

"""

import unittest
import time
from collections import namedtuple
from tingyun.logistics.attribution import node_start_time, node_end_time, node_duration_time

Node = namedtuple("RootNode", ["start_time", "end_time"])


class TestStatsCase(unittest.TestCase):
    """
    """
    def setUp(self):
        unittest.TestCase.setUp(self)

    def tearDown(self):
        unittest.TestCase.tearDown(self)

    def test_node_time(self):
        """
        :return:
        """
        base_time = time.time()
        root = Node(start_time=base_time, end_time=base_time + 20)
        child_1 = Node(start_time=base_time + 10, end_time=base_time + 15)
        child_2 = Node(start_time=base_time + 12, end_time=base_time + 14)

        # test the relative start time
        ret_1 = node_start_time(root, child_1)
        ret_2 = node_start_time(root, child_2)
        self.assertEqual(ret_1, 10000, "first child start time error.")
        self.assertEqual(ret_2, 12000, "first child start time error.")

        # test the relative end time
        ret_1 = node_end_time(root, child_1)
        ret_2 = node_end_time(root, child_2)
        self.assertEqual(ret_1, 15000, "first child start time error.")
        self.assertEqual(ret_2, 14000, "first child start time error.")

        # test the duration time
        ret_0 = node_duration_time(root)
        ret_2 = node_duration_time(child_2)
        self.assertEqual(ret_0, 20000, "first child start time error.")
        self.assertEqual(ret_2, 2000, "first child start time error.")


if __name__ == "__main__":
    unittest.main()
