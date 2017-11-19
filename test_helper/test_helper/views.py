#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.http import JsonResponse
import redis
from pymemcache.client.base import Client


def upload(requests):
    res = upload_ret_460()
    return JsonResponse(res)


def redirect(requests):
    res = redirect_ret_success()
    return JsonResponse(res)


def init(requests):
    res = init_ret_success()
    return JsonResponse(res)


def upload_ret_error():
    return {
        "status":"error",
        "result":{
            "errorCode":-1,
            "errorMessage":"server internal error"
        }
    }


def upload_ret_460():
    return {
        "status":"error",
        "result":{
            "errorCode":460,
            "errorMessage":"Invalid license key"
        }
    }


def upload_ret_461():
    return {
        "status":"error",
        "result":{
            "errorCode":461,
            "errorMessage":"Invalid license key"
        }
    }


def upload_ret_470():
    return {
        "status":"error",
        "result":{
            "errorCode":470,
            "errorMessage":"Invalid license key"
        }
    }


def redirect_ret_success():
    return {
        "status": "success",
        "result": "127.0.0.1"
    }


def init_ret_success():
    return {
        "status": "success"
    }

def redis_tst(self):
    r = redis.StrictRedis(host='xuni.com', port=6379, db=0)
    r.set('foo', 'bar')
    r.get('foo')
    return HttpResponse(r.get('foo'))

def memcache_tst(self):
    client = Client(('xuni.com', 11211))
    client.set('some_key', 'some_value')
    result = client.get('some_key')
    return HttpResponse(client.get('some_key'))
