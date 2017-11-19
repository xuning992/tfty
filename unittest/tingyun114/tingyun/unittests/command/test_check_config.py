#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os
import commands
import unittest
from tingyun.logistics.mapper import ENV_CONFIG_FILE


class CheckConfigTestCase(unittest.TestCase):
    """
    """
    def setUp(self):
        """
        :return:
        """
        self.log_file = os.path.join("/tmp/", "check-config-log-file.log")
        self.config_file = os.path.join("/tmp/", "check-config-config-file.ini")
        self.config_line = {"license_key": "999-999-999", "enabled": True, "app_name": "hello",
                            "log_file": self.log_file, "audit_mode": True, "log_level": "debug", "ssl": True,
                            "auto_action_naming": True, "action_tracer.log_sql": True}
        self.clear_env()
        unittest.TestCase.setUp(self)

    def tearDown(self):
        """
        :return:
        """
        self.clear_env()
        unittest.TestCase.tearDown(self)

    def clear_env(self):
        """
        :return:
        """
        if ENV_CONFIG_FILE in os.environ:
            del os.environ[ENV_CONFIG_FILE]

        if os.path.isfile(self.log_file):
            os.remove(self.log_file)

        if os.path.isfile(self.config_file):
            os.remove(self.config_file)

    def touch_log_file(self):
        """
        :return:
        """
        try:
            with open(self.log_file, "a") as fd:
                pass
        except Exception as _:
            pass

    def generate_config_file(self, modify, change_section=False):
        """
        :return:
        """
        if os.path.isfile(self.config_file):
            os.remove(self.config_file)

        try:
            with open(self.config_file, "w") as fd:
                fd.write("[tingyun]\n" if not change_section else "[test]")
                for key in self.config_line:
                    if key not in modify:
                        fd.write("%s = %s\n" % (key, self.config_line[key]))
                    else:
                        fd.write("%s = %s\n" % (key, modify[key]))
        except Exception as err:
            print err
            return False

        return True

    def test_check_config(self):
        """
        :return:
        """
        # TODO: log file write permission dose not tested
        status, ret = commands.getstatusoutput("tingyun-admin check-config")
        self.assertEqual(status, 0, "return command code error.")
        self.assertTrue("Command Usage" in ret, "return message error.")

        self.generate_config_file({})
        os.environ["TING_YUN_CONFIG_FILE"] = self.config_file
        status, ret = commands.getstatusoutput("tingyun-admin check-config")
        self.assertEqual(status, 0, "return command code error.")

        msg = "Validate agent config file success!!"
        self.assertTrue(msg in ret, "return message error.")

        self.generate_config_file({"license_key": ""})
        os.environ["TING_YUN_CONFIG_FILE"] = self.config_file
        status, ret = commands.getstatusoutput("tingyun-admin check-config")
        self.assertEqual(status, 0, "return command code error.")

        msg = "config option <license_key> is not defined, agent will not work well."
        self.assertTrue(msg in ret, "return message error.")

        self.generate_config_file({"log_file": ""})
        self.touch_log_file()
        os.environ["TING_YUN_CONFIG_FILE"] = self.config_file
        status, ret = commands.getstatusoutput("tingyun-admin check-config")
        self.assertEqual(status, 0, "return command code error.")
        msg = "config option <log_file> is not defined, agent log will output to stderr"
        self.assertTrue(msg in ret, "return message error.")

        self.generate_config_file({"audit_mode": "TrU"})
        os.environ["TING_YUN_CONFIG_FILE"] = self.config_file
        status, ret = commands.getstatusoutput("tingyun-admin check-config")
        msg = "audit_mode=TrU, TrU is not supported. Use default value [False] instead"
        self.assertTrue(msg in ret, "return message error.")
        self.assertEqual(status, 0, "return command code error.")

        self.generate_config_file({"log_level": "dfsf"})
        os.environ["TING_YUN_CONFIG_FILE"] = self.config_file
        status, ret = commands.getstatusoutput("tingyun-admin check-config")
        msg = "log_level=dfsf, dfsf is not supported. Use default value [logging.DEBUG] instead"
        self.assertTrue(msg in ret, "return message error.")
        self.assertEqual(status, 0, "return command code error.")

        self.generate_config_file({"action_tracer.log_sql": ""})
        os.environ["TING_YUN_CONFIG_FILE"] = self.config_file
        status, ret = commands.getstatusoutput("tingyun-admin check-config")
        msg = "action_tracer.log_sql=,  is not supported. Use default value [False] instead"
        self.assertTrue(msg in ret, "return message error.")
        self.assertEqual(status, 0, "return command code error.")

        self.generate_config_file({"action_tracer.log_sql": "ff"})
        os.environ["TING_YUN_CONFIG_FILE"] = self.config_file
        status, ret = commands.getstatusoutput("tingyun-admin check-config")
        msg = "action_tracer.log_sql=ff, ff is not supported. Use default value [False] instead"
        self.assertTrue(msg in ret, "return message error.")
        self.assertEqual(status, 0, "return command code error.")

        self.generate_config_file({"log_level": "ff"})
        os.environ["TING_YUN_CONFIG_FILE"] = self.config_file
        status, ret = commands.getstatusoutput("tingyun-admin check-config")
        msg = "log_level=ff, ff is not supported. Use default value [logging.DEBUG] instead"
        self.assertTrue(msg in ret, "return message error.")
        self.assertEqual(status, 0, "return command code error.")

        self.generate_config_file({}, True)
        os.environ["TING_YUN_CONFIG_FILE"] = self.config_file
        status, ret = commands.getstatusoutput("tingyun-admin check-config")

        msg = "Section [tingyun] is not specified"
        self.assertTrue(msg in ret, "return message error.")
        self.assertEqual(status, 0, "return command code error.")


if __name__ == "__main__":
    unittest.main()
