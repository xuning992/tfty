#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os
import commands
import unittest

os.environ['TING_YUN_STARTUP_DEBUG'] = 'fd'

from tingyun.config.start_log import log_message
from tingyun.commander import launch_commanding_elevation


def define_for_deco_test():
    """
    :return:
    """
    pass


class AdminTestCase(unittest.TestCase):
    """
    """
    def setUp(self):
        """
        :return:
        """
        unittest.TestCase.setUp(self)

    def tearDown(self):
        """
        :return:
        """
        unittest.TestCase.tearDown(self)

    def test_load_internal_plugins(self):
        """test the load specified plugins is success or not
        :return:
        """
        launch_commanding_elevation()

        self.assertTrue(sys.modules.get('tingyun.commander.commands.run_program', False),
                        "load internal plugin normal test failed.")
        self.assertTrue(sys.modules.get('tingyun.commander.commands.generate_config', False),
                        "load internal plugin normal test failed.")
        self.assertTrue(sys.modules.get('tingyun.commander.commands.check_config', False),
                        "load internal plugin normal test failed.")
        self.assertFalse(sys.modules.get('tinyun.admin.ruogram', False), "load internal plugin error test failed.")

    def test_decorator_command(self):
        """test the decorator
        :return:
        """
        pass
        # deco = command("test")
        # self.assertTrue(callable(deco), "test decorator callable return failed.")
        #
        # deco_callback = deco(define_for_deco_test)
        # self.assertEqual("test", deco_callback.name, "decorator failed for property name")
        # self.assertEqual(deco_callback, define_for_deco_test)

    def test_main(self):
        """
        :return:
        """

        self.assertTrue(sys.modules.get('tingyun.commander.commands.run_program', False),
                        "load internal plugin normal test failed.")
        status, _ = commands.getstatusoutput("tingyun-admin help")
        self.assertEqual(status, 0, "default help output status error.")

        status, content = commands.getstatusoutput("tingyun-admin hello")
        self.assertTrue('Support commands are' in content, "unknown output error.")
        self.assertEqual(status, 0, "return value error.")

        shell_file = os.path.join(os.path.dirname(__file__), "excute.sh")
        shell_test_file = os.path.join(os.path.dirname(__file__), "shell_test.file")
        
        # clear the env
        if os.path.isfile(shell_file):
            os.remove(shell_file)
            
        if os.path.isfile(shell_test_file):
            os.remove(shell_test_file)
        
        fd = open(shell_file, "w")
        fd.writelines("#!/bin/sh\n")
        fd.writelines("touch %s" % shell_test_file)
        fd.close()
        
        status, _ = commands.getstatusoutput("tingyun-admin run-program sh %s" % shell_file)
        self.assertEqual(status, 0, "full success command execute error.")
        
        # clear the env
        if os.path.isfile(shell_file):
            os.remove(shell_file)
            
        if os.path.isfile(shell_test_file):
            os.remove(shell_test_file)

    def test_start_log(self):
        """
        :return:
        """
        
        output = log_message("this is test: %s", os.environ.get('TING_YUN_STARTUP_DEBUG'))
        self.assertFalse(output, "output is not empty.")

    def test_run_program(self):
        """
        """
        shell_file = os.path.join(os.path.dirname(__file__), "excute.sh")
        shell_test_file = os.path.join(os.path.dirname(__file__), "shell_test.file")
    
        # clear the env
        if os.path.isfile(shell_file):
            os.remove(shell_file)
            
        if os.path.isfile(shell_test_file):
            os.remove(shell_test_file)
        
        fd = open(shell_file, "w")
        fd.writelines("#!/bin/sh\n")
        fd.writelines("touch %s" % shell_test_file)
        fd.close()
        
        status, _ = commands.getstatusoutput("tingyun-admin run-program sh %s" % shell_file)
        commands.getstatusoutput("tingyun-admin run-program sh %s" % shell_file)
        self.assertEqual(status, 0, "")
        self.assertTrue(os.path.isfile(shell_test_file), "program shouldn't excuted.")
         
        #TODO: add other case test
         
        # clear the env
        if os.path.isfile(shell_file):
            os.remove(shell_file)
            
        if os.path.isfile(shell_test_file):
            os.remove(shell_test_file)


if __name__ == "__main__":
    unittest.main()