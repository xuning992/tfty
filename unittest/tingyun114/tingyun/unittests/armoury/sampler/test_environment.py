#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""used to test the environment module of the agent

"""


import unittest
from tingyun.armoury.sampler.environment import env_config


class TestEnvironmentCase(unittest.TestCase):
    """
    """
    def setUp(self):
        unittest.TestCase.setUp(self)
        
    def tearDown(self):
        unittest.TestCase.tearDown(self)
        
    def test_env_config(self):
        """
        """
        env = env_config()
        
        self.assertTrue("OS Arch" in env, "")
        self.assertTrue("CPU Cores" in env, "")
        self.assertTrue("OS Version" in env, "")
        
        self.assertTrue("Python Version" in env, "")
        self.assertTrue("Python Platform" in env, "")
        self.assertTrue("Physical Memory" in env, "")
        self.assertTrue("CPU Vendor" in env, "")
        self.assertTrue("kernel" in env, "")


if __name__ == "__main__":
    unittest.main()
