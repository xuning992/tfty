# -*- coding: utf-8 -*-

from tingyun.config.settings import merge_settings
import unittest


class TestMergeSettingQuantile(unittest.TestCase):
    def setUp(self):
        # unittest.TestCase.setUp(self)
        self.server_side_config = {u'apdex_t': 500, u'applicationId': 127193, u'hotspotPeriod': 600, u'enabled': True,
                                   u'dataSentInterval': 60, u'appSessionKey': u'161006', u'hotspotRules': u'',
                                   u'config': {u'nbs.ignored_params': u'', u'nbs.quantile': u'[]',
                                               u'nbs.ignore_static_resources': True,
                                               u'nbs.action_tracer.record_sql': u'obfuscated',
                                               u'nbs.error_collector.enabled': True, u'nbs.rum.mix_enabled': False,
                                               u'nbs.action_tracer.nbsua': False,
                                               u'nbs.action_tracer.stack_trace_threshold': 500,
                                               u'nbs.external_url_params_captured': u'',
                                               u'nbs.auto_action_naming': False,
                                               u'nbs.action_tracer.action_threshold': 1,
                                               u'nbs.action_tracer.slow_sql_threshold': 500,
                                               u'nbs.action_tracer.explain_enabled': True, u'nbs.agent_enabled': True,
                                               u'nbs.hotspot.enabled': False, u'nbs.instrumentation_custom': u'[]',
                                               u'nbs.rum.sample_ratio': 1.0, u'nbs.capture_params': False,
                                               u'nbs.action_tracer.enabled': True,
                                               u'nbs.transaction_tracer.thrift': False,
                                               u'nbs.transaction_tracer.enabled': True,
                                               u'nbs.action_tracer.slow_sql': True,
                                               u'nbs.action_tracer.obfuscated_sql_fields': u'',
                                               u'nbs.urls_captured': u'',
                                               u'nbs.action_tracer.action_name_functions': u'',
                                               u'nbs.error_collector.ignored_errors': u'',
                                               u'nbs.action_tracer.remove_trailing_path': False,
                                               u'nbs.error_collector.ignored_status_codes': u'',
                                               u'nbs.rum.enabled': False, u'nbs.error_collector.record_db_errors': True,
                                               u'nbs.rum.script': u'', u'nbs.action_tracer.explain_threshold': 500,
                                               u'nbs.web_action_uri_params_captured': u''},
                                   u'tingyunIdSecret': u'QPo-y6LCVc8|fWas9t8eaLs#1LWVcVhU4GA'}

    def tearDown(self):
        # unittest.TestCase.tearDown(self)
        pass

    def test_quantile_1_blank(self):

        print "begin blank"
        quantile_ = []

        self.server_side_config['config']['nbs.quantile'] = quantile_
        result = merge_settings(server_side_config=self.server_side_config)
        try:
            quantile_raw = result['quantile']
        except Exception as err:
            print "blank`s server_config: %s " % result
            quantile_raw = "fail"

        self.assertEqual(quantile_raw, [])

    def test_quantile_2_str(self):

        print "begin str"
        quantile_ = ['abc', 'DE', 'FFFF']

        self.server_side_config['config']['nbs.quantile'] = quantile_
        result = merge_settings(self.server_side_config)
        try:
            quantile_raw = result['quantile']
        except Exception as err:
            print "str`s server_config: %s " % result
            quantile_raw = "fail"

        self.assertEqual(quantile_raw, [])

    def test_quantile_3_float(self):

        print "begin float"
        quantile_ = [12.4, 98.9]

        self.server_side_config['config']['nbs.quantile'] = quantile_
        result = merge_settings(self.server_side_config)
        try:
            quantile_raw = result['quantile']
        except Exception as err:
            print "float`s server_config: %s " % result
            quantile_raw = "fail"

        self.assertEqual(quantile_raw, [])

    def test_quantile_4_specail_str(self):

        print "begin specail str"
        quantile_ = [[], '\\']

        self.server_side_config['config']['nbs.quantile'] = quantile_
        result = merge_settings(self.server_side_config)
        try:
            quantile_raw = result['quantile']
        except Exception as err:
            print "special str`s server_config: %s " % result
            quantile_raw = "fail"

        self.assertEqual(quantile_raw, [])

    def test_quantile_5_five(self):

        print "begin five"
        quantile_ = [1, 25, 50, 75, 99]

        self.server_side_config['config']['nbs.quantile'] = quantile_
        result = merge_settings(self.server_side_config)
        try:
            quantile_raw = result['quantile']
        except Exception as err:
            print "five`s server_config: %s " % result
            quantile_raw = "fail"

        self.assertEqual(quantile_raw, [])

    def test_quantile_6_negative(self):

        print "begin negative"
        quantile_ = [-1]

        self.server_side_config['config']['nbs.quantile'] = quantile_
        result = merge_settings(self.server_side_config)
        try:
            quantile_raw = result['quantile']
        except Exception as err:
            print "negative`s server_config: %s " % result
            quantile_raw = "fail"

        self.assertEqual(quantile_raw, [])

    def test_quantile_7_out_range(self):

        print "begin out range"
        quantile_ = [100, 100000000]

        self.server_side_config['config']['nbs.quantile'] = quantile_
        result = merge_settings(self.server_side_config)
        try:
            quantile_raw = result['quantile']
        except Exception as err:
            print "out range`s server_config: %s " % result
            quantile_raw = "fail"

        self.assertEqual(quantile_raw, [])

if __name__ == "__main__":
    unittest.main()
