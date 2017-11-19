#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""used to test the profile module of the agent

"""
import json
import unittest

from tingyun.armoury.sampler.profile import Profile, ProfileTraceNode


class TestProfileCase(unittest.TestCase):
    """
    """
    def setUp(self):
        self.profile = Profile(123)

        unittest.TestCase.setUp(self)

    def tearDown(self):
        unittest.TestCase.tearDown(self)

    def test_profile_node(self):
        """
        :return:
        """
        root = ProfileTraceNode('Web', 'ProfileNode', 'test_profile_node', 21, {"is_runnable": True})
        self.assertEqual(root.get_child_key(), 'unknown', "empty child node key test error.")

        child = ProfileTraceNode('Web', 'ProfileNode', 'test_profile_child_node', 22, {"is_runnable": True})
        root.append_child("test_profile_child_node", child)
        self.assertTrue(root.has_child())
        self.assertEqual(root.trace_segment, ['ProfileNode', 'test_profile_node', 21])
        self.assertEqual(root.format_data(), [['ProfileNode', 'test_profile_node', 21], 0, 0])

    def test_retrieve_profile_node(self):
        """
        :return:
        """
        root = ProfileTraceNode('Web', 'ProfileNode', 'test_profile_node', 31, {"is_runnable": True})

        child1_1 = ProfileTraceNode('Web', 'ProfileNode', 'test_profile_node_1', 311, {"is_runnable": True})
        child1_2 = ProfileTraceNode('Web', 'ProfileNode', 'test_profile_node_2', 313, {"is_runnable": True})

        child1_2_1 = ProfileTraceNode('Web', 'ProfileNode', 'test_profile_node_2_1', 3131, {"is_runnable": True})
        child1_2_1_1 = ProfileTraceNode('Web', 'ProfileNode', 'test_profile_node_2_1_1', 3131, {"is_runnable": True})
        child1_2_2 = ProfileTraceNode('Web', 'ProfileNode', 'test_profile_node_2_2', 3131, {"is_runnable": True})

        # build the test data node
        root.append_child('test_profile_node_1', child1_1)
        root.append_child('test_profile_node_2', child1_2)
        child1_2_1.append_child('test_profile_node_2_1_1', child1_2_1_1)
        child1_2.append_child('test_profile_node_2_1', child1_2_1)
        child1_2.append_child('test_profile_node_2_2', child1_2_2)

        # parse the data node to the target data structure(according to doc)
        # the root_data node will replace the first node of the data tree(there is root defined above)
        root_data = [['-', 'PythonProfileEntryFunc', 0], 0, 0, []]
        self.profile.retrieve_profile_node(root, root_data)

        self.assertEqual(len(root_data), 4, "")
        self.assertEqual(root_data[0], ['-', 'PythonProfileEntryFunc', 0], "")

        self.assertEqual(len(root_data[3]), 2, "")
        self.assertEqual(len(root_data[3][0]), 4, "")
        self.assertEqual(len(root_data[3][1]), 4, "")

        if root_data[3][0][0][1] == 'test_profile_node_2':
            self.assertEqual(len(root_data[3][0][3]), 2)
            self.assertEqual(len(root_data[3][0][3][1]), 4)

            if root_data[3][0][3][1][0][1] == 'test_profile_node_2_1':
                self.assertEqual(len(root_data[3][0][3][1][3]), 1)
            else:
                self.assertEqual(len(root_data[3][0][3][1][3]), 0)
        else:
            self.assertEqual(len(root_data[3][0][3]), 0)

    def test_update_trace_node_runnable_status(self):
        """
        :return:
        """
        # recovery the tested data.
        self.profile.retrieve_depth = 0
        root = ProfileTraceNode('Web', 'ProfileNode', 'test_profile_node_2', 311, {"is_runnable": True})
        child1 = ProfileTraceNode('Web', 'ProfileNode', 'test_profile_node_2_1', 3131, {"is_runnable": True})
        child2 = ProfileTraceNode('Web', 'ProfileNode', 'test_profile_node_2_2', 3131, {"is_runnable": True})
        root.append_child('test_profile_node_2_1', child1)
        child1.append_child('test_profile_node_2_2', child2)

        self.profile.update_trace_node_runnable_status(root)

        self.assertEqual(root.runnable, 1)
        self.assertEqual(root.non_runnable, 0)

        self.assertEqual(root.children.values()[0].runnable, 1)
        self.assertEqual(root.children.values()[0].non_runnable, 0)

        self.assertEqual(root.children.values()[0].children.values()[0].runnable, 1)
        self.assertEqual(root.children.values()[0].children.values()[0].non_runnable, 0)

        # ensure the count is right
        self.profile.update_trace_node_runnable_status(root)
        self.assertEqual(root.runnable, 1)
        self.assertEqual(root.non_runnable, 0)

        self.assertEqual(root.children.values()[0].runnable, 1)
        self.assertEqual(root.children.values()[0].non_runnable, 0)

        self.assertEqual(root.children.values()[0].children.values()[0].runnable, 1)
        self.assertEqual(root.children.values()[0].children.values()[0].non_runnable, 0)

    def test_update_thread_trace(self):
        """
        :return:
        """
        category = 'Web'
        profile = Profile(456)
        root = ProfileTraceNode(category, 'ProfileNode', 'test_profile_node_2', 311, {"is_runnable": True})
        child1 = ProfileTraceNode(category, 'ProfileNode', 'test_profile_node_2_1', 3131, {"is_runnable": True})
        child2 = ProfileTraceNode(category, 'ProfileNode', 'test_profile_node_2_2', 3131, {"is_runnable": True})
        root.append_child('test_profile_node_2_1', child1)
        child1.append_child('test_profile_node_2_2', child2)

        profile.update_thread_trace(category, root)
        self.assertTrue(category in profile.stacktraces, "")

        profile.update_thread_trace(category, root)
        self.assertTrue(category in profile.stacktraces, "")

        self.assertEqual(profile.stacktraces[category].runnable, 1, "")
        self.assertEqual(profile.stacktraces[category].method_name, 'test_profile_node_2', "")
        second = profile.stacktraces[category].children.values()[0]  # second switch, first node.
        self.assertEqual(second.runnable, 2, "")
        third = second.children.values()[0]  # third switch, first node.
        self.assertEqual(third.runnable, 2, "")

        # non runnable test.
        root_non_runnable = ProfileTraceNode(category, 'ProfileNode', 'test_profile_node_2', 31, {"is_runnable": False})
        child1 = ProfileTraceNode(category, 'ProfileNode', 'test_profile_node_2_1', 3131, {"is_runnable": False})
        child2 = ProfileTraceNode(category, 'ProfileNode', 'test_profile_node_2_2', 3131, {"is_runnable": False})
        root_non_runnable.append_child('test_profile_node_2_1', child1)
        child1.append_child('test_profile_node_2_2', child2)

        profile.update_thread_trace(category, root_non_runnable)

        self.assertEqual(profile.stacktraces[category].runnable, 1, "")
        self.assertEqual(profile.stacktraces[category].method_name, 'test_profile_node_2', "")
        second = profile.stacktraces[category].children.values()[0]  # second switch, first node.
        self.assertEqual(second.runnable, 2, "")
        self.assertEqual(second.non_runnable, 1, "")
        third = second.children.values()[0]  # third switch, first node.
        self.assertEqual(third.runnable, 2, "")
        self.assertEqual(third.non_runnable, 1, "")

    def test_profile_data(self):
        """
        :return:
        """
        category = 'Web'
        profile = Profile(456)
        # this node will be drop in retrieve_profile_node(), and add in profile_data(), so we should make a fade one.
        top_node = ProfileTraceNode(category, "-", 'PythonProfileEntryFunc', 0, {"is_runnable": True})
        root = ProfileTraceNode(category, 'ProfileNode', 'test_profile_node_2', 311, {"is_runnable": True})
        child1 = ProfileTraceNode(category, 'ProfileNode', 'test_profile_node_2_1', 3131, {"is_runnable": True})
        child2 = ProfileTraceNode(category, 'ProfileNode', 'test_profile_node_2_2', 3131, {"is_runnable": True})
        root.append_child('test_profile_node_2_1', child1)
        child1.append_child('test_profile_node_2_2', child2)
        top_node.append_child('test_profile_node_2', root)

        top_node_non_runnable = ProfileTraceNode(category, "-", 'PythonProfileEntryFunc', 0, {"is_runnable": False})
        root = ProfileTraceNode(category, 'ProfileNode', 'test_profile_node_2', 31, {"is_runnable": False})
        child1 = ProfileTraceNode(category, 'ProfileNode', 'test_profile_node_2_1', 3131, {"is_runnable": False})
        child2 = ProfileTraceNode(category, 'ProfileNode', 'test_profile_node_2_2', 3131, {"is_runnable": False})

        child1.append_child('test_profile_node_2_2', child2)
        root.append_child('test_profile_node_2_1', child1)
        top_node_non_runnable.append_child('test_profile_node_2', root)

        second_branch = ProfileTraceNode(category, "-", 'PythonProfileEntryFunc', 0, {"is_runnable": False})
        root_se = ProfileTraceNode(category, 'ProfileNode', 'test_profile_node_branch', 31, {"is_runnable": False})
        child_se = ProfileTraceNode(category, 'ProfileNode', 'test_profile_node_branch_1', 3131, {"is_runnable": False})
        child_th = ProfileTraceNode(category, 'ProfileNode', 'test_profile_node_branch_2', 3131, {"is_runnable": False})

        child_se.append_child('test_profile_node_branch_2', child_th)
        root_se.append_child('test_profile_node_branch_1', child_se)
        second_branch.append_child('test_profile_node_branch', root_se)

        profile.update_thread_trace(category, top_node)
        profile.update_thread_trace(category, top_node_non_runnable)
        profile.update_thread_trace(category, second_branch)

        ret = profile.profile_data()

        self.assertTrue('profileId' in ret, "")
        self.assertTrue(ret['profileId'] == 456, "")
        self.assertTrue('beginTime' in ret, "")
        self.assertTrue('endTime' in ret, "")
        self.assertTrue('sampleCount' in ret, "")
        self.assertTrue('threads' in ret, "")
        self.assertTrue('runnableThreads' in ret, "")
        self.assertTrue('stacktraces' in ret, "")
        self.assertNotEqual(ret['stacktraces'], "", "")

        # stack_trace = json.loads(ret['stacktraces'])
        # self.assertTrue('Web' in stack_trace)
        # self.assertTrue('Background' in stack_trace)
        # self.assertTrue('Agent' in stack_trace)
        # self.assertTrue('Other' in stack_trace)
        #
        # self.assertEqual(stack_trace['Other']['threadTraces'], [], "")
        # self.assertEqual(stack_trace['Other']['cpuTime'], 0, "")
        #
        # first = stack_trace['Web']['threadTraces'][0]
        # self.assertEqual(first[0][1], 'PythonProfileEntryFunc', "")
        # self.assertEqual(len(stack_trace['Web']['threadTraces'][0][3]), 2, "should has two branch")
        #
        # second = stack_trace['Web']['threadTraces'][0][3][0]


if __name__ == "__main__":
    unittest.main()
