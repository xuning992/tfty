#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""used to test the system info module of the agent

"""


import unittest
import commands
from tingyun.armoury.sampler.system_info import cpu_count, memory_total


class TestSystemInfoCase(unittest.TestCase):
    """
    """
    def setUp(self):
        unittest.TestCase.setUp(self)
        
    def tearDown(self):
        unittest.TestCase.tearDown(self)
        
    def test_cpu_count(self):
        """
        """
        cpus = commands.getoutput("cat /proc/cpuinfo | grep processor | wc -l")
        self.assertEqual(int(cpus), cpu_count(), "")
        
    def test_memory_total(self):
        """
        """
        except_flag = False
        
        try:
            memory_total()
        except Exception as _:
            except_flag = True
            
        self.assertFalse(except_flag, "")
        
        
if __name__ == "__main__":
    unittest.main()
