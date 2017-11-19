#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time

import requests
from django.http import HttpResponse


URL = "http://192.168.5.140:8080/jdk1.5_External_01_httpclient3.0-4.0/test"


def requests_get(request):
    resp = requests.get(URL)
    time.sleep(2)
    return HttpResponse(resp)