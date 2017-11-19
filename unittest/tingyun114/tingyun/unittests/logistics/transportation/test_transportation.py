#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""used to test the uploader module of the agent

"""


import unittest
import os
import logging
from tingyun.logistics.transportation import transmitter
from tingyun.logistics.transportation.engine import connect_url, create_connection, Engine
from tingyun.embattle.log_file import initialize_logging
from tingyun.config.settings import global_settings
from tingyun.armoury.sampler.environment import env_config


redirect_hosts = ["dc1.networkbench.com", "dc2.networkbench.com", "redirect.networkbench.com",
                  "dcs1dev.networkbench.com", "dc3.networkbench.com", "dc3.networkbench.com",
                  "dc1dev.networkbench.com", "dc2dev.networkbench.com", "dc3dev.networkbench.com"]


class TestUploaderCase(unittest.TestCase):
    """
    """
    def setUp(self):
        unittest.TestCase.setUp(self)

    def tearDown(self):
        unittest.TestCase.tearDown(self)

    def test_connect_url(self):
        """
        """
        actual = "https://redirect.networkbench.com/getRedirectHost/?licenseKey=999-999-999"
        ret_url = connect_url("getRedirectHost") + "/?licenseKey=999-999-999"

        self.assertEqual(actual, ret_url, "url error..")

    def test_transmitter(self):
        """
        """
        # prepare the log environment for test
        test_log = os.path.join(os.path.dirname(__file__), "test.log")
        initialize_logging(test_log, logging.DEBUG)

        url = connect_url("getRedirectHost")
        # redirect_url = transmitter(None, url, "getRedirectHost", param={"licenseKey": "999-999-999"})
        # self.assertTrue(redirect_url, "get url error.")

        try:
            host = transmitter(None, url, "getRedirectHost", param={"licenseKey": "8sadf8-8fsd8-fds88"})
        except Exception as _:
            host = ""
        # self.assertTrue(host in redirect_hosts, "")

        local_conf = {
            "host": "dev.agent.com",
            "appName": ["PythonApp", ],
            "language": "Python",
            "agentVersion": "1.0",
            "config": {"nbs.enabled": "true"},
            "env": {"Os": "linux"}
        }

        # url = connect_url("initAgentApp", host, with_port=False)
        # server_conf = transmitter(None, url, "initAgentApp", local_conf, {"licenseKey": "999-999-999"})
        #
        # self.assertTrue("config" in server_conf, "")
        # self.assertTrue(isinstance(server_conf["config"], dict), "")
        #
        # self.assertTrue("applicationId" in server_conf, "")
        # self.assertTrue("enabled" in server_conf, "")
        # self.assertTrue("appSessionKey" in server_conf, "")
        # self.assertTrue("dataSentInterval" in server_conf, "")
        # self.assertTrue("apdex_t" in server_conf, "")

        if os.path.isfile(test_log):
            os.remove(test_log)

    def test_create_connection(self):
        """
        """
        settings = global_settings()
        settings.license_key = "999-999-999"
        test_log = os.path.join(os.path.dirname(__file__), "test.log")
        initialize_logging(test_log, logging.DEBUG)

        session = create_connection("999-999-999", "Python App Test", [], env_config(), settings)
        self.assertTrue(isinstance(session, Engine), "")

        if os.path.isfile(test_log):
            os.remove(test_log)

    def test_private(self):
        """
        :return:
        """
        settings = global_settings()
        settings.license_key = "999-999-999"
        settings.log_file = os.path.join(os.path.dirname(__file__), "test.log")
        settings.host = '192.168.2.81'
        settings.port = 8081

        url = connect_url("getRedirectHost", with_port=True)
        self.assertEqual(url, 'https://192.168.2.81:8081/getRedirectHost')

        url = connect_url("getRedirectHost", host='192.168.2.82:8081', with_port=False)
        self.assertEqual(url, 'https://192.168.2.82:8081/getRedirectHost')

        # recovery the default settings
        settings.host = 'redirect.networkbench.com'


if __name__ == "__main__":
    unittest.main()
