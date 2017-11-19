#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""used to test the logging module of the agent

"""

import logging
import os
import threading
import unittest

import tingyun.embattle.log_file
from tingyun.embattle.log_file import initialize_logging

thread_test_log = "/tmp/thread_test_log.log"
write_separate_msg = "test separated log.."


def inline_test_threading():
    """
    :return:
    """
    tingyun.embattle.log_file._initialized = False
    initialize_logging(thread_test_log, logging.DEBUG)
    _logger = logging.getLogger("tingyun.api")
    _logger.debug(write_separate_msg)


class TestLogFileCase(unittest.TestCase):
    """
    """
    def setUp(self):
        self.test_log = "/tmp/test_log.log"
        self.thread_test_log = thread_test_log
        self.clear_env()
        unittest.TestCase.setUp(self)
        
    def tearDown(self):
        self.clear_env()
        unittest.TestCase.tearDown(self)

    def clear_env(self):
        """
        """
        if os.path.isfile(self.test_log):
            os.remove(self.test_log)

        if os.path.isfile(self.thread_test_log):
            os.remove(self.thread_test_log)
        
    def test_initialize_logging(self):
        """
        """
        self.clear_env()

        # reset the log status
        tingyun.embattle.log_file._initialized = False
        initialize_logging(self.test_log, logging.DEBUG)
        _logger = logging.getLogger("tingyun." + __name__)
        _logger.debug("test for log.")

        self.assertTrue(os.path.isfile(self.test_log), "test log failed...")

        self.clear_env()

    def test_log_separation(self):
        """
        :return:
        """
        self.clear_env()
        global write_separate_msg

        _logger = logging.getLogger()
        _logger.addHandler(logging.FileHandler(self.test_log))
        _logger.setLevel(logging.DEBUG)
        write_msg = "Other threading write."
        _logger.info(write_msg)

        test_thread = threading.Thread(target=inline_test_threading)
        test_thread.start()
        test_thread.join()

        test_log_sign = False
        log_separate_sign = True
        for line in open(self.test_log):
            if write_msg == line.strip("\n"):
                test_log_sign = True

            if write_separate_msg == line.strip("\n"):
                log_separate_sign = False

        self.assertTrue(test_log_sign, "the root log is not write to log.")
        self.assertTrue(log_separate_sign, "the agent log is appear in root log")

        test_log_sign = False
        log_separate_sign = True
        for line in open(self.thread_test_log):
            if write_msg == line.strip("\n"):
                test_log_sign = True

            if -1 != line.find(write_separate_msg):
                log_separate_sign = False

        self.assertFalse(test_log_sign, "the root log is appear in agent log.")
        self.assertFalse(log_separate_sign, "the agent log is not appear in root log")

        self.clear_env()

        
if __name__ == "__main__":
    unittest.main()
