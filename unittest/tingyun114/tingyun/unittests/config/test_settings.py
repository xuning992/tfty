#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""used to test the settings of the agent

"""

import unittest

import tingyun.config.settings
import tingyun.config.settings
from tingyun.config.settings import Settings, flatten_settings, get_upload_settings, apply_config_setting, merge_settings


class TestSettingsCase(unittest.TestCase):
    """
    """

    def setUp(self):
        unittest.TestCase.setUp(self)
        self.settings = tingyun.config.settings.global_settings()

    def tearDown(self):
        unittest.TestCase.tearDown(self)

    def test_attribute(self):
        """
        """
        self.assertTrue(hasattr(self.settings, "license_key"), "app name attribute lost")
        self.assertTrue(hasattr(self.settings, "enabled"), "log_level attribute lost")
        self.assertTrue(hasattr(self.settings, "app_name"), "audit_mode attribute lost")

        self.assertTrue(hasattr(self.settings, "log_file"), "app name attribute lost")
        self.assertTrue(hasattr(self.settings, "audit_mode"), "log_level attribute lost")
        self.assertTrue(hasattr(self.settings, "log_level"), "audit_mode attribute lost")

        self.assertTrue(hasattr(self.settings, "ssl"), "app name attribute lost")
        self.assertTrue(hasattr(self.settings, "auto_action_naming"), "log_level attribute lost")
        self.assertTrue(hasattr(self.settings, "action_tracer"), "audit_mode attribute lost")

        self.assertTrue(hasattr(self.settings.action_tracer, "log_sql"), "audit_mode attribute lost")

        self.assertTrue(isinstance(self.settings.error_collector, Settings), "log_level attribute lost")
        self.assertTrue(isinstance(self.settings.action_tracer, Settings), "log_level attribute lost")

    def test_flatten_settings(self):
        """
        """
        flat_setting = flatten_settings(self.settings)

        self.assertTrue("enabled" in flat_setting, "enabled attribute lost")
        self.assertTrue("app_name" in flat_setting, "app_name attribute lost")
        self.assertTrue("host" in flat_setting, "host attribute lost")
        self.assertTrue("ssl" in flat_setting, "ssl attribute lost")

        self.assertTrue("action_tracer.slow_sql" in flat_setting, "action_tracer.slow_sql attribute lost")
        self.assertTrue("action_tracer.stack_trace_threshold" in flat_setting, "action_tracer attribute lost")
        self.assertFalse("log_level_mapping" in flat_setting, "action_tracer attribute lost")

        self.assertTrue(isinstance(flat_setting["action_apdex"], dict), "the action apdex is not list.")
        self.assertTrue(isinstance(flat_setting["urls_captured"], list), "the action apdex is not list.")
        self.assertTrue(isinstance(flat_setting["error_collector.ignored_status_codes"], list),
                        "the action apdex is not list.")

    def test_get_upload_settings(self):
        """
        """
        dump_setting = get_upload_settings()

        self.assertTrue("nbs.app_name" in dump_setting, "app_name attribute lost")
        self.assertTrue("nbs.host" in dump_setting, "host attribute lost")
        self.assertTrue("nbs.license_key" in dump_setting, "ssl attribute lost")
        self.assertTrue("nbs.agent_enabled" in dump_setting, "ssl attribute lost")
        self.assertTrue("nbs.audit_mode" in dump_setting, "audit_mode attribute lost")
        self.assertTrue("nbs.auto_app_naming" in dump_setting, "auto_action_naming attribute lost")
        self.assertTrue("nbs.action_tracer.log_sql" in dump_setting, "log_sql attribute lost")
        self.assertFalse("nbs.log_level_mapping" in dump_setting, "action_tracer attribute lost")

    def test_apply_config_setting(self):
        """test the string config to object.
        """
        apply_config_setting(self.settings, "lover", "fzz")
        self.assertTrue(hasattr(self.settings, "lover"), "change attribute failed.")
        self.assertEqual(self.settings.lover, "fzz", "change attribute failed.")

        apply_config_setting(self.settings, "error_collector.switch", "on")
        self.assertTrue(hasattr(self.settings, "error_collector"), "change attribute failed.")
        self.assertEqual(self.settings.error_collector.switch, "on", "change attribute failed.")

        apply_config_setting(self.settings, "customer_type.switch", "on")
        self.assertTrue(hasattr(self.settings, "customer_type"), "change attribute failed.")
        self.assertEqual(self.settings.customer_type.switch, "on", "change attribute failed.")

        apply_config_setting(self.settings, "error_collector.ignored_status_codes", "304, 404")
        self.assertEqual(self.settings.error_collector.ignored_status_codes, [304, 404], "ignore status code error.")
        apply_config_setting(self.settings, "error_collector.ignored_status_codes", "")
        self.assertTrue(isinstance(self.settings.error_collector.ignored_status_codes, list),
                        "ignore status type error")

        apply_config_setting(self.settings, "urls_captured", "/cargo/detail/6/\\n/cargo/detail/7/")
        self.assertTrue(isinstance(self.settings.urls_captured, list), "capture url error.")
        self.settings.urls_captured = []
        apply_config_setting(self.settings, "urls_captured", "")
        self.assertEqual(self.settings.urls_captured, [], "empty capture url analyze error.")

        apply_config_setting(self.settings, "ignored_params", "time,info")
        self.assertTrue(isinstance(self.settings.urls_captured, list), "ignored_params error.")
        self.assertEqual(self.settings.ignored_params, ["time", "info"], "ignore status code error.")
        self.settings.urls_captured = []
        apply_config_setting(self.settings, "ignored_params", "")
        self.assertEqual(self.settings.urls_captured, [], "ignored_params analyze error.")

    def test_merge_settings(self):
        """
        """
        server_conf = {
            "applicationId": "1233",
            "enabled": True,
            "appSessionKey": "rwreqrq",
            "dataSentInterval": 60,
            "apdex_t": 25,
            "config": {
                "nbs.agent_enabled": True,
                "nbs.auto_action_naming": True,
                "nbs.capture_params": True,
                "nbs.error_collector.enabled": True,
                "nbs.error_collector.record_db_errors": True,
                "nbs.action_tracer.enabled": True,
                "nbs.action_tracer.action_threshold": 0,
                "nbs.action_tracer.record_sql": "obfuscated",
                "nbs.action_tracer.slow_sql": True,
                "nbs.action_tracer.slow_sql_threshold": 500,
                "nbs.ignored_params": "",
                "nbs.error_collector.ignored_status_codes": "",
                "nbs.urls_captured": "/cargo/detail/6/\\n/cargo/detail/7/",
            }
        }
        snapshot = merge_settings(server_conf)

        self.assertTrue(hasattr(snapshot, "applicationId"), "merge attribute failed.")
        self.assertEqual(snapshot.applicationId, "1233", "merge attribute failed.")

        self.assertTrue(hasattr(snapshot, "enabled"), "merge attribute failed.")
        self.assertEqual(snapshot.enabled, True, "merge attribute failed.")

        self.assertTrue(hasattr(snapshot, "appSessionKey"), "merge attribute failed.")
        self.assertEqual(snapshot.appSessionKey, "rwreqrq", "merge attribute failed.")

        self.assertTrue(hasattr(snapshot, "apdex_t"), "merge attribute failed.")
        self.assertEqual(snapshot.apdex_t, 25, "merge attribute failed.")

        self.assertTrue(hasattr(snapshot, "error_collector"), "merge attribute failed.")
        self.assertEqual(snapshot.error_collector.enabled, True, "merge attribute failed.")

        self.assertTrue(hasattr(snapshot, "capture_params"), "merge attribute failed.")
        self.assertEqual(snapshot.capture_params, True, "merge attribute failed.")


if __name__ == "__main__":
    unittest.main()
