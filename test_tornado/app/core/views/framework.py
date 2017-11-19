#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time

from tornado import httpclient
from tornado import gen

from core.views.base import BaseHandler
from core.views.base import JsonView


class HelloHandler(BaseHandler):
    def get(self):
        self.write({
            "name": "tom"
        })


class RespError500(BaseHandler):
    def get(self):
        a = 1 / 0
        self.write("500")


class OnFinishHandler(BaseHandler):
    def get(self):
        self.write("on finish")
        self.on_finish()


class FinishHandler(BaseHandler):
    def get(self):
        self.write("finish")
        self.finish()


class InitializeHandler(BaseHandler):
    '''tornado.web.RequestHandler:initialize
    '''

    def initialize(self, db=None):
        self.db = db

    def get(self):
        self.write("Get db from initialize：{db}".format(db=self.db))


class PrepareHandler(BaseHandler):
    '''tornado.web.RequestHandler:prepare
    '''

    def prepare(self):
        self.pre = "prepare"

    def get(self):
        self.write("Get info from prepare: {pre}".format(pre=self.pre))


class RequestMethodHandler(BaseHandler):
    '''request
    '''

    def get(self):
        self.write("request method : {method}".format(method="GET"))

    def post(self):
        self.write("request method : {method}".format(method="POST"))

    def put(self):
        self.write("request method : {method}".format(method="PUT"))

    def delete(self):
        self.write("request method : {method}".format(method="DELETE"))

    def patch(self):
        self.write("request method : {method}".format(method="PATCH"))

    def head(self):
        self.write("request method : {method}".format(method="HEAD"))

    def options(self):
        self.write("request method : {method}".format(method="OPTIONS"))


class RenderHandler(BaseHandler):
    '''render
    '''

    def get(self):
        self.render("hello.html")


class HttpClientHandler(BaseHandler):
    def get(self):
        start_time = time.time()
        resp = []

        http_client = httpclient.HTTPClient()
        for url in ["https://baidu.com/"]:
            response = http_client.fetch(url)
            resp.append(response)
        self.write("HttpClient fetch url cost {time} response : {r}".format(time=time.time() - start_time, r=resp))


class AsyncHttpClientHandler(BaseHandler):
    @gen.coroutine
    def get(self):
        http_client = httpclient.AsyncHTTPClient()
        page = yield http_client.fetch("http://baidu.com/", self.handle_response)
        self.write(page.body)

    def handle_response(self, response):
        if response.error:
            return "AsyncHttpClient Request get error: {e}".format(e=response.error)
        else:
            return "AsyncHttpClient Request get response: {response}".format(response=response)


class CoroutineHandler(BaseHandler):
    @gen.coroutine
    def get(self):
        http_client = httpclient.AsyncHTTPClient()
        resp = yield [http_client.fetch(url) for url in ["https://www.baidu.com/"]]
        self.write("Coroutine Request get response: {response}".format(response=resp))
