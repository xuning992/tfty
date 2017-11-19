#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""used to test the packets module of the agent

"""


import unittest
from collections import namedtuple
from tingyun.logistics.workshop.packets import TimePackets, ApdexPackets, SlowSqlPackets

TimePacketsNode = namedtuple("TimePacketsNode", ["duration", "exclusive"])
ApdexPacketsNode = namedtuple("ApdexPacketsNode", ["satisfying", "tolerating", "frustrating"])
SqlPacketsNode = namedtuple("SqlPacketsNode", ["duration", ])


class TestPacketsCase(unittest.TestCase):
    """
    """
    def setUp(self):
        unittest.TestCase.setUp(self)

    def tearDown(self):
        unittest.TestCase.tearDown(self)

    def test_time_packets(self):
        """
        :return:
        """
        time_node = TimePacketsNode(3, 2)
        packets = TimePackets()
        packets.merge_time_metric(time_node)
        self.assertEqual(packets[0], 1, "call times count error.")
        self.assertEqual(packets[1], 3, "total cost times count error.")
        self.assertEqual(packets[2], 2, "total exclusive times count error.")
        self.assertEqual(packets[3], 3, "max cost time count error.")
        self.assertEqual(packets[4], 3, "min cost time count error.")
        self.assertEqual(packets[5], 9, "time square count error.")

        time_node = TimePacketsNode(5, 3)
        packets.merge_time_metric(time_node)
        self.assertEqual(packets[0], 2, "call times count error.")
        self.assertEqual(packets[1], 8, "total cost times count error.")
        self.assertEqual(packets[2], 5, "total exclusive times count error.")
        self.assertEqual(packets[3], 5, "max cost time count error.")
        self.assertEqual(packets[4], 3, "min cost time count error.")
        self.assertEqual(packets[5], 34, "time square count error.")

        packets_other = TimePackets()
        time_node = TimePacketsNode(4, 3)
        packets_other.merge_time_metric(time_node)
        self.assertEqual(packets_other[0], 1, "call times count error.")
        self.assertEqual(packets_other[1], 4, "total cost times count error.")
        self.assertEqual(packets_other[2], 3, "total exclusive times count error.")
        self.assertEqual(packets_other[3], 4, "max cost time count error.")
        self.assertEqual(packets_other[4], 4, "min cost time count error.")
        self.assertEqual(packets_other[5], 16, "time square count error.")

        time_node = TimePacketsNode(8, 2)
        packets_other.merge_time_metric(time_node)
        self.assertEqual(packets_other[0], 2, "call times count error.")
        self.assertEqual(packets_other[1], 12, "total cost times count error.")
        self.assertEqual(packets_other[2], 5, "total exclusive times count error.")
        self.assertEqual(packets_other[3], 8, "max cost time count error.")
        self.assertEqual(packets_other[4], 4, "min cost time count error.")
        self.assertEqual(packets_other[5], 80, "time square count error.")

        packets.merge_packets(packets_other)
        self.assertEqual(packets[0], 4, "call times count error.")
        self.assertEqual(packets[1], 20, "total cost times count error.")
        self.assertEqual(packets[2], 10, "total exclusive times count error.")
        self.assertEqual(packets[3], 8, "max cost time count error.")
        self.assertEqual(packets[4], 3, "min cost time count error.")
        self.assertEqual(packets[5], 114, "time square count error.")

    def test_apdex_packets(self):
        """
        :return:
        """
        apdex_node = ApdexPacketsNode(1, 0, 0)
        packets = ApdexPackets()
        packets.merge_apdex_metric(apdex_node)
        self.assertEqual(packets[0], 1, "satisfied count error.")
        self.assertEqual(packets[1], 0, "tolerating count error.")
        self.assertEqual(packets[2], 0, "frustrating count error.")

        apdex_node = ApdexPacketsNode(0, 1, 0)
        packets.merge_apdex_metric(apdex_node)
        self.assertEqual(packets[0], 1, "satisfied count error.")
        self.assertEqual(packets[1], 1, "tolerating count error.")
        self.assertEqual(packets[2], 0, "frustrating count error.")

        packets_other = ApdexPackets()
        apdex_node = ApdexPacketsNode(0, 0, 1)
        packets_other.merge_apdex_metric(apdex_node)
        self.assertEqual(packets_other[0], 0, "satisfied count error.")
        self.assertEqual(packets_other[1], 0, "tolerating count error.")
        self.assertEqual(packets_other[2], 1, "frustrating count error.")

        apdex_node = ApdexPacketsNode(1, 0, 0)
        packets_other.merge_apdex_metric(apdex_node)
        self.assertEqual(packets_other[0], 1, "satisfied count error.")
        self.assertEqual(packets_other[1], 0, "tolerating count error.")
        self.assertEqual(packets_other[2], 1, "frustrating count error.")

        packets.merge_packets(packets_other)
        self.assertEqual(packets[0], 2, "satisfied count error.")
        self.assertEqual(packets[1], 1, "tolerating count error.")
        self.assertEqual(packets[2], 1, "frustrating count error.")

    def test_sql_packets(self):
        """
        :return:
        """
        packets = SlowSqlPackets()
        sql_node = SqlPacketsNode(6)
        packets.merge_slow_sql_node(sql_node)

        self.assertEqual(packets[0], 1, "call times count error.")
        self.assertEqual(packets[1], 6, "total cost times count error.")
        self.assertEqual(packets[2], 6, "min cost time count error.")
        self.assertEqual(packets[3], 6, "max cost time count error.")

        sql_node = SqlPacketsNode(7)
        packets.merge_slow_sql_node(sql_node)

        self.assertEqual(packets[0], 2, "call times count error.")
        self.assertEqual(packets[1], 13, "total cost times count error.")
        self.assertEqual(packets[2], 6, "min cost time count error.")
        self.assertEqual(packets[3], 7, "max cost time count error.")

        packets_other = SlowSqlPackets()
        sql_node = SqlPacketsNode(11)
        packets_other.merge_slow_sql_node(sql_node)

        self.assertEqual(packets_other[0], 1, "call times count error.")
        self.assertEqual(packets_other[1], 11, "total cost times count error.")
        self.assertEqual(packets_other[2], 11, "min cost time count error.")
        self.assertEqual(packets_other[3], 11, "max cost time count error.")

        packets.merge_packets(packets_other)
        self.assertEqual(packets[0], 3, "call times count error.")
        self.assertEqual(packets[1], 24, "total cost times count error.")
        self.assertEqual(packets[2], 6, "min cost time count error.")
        self.assertEqual(packets[3], 11, "max cost time count error.")


if __name__ == "__main__":
    unittest.main()
