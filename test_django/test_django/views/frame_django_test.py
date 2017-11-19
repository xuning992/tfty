# -*- coding: utf-8- -*-

import datetime
import requests
import os
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.http import HttpResponseForbidden
from django.views import generic
from ..models.test_db import DjangoOrmTest


now = datetime.datetime.now()
content_values = {'now': now, 'view': None}
url = "http://baidu.com/"


def test_template(request):

    content_values['view'] = "test template"
    return render_to_response("test_template.html", content_values)


def func_view(request):
    """
    :param request:
    :return:
    """
    try:
        URL = os.environ("URL")
    except Exception as err:
        URL = url
    resp = requests.get(URL)
    return HttpResponse(resp)


class ClassView(generic.ListView):

    template_name = "class_view.html"
    context_object_name = "django_orm_test"
    model = DjangoOrmTest.objects.using("mysql_mysqldb")

    # print "%s" % locals()
    object_list = []

    def get_queryset(self, **kwargs):
        kwargs['object_list'] = DjangoOrmTest.objects.using("mysql_mysqldb").all()
        return super(ClassView, self).get_context_data(**kwargs)

        # def get_now(self):
        #     content_values['view'] = 'class view && get now time'
        #     return content_values


class BlockedIpMiddleware(object):
    """自定义中间件
    """
    def process_request(self, request):
        if request.META['REMOTE_ADDR'] in ("192.168.2.1", ):
            return HttpResponseForbidden('<h1>Forbidden</h1>')

    def process_response(self, request, response):
        return response
