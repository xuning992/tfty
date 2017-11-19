
import json
import logging

from collections import namedtuple
from tingyun.logistics.attribution import TimeMetric, ApdexMetric, TracedError, node_start_time, node_end_time
from tingyun.logistics.attribution import TracedExternalError


console = logging.getLogger(__name__)
_TrackerNode = namedtuple('_TrackerNode', ['type', 'group', 'name', 'start_time', 'end_time', 'request_uri',
                                           'duration', 'http_status', 'exclusive', 'children', 'path', "errors",
                                           "apdex_t", "request_params", "custom_params", "thread_name", "trace_data",
                                           "referer", "slow_sql", "queque_time", "trace_guid", 'trace_id',
                                           "external_error"])


class TrackerNode(_TrackerNode):
    """hold the tracker trace data for collect

    """
    def time_metrics(self):
        """
        :return:
        """
        yield TimeMetric(name=self.path, scope=self.path, duration=self.duration, exclusive=self.exclusive)

        queque_metric = 'GENERAL/WebFrontend/NULL/QueueTime'
        yield TimeMetric(name=queque_metric, scope=queque_metric, duration=self.queque_time, exclusive=self.queque_time)

        for child in self.children:
            for metric in child.time_metrics(self, self):
                yield metric

    def quantile(self):
        """
        :return:
        """
        return self.path, self.duration

    def action_metrics(self):
        """
        :return: the full tracker metric of the top
        """
        if self.type != "WebAction":
            return

        if self.http_status > 400:
            console.debug("Application response with status code `%s` ignore the action data.", self.http_status)
            return

        yield TimeMetric(name=self.path, scope="", duration=self.duration, exclusive=self.exclusive)

    def apdex_metrics(self):
        """
        :return:
        """
        if self.type != "WebAction":
            console.debug("get apdex with none webaction %s", self.type)
            return

        satisfying = 0
        tolerating = 0
        frustrating = 0

        # status code large than 400 but not 401, we think it frustrating
        if (self.http_status >= 400 and self.http_status != 401) or self.errors:
            frustrating = 1
        else:
            if self.duration <= self.apdex_t:
                satisfying = 1
            elif self.duration <= 4 * self.apdex_t:
                tolerating = 1
            else:
                frustrating = 1

        name = self.path.replace("WebAction", "Apdex")
        yield ApdexMetric(name=name, satisfying=satisfying, tolerating=tolerating, frustrating=frustrating,
                          apdex_t=self.apdex_t)

    def traced_error(self):
        """yield the traced errors according to protocol
        :return:
        """
        error_type_cache = []

        for error in self.errors:
            error_filter_key = "%s_|%s_|%s_|%s" % (self.path, error.http_status, error.error_class_name, error.message)
            if error_filter_key in error_type_cache:
                console.debug("Duplicate error `%s` for uri %s", error.error_class_name, self.request_uri)
                continue

            error_item = [error.error_time, self.path, self.http_status, error.error_class_name, error.message,
                          1, self.request_uri]
            stack_detail = []
            for line in error.stack_trace:
                if len(line) >= 4 and 'tingyun' not in line[0]:
                    stack_detail.append("%s(%s:%s)" % (line[2], line[0], line[1]))

            error_params = {"params": {"threadName": error.thread_name, "httpStatus": self.http_status,
                                       "referer": error.referer},
                            "requestParams": error.request_params,
                            "stacktrace": stack_detail
                            }

            error_item.append(json.dumps(error_params))
            error_type_cache.append(error_filter_key)

            yield TracedError(error_filter_key=error_filter_key, tracker_type=error.tracker_type, trace_data=error_item)

    def trace_node(self, root):
        """
        :param root: the root node of the tracker
        :return: traced node
        """
        start_time = node_start_time(root, self)
        end_time = node_end_time(root, self)
        metric_name = self.path
        call_url = self.request_uri
        call_count = 1
        class_name = ""
        method_name = self.name
        params = {}
        children = []

        root.trace_node_count += 1
        for child in self.children:
            if root.trace_node_count > root.trace_node_limit:
                break

            children.append(child.trace_node(root))

        return [start_time, end_time, metric_name, call_url, call_count, class_name, method_name, params, children]

    def slow_action_trace(self, limit, threshold):
        """ the main interface to data engine
        :param limit: the maximum limitation of the nodes
        :param threshold: this value is dynamic from server. then pass from packager
        :return:
        """
        self.trace_node_limit = limit
        self.trace_node_count = 0
        start_time = int(self.start_time)
        duration = self.duration
        trace_id = self.trace_id if self.trace_id else ""
        # not a bug. the trace id indicate it is caller or called with cross trace, if this app is only called, this
        # should be empty
        trace_guid = self.trace_guid if self.trace_id else ""

        # if trace data has the tr attribute, the called has the slow action trace.
        action_trace_invoke = False
        if self.trace_data and self.trace_data.get("tr", False):
            action_trace_invoke = True

        # intercept the illegal data. before access the trace node(spend more sources)
        # now we return the original data with empty trace data. the next step will detect the duration value is less
        # than settings threshold.
        if duration < threshold and not action_trace_invoke:
            return [start_time, duration, self.path, self.request_uri, ""]

        trace_node = self.trace_node(self)
        slow_trace = [start_time, self.request_params, {"httpStatus": self.http_status, "threadName": self.thread_name,
                                                        "referer": self.referer}, trace_node]

        return [start_time, duration, self.path, self.request_uri, json.dumps(slow_trace),
                trace_id, trace_guid]

    def slow_sql_nodes(self):
        """
        :return:
        """
        for item in self.slow_sql:
            yield item.slow_sql_node(self)

    def traced_external_error(self):
        """
        :return:
        """
        for error in self.external_error:
            metric_name = 'External/%s/%s' % (error.url.replace("/", "%2F"), self.name)
            error_item = [error.error_time, metric_name, error.status_code,
                          error.error_class_name, 1, self.path]

            stack_detail = []
            for line in error.stack_trace:
                if len(line) >= 4 and 'tingyun' not in line[0]:
                    stack_detail.append("%s(%s:%s)" % (line[2], line[0], line[1]))

            error_params = {"params": {"threadName": error.thread_name, "httpStatus": self.http_status},
                            "requestParams": error.request_params, "stacktrace": stack_detail}
            error_item.append(json.dumps(error_params))

            error_filter_key = "%s_|%s_|%s" % (metric_name, self.http_status, error.error_class_name)
            yield TracedExternalError(error_filter_key=error_filter_key, trace_data=error_item,
                                      tracker_type=error.tracker_type, status_code=self.http_status)
