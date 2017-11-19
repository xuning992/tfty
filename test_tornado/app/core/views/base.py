#!/usr/bin/env python
# -*- coding: utf-8 -*-

# import redis
from tornado.web import RequestHandler
from tornado.web import HTTPError
from tornado import gen
from enum import Enum as IntEnum
import json
import ujson

DEBUG = 0

class BaseHandler(RequestHandler):
    def prepare(self):
        content_type = self.request.headers.get('Content-Type', '')

        if content_type and content_type.startswith("application/json"):
            try:
                self.json_args = json.loads(self.request.body)
            except:
                self.json_args = None
        else:
            self.json_args = None

    def get_application_json(self, bit_str=None):
        if not bit_str:
            return {}
        try:
            dic = bit_str.decode('utf-8')
        except Exception as e:
            dic = {}
        return dict(json.loads(dic))

    def tag_is_equal(self, tag1, tag2):
        if tag1.lower().strip().strip('/') == tag2.lower().strip().strip('/'):
            return True
        return False

    def resp_200(self, res={}):
        ret = {
            'resp_code': 200,
            'resp_msg': 'success',
            'data': res
        }
        self.write(ret)

    def resp_400(self, res={}):
        ret = {
            'resp_code': 400,
            'resp_msg': '参数错误',
            'data': res
        }
        self.write(ret)

    def resp_404(self, res={}):
        ret = {
            'resp_code': 404,
            'resp_msg': '数据不存在',
            'data': res
        }
        self.write(ret)

    def resp_500(self, res={}):
        ret = {
            'resp_code': 500,
            'resp_msg': 'error',
            'data': res
        }
        self.write(ret)


class JSONBaseHandler(BaseHandler):
    def prepare(self):
        # mc.reset()
        super(BaseHandler, self).prepare()

    def decode_argument(self, value, name=None):
        return value

    def redirect(self, url, permanent=False):
        """Sends a redirect to the given (optionally relative) URL."""
        if self._headers_written:
            raise Exception('Cannot redirect after headers have been written')
        self.set_status(301 if permanent else 302)
        self.set_header('Location', url)
        self.finish()

    def render_error_html(self):
        """
        显示
        :return:
        """
        context = dict()
        if context:
            context["arguments"] = self.request.arguments
            context["url"] = self.request.uri
            context["cookies"] = self.cookies
            self.render_error_html()
            from tornado.template import Template
            return Template(HTML).generate(**context)
            # return self.render_string("error.html",
            #                           **context)
        return ""

    def alarm_exception(self, html, error=None):
        if html:
            pass

    def _execute(self, transforms, *args, **kwargs):
        """Executes this request with the given output transforms."""
        self._transforms = transforms
        try:
            if self.request.method not in self.SUPPORTED_METHODS:
                raise HTTPError(405)
            # If XSRF cookies are turned on, reject form submissions without
            # the proper cookie
            # if self.request.method not in ('GET', 'HEAD', 'OPTIONS') and \
            #   self.application.settings.get('xsrf_cookies'):
            #    self.check_xsrf_cookie()
            self.prepare()
            if not self._finished:
                args = [self.decode_argument(arg) for arg in args]
                kwargs = dict((k, self.decode_argument(v, name=k))
                              for (k, v) in kwargs.iteritems())
                if hasattr(self, 'init'):
                    getattr(self, 'init')(*args, **kwargs)
                getattr(self, self.request.method.lower())(*args, **kwargs)
                if self._auto_finish and not self._finished:
                    self.finish()
        except Exception, e:
            self._handle_request_exception(e)

    def _handle_request_exception(self, exception):
        if DEBUG:
            error_html = self.render_error_html()
            self.alarm_exception(error_html, exception)
        return super(BaseHandler, self)._handle_request_exception(exception)


def write_error(self, status_code, **kwargs):
    '''回写API类的异常.
    '''
    self.set_header('Content-Type', 'application/json; charset=UTF-8')

    self.finish(
        {
            'code': status_code,
            'message': ''.join(self._reason)
        }
    )


# tornado.web.RequestHandler.write_error = write_error
def map_intenum(data):
    if isinstance(data, IntEnum):
        return data.value
    if isinstance(data, dict):
        return {k: map_intenum(v) for k, v in data.iteritems()}
    if isinstance(data, (list, tuple)):
        return [map_intenum(v) for v in data]
    return data


class CObjectsEncoder(json.JSONEncoder):
    def iterencode(self, o, _one_shot=False):
        o = map_intenum(o)
        return super(CObjectsEncoder, self).iterencode(o, _one_shot)

    def default(self, o):
        if isinstance(o, IntEnum):
            return {'__class__': o.__class__.__name__,
                    '__value__': (o.value,)}
        return super(CObjectsEncoder, self).default(o)


class JsonView(JSONBaseHandler):
    pass

    SUPPORTED_METHODS = ('POST', 'GET')

    write_error = write_error

    def prepare(self):
        self.content_type = self.request.headers.get('content-type')
        super(JsonView, self).prepare()

    @gen.coroutine
    def _execute(self, transforms, *args, **kwargs):
        self._transforms = transforms
        try:
            if self.request.method not in self.SUPPORTED_METHODS:
                raise HTTPError(405)
            # self.prepare()
            try:
                result = self.prepare()
                if result is not None:
                    result = yield result
            except Exception as e:
                self.finish(e.dump())

            if self._prepared_future is not None:
                self._prepared_future.set_result(None)
            if self._finished:
                return

            args = [self.decode_argument(arg) for arg in args]
            kwargs = dict((k, self.decode_argument(v, name=k))
                          for (k, v) in kwargs.iteritems())
            if hasattr(self, 'init'):
                getattr(self, 'init')(*args, **kwargs)
            try:
                method = getattr(self, self.request.method.lower())
                result = method(*args, **kwargs)
                if result is not None:
                    yield result
            except Exception as e:
                # self._handle_request_exception(e)
                self.finish(e.dump())

            if self._auto_finish and not self._finished:
                self.finish()
        except Exception, e:
            # 回写异常, 并结束异常请求.
            self._handle_request_exception(e)

    def render(self, chunk):
        default_response = {
            'code': 200,
            'message': 'OK'
        }
        if not chunk:
            chunk = default_response
        # self.set_header('Content-Type', 'application/json; charset=UTF-8')
        chunk.update(default_response)
        self.finish(chunk)

    def finish(self, chunk={}):
        callback = self.get_argument('callback', None)
        if callback:
            if type(chunk) is dict:
                chunk = ujson.dumps(chunk, ensure_ascii=False)
            chunk = '%s(%s)' % (callback, chunk)
        self.set_header('Content-Type', 'application/json; charset=UTF-8')

        if isinstance(chunk, dict):
            super(JsonView, self).finish(ujson.dumps(chunk, ensure_ascii=False))
        else:
            super(JsonView, self).finish(chunk)
        # super(JsonView, self).finish(dumps(chunk))
        # super(JsonView, self).finish(json.dumps(chunk))


HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta http-equiv="content-type" content="text/html; charset=utf-8">
  <meta name="robots" content="NONE,NOARCHIVE">
  <title>Error Report: {{ repr(exception) }}</title>
  <style type="text/css">
    html * { padding:0; margin:0; }
    body * { padding:10px 20px; }
    body * * { padding:0; }
    body { font:small sans-serif; }
    body>div { border-bottom:1px solid #ddd; }
    h1 { font-weight:normal; }
    h2 { margin-bottom:.8em; }
    h2 span { font-size:80%; color:#666; font-weight:normal; }
    h3 { margin:1em 0 .5em 0; }
    h4 { margin:0 0 .5em 0; font-weight: normal; }
    code, pre { font-size: 100%; white-space: pre-wrap; }
    table { border:1px solid #ccc; border-collapse: collapse; width:100%; background:white; }
    tbody td, tbody th { vertical-align:top; padding:2px 3px; }
    thead th { padding:1px 6px 1px 3px; background:#fefefe; text-align:left; font-weight:normal; font-size:11px; border:1px solid #ddd; }
    tbody th { width:12em; text-align:right; color:#666; padding-right:.5em; }
    table.vars { margin:5px 0 2px 40px; }
    table.vars td, table.req td { font-family:monospace; }
    table td.code { width:100%; }
    table td.code pre { overflow:hidden; }
    table.source th { color:#666; }
    table.source td { font-family:monospace; white-space:pre; border-bottom:1px solid #eee; }
    ul.traceback { list-style-type:none; color: #222; }
    ul.traceback li.frame { padding-bottom:1em; color:#666; }
    ul.traceback li.user { background-color:#e0e0e0; color:#000 }
    div.context { padding:10px 0; overflow:hidden; }
    div.context ol { padding-left:30px; margin:0 10px; list-style-position: inside; }
    div.context ol li { font-family:monospace; white-space:pre; color:#777; cursor:pointer; }
    div.context ol li pre { display:inline; }
    div.context ol.context-line li { color:#505050; background-color:#dfdfdf; }
    div.context ol.context-line li span { position:absolute; right:32px; }
    .user div.context ol.context-line li { background-color:#bbb; color:#000; }
    .user div.context ol li { color:#666; }
    div.commands { margin-left: 40px; }
    div.commands a { color:#555; text-decoration:none; }
    .user div.commands a { color: black; }
    #summary { background: #ffc; }
    #summary h2 { font-weight: normal; color: #666; }
    #explanation { background:#eee; }
    #template, #template-not-exist { background:#f6f6f6; }
    #template-not-exist ul { margin: 0 0 0 20px; }
    #unicode-hint { background:#eee; }
    #traceback { background:#eee; }
    #requestinfo { background:#f6f6f6; padding-left:120px; }
    #summary table { border:none; background:transparent; }
    #requestinfo h2, #requestinfo h3 { position:relative; margin-left:-100px; }
    #requestinfo h3 { margin-bottom:-1em; }
    .error { background: #ffc; }
    .specific { color:#cc3300; font-weight:bold; }
    h2 span.commands { font-size:.7em;}
    span.commands a:link {color:#5E5694;}
    pre.exception_value { font-family: sans-serif; color: #666; font-size: 1.5em; margin: 10px 0 10px 0; }
  </style>

  <script type="text/javascript">
  //<!--
    function getElementsByClassName(oElm, strTagName, strClassName){
        // Written by Jonathan Snook, http://www.snook.ca/jon; Add-ons by Robert Nyman, http://www.robertnyman.com
        var arrElements = (strTagName == "*" && document.all)? document.all :
        oElm.getElementsByTagName(strTagName);
        var arrReturnElements = new Array();
        strClassName = strClassName.replace(/\-/g, "\\-");
        var oRegExp = new RegExp("(^|\\s)" + strClassName + "(\\s|$)");
        var oElement;
        for(var i=0; i<arrElements.length; i++){
            oElement = arrElements[i];
            if(oRegExp.test(oElement.className)){
                arrReturnElements.push(oElement);
            }
        }
        return (arrReturnElements)
    }
    function hideAll(elems) {
      for (var e = 0; e < elems.length; e++) {
        elems[e].style.display = 'none';
      }
    }
    window.onload = function() {
      hideAll(getElementsByClassName(document, 'table', 'vars'));
      hideAll(getElementsByClassName(document, 'ol', 'pre-context'));
      hideAll(getElementsByClassName(document, 'ol', 'post-context'));
      hideAll(getElementsByClassName(document, 'div', 'pastebin'));
    }
    function toggle() {
      for (var i = 0; i < arguments.length; i++) {
        var e = document.getElementById(arguments[i]);
        if (e) {
          e.style.display = e.style.display == 'none' ? 'block': 'none';
        }
      }
      return false;
    }
    function varToggle(link, id) {
      toggle('v' + id);
      var s = link.getElementsByTagName('span')[0];
      var uarr = String.fromCharCode(0x25b6);
      var darr = String.fromCharCode(0x25bc);
      s.innerHTML = s.innerHTML == uarr ? darr : uarr;
      return false;
    }
    function switchPastebinFriendly(link) {
      s1 = "Switch to copy-and-paste view";
      s2 = "Switch back to interactive view";
      link.innerHTML = link.innerHTML == s1 ? s2: s1;
      toggle('browserTraceback', 'pastebinTraceback');
      return false;
    }
    //-->
  </script>
</head>
<body>
<div id="summary">
    <h2>Exception: {{ repr(exception) }}</h2>
</div>

<div id="traceback">
  <h2>Traceback</h2>

  <div id="browserTraceback">
    <ul class="traceback">
      {% for frame in frames %}
        <li class="frame {{ frame["type"] }}">
          <code>{{ frame["filename"] }}</code> in <code>{{ frame["tb"].tb_frame.f_code.co_name }}}</code>

          {% if frame["context_line"] %}
            <div class="context" id="c{{ frame["id"] }}">
              <ol start="{{ frame["pre_context_lineno"] }}" class="pre-context" id="pre{{ frame["id"] }}">
                {% for line in frame["pre_context"] %}<li onclick="toggle('pr{{ frame["id"] }}', 'post{{ frame["id"] }}')"><pre>{{ line }}</pre></li>{% end %}</ol>
              <ol start="{{ frame["lineno"] }}" class="context-line"><li onclick="toggle('pre{{ frame["id"] }}', 'post{{ frame["id"] }}')"><pre>{{ frame["context_line"] }}</pre></li></ol>
              <ol start='{{ frame["lineno"] }}' class="post-context" id="post{{ frame["id"] }}">{% for line in frame["post_context"] %}<li onclick="toggle('pre{{ frame["id"] }}', 'post{{ frame["id"] }}')"><pre>{{ line }}</pre></li>{% end %}</ol>
            </div>
          {% end %}

          {% if frame["vars"] %}
            <div class="commands">
                <a href="#" onclick="return varToggle(this, '{{ frame["id"] }}')"><span>&#x25b6;</span> Local vars</a>
            </div>
            <table class="vars" id="v{{ frame["id"] }}">
              <thead>
                <tr>
                  <th>Variable</th>
                  <th>Value</th>
                </tr>
              </thead>
              <tbody>
                {% for k, v in frame["vars"].iteritems() %}
                  <tr>
                    <td>{{ k }}</td>
                    <td class="code"><pre>{{ repr(v) }}</pre></td>
                  </tr>
                {% end %}
              </tbody>
            </table>
          {% end %}
        </li>
      {% end %}
    </ul>
  </div>
</div>
<div id="requestinfo">
    <h2>URL: {{url}}</h2>
    <h2>Request Arguments</h2>
    <div>
        <table>
          <thead>
            <tr>
              <th>Variable</th>
              <th>Value</th>
            </tr>
          </thead>
          <tbody>
            {% for k, v in arguments.iteritems() %}
              <tr>
                <td>{{ k }}</td>
                <td class="code"><pre>{{ repr(v) }}</pre></td>
              </tr>
            {% end %}
          </tbody>
        </table>
    </div>
    <br>
    <h2>Request Cookies</h2>
    <div>
        <table>
          <thead>
            <tr>
              <th>Variable</th>
              <th>Value</th>
            </tr>
          </thead>
          <tbody>
            {% for cookie in cookies.values() %}
              <tr>
                <td>{{ cookie.key }}</td>
                <td class="code"><pre>{{ cookie.value }}</pre></td>
              </tr>
            {% end %}
          </tbody>
        </table>
    </div>
</div>
</body>
</html>
"""
