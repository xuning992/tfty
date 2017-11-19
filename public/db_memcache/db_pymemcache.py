#!/usr/bin/env python
# -*- coding: utf-8 -*-
from public.db_util import common_set, common_get, common_delete, common_set_many, common_get_many, common_delete_many
from ..config import MEMCACHE_CONF

class PymemcacheCtl():
    def __init__(self, v):
        self.v = v

    def __enter__(self):
        if self.v == "1.2.0":
            from public.packages.pymemcache.v120.pymemcache import client
        elif self.v == "1.3.0":
            from public.packages.pymemcache.v130 import pymemcache
            from public.packages.pymemcache.v130.pymemcache.client import hash
        elif self.v == "1.4.0":
            print "get pymemcache 1.4.0"
            from public.packages.pymemcache.v140 import pymemcache
            from public.packages.pymemcache.v140.pymemcache.client import hash

        if self.v in ['1.3.0', '1.4.0']:
            self.client = pymemcache.client.Client((MEMCACHE_CONF['host'], int(MEMCACHE_CONF['port'])))
            self.hash_client = hash.HashClient([(MEMCACHE_CONF['host'], int(MEMCACHE_CONF['port']))])
        elif self.v == '1.2.0':
            self.client = client.Client((MEMCACHE_CONF['host'], int(MEMCACHE_CONF['port'])))
            self.hash_client = None

        return self.client, self.hash_client

    def __exit__(self, type, value, tb):
        self.client.close()
        # if self.hash_client is not None:
        #     self.hash_client.close()


def pymemcache_set(v):
    with PymemcacheCtl(v) as pymemcache_ctl:
        return common_set(pymemcache_ctl[0])


def pymemcache_set_multi(v):
    with PymemcacheCtl(v) as pymemcache_ctl:
        return common_set_many(pymemcache_ctl[0])


def pymemcache_get(v):
    with PymemcacheCtl(v) as pymemcache_ctl:
        return common_get(pymemcache_ctl[0])


def pymemcache_get_multi(v):
    with PymemcacheCtl(v) as pymemcache_ctl:
        return common_get_many(pymemcache_ctl[0])


def pymemcache_delete(v):
    with PymemcacheCtl(v) as pymemcache_ctl:
        return common_delete(pymemcache_ctl[0])


def pymemcache_delete_multi(v):
    with PymemcacheCtl(v) as pymemcache_ctl:
        return common_delete_many(pymemcache_ctl[0])


def pymemcache_conn_by_client(v):
    with PymemcacheCtl(v) as pymemcache_ctl:
        return common_get(pymemcache_ctl[0])


def pymemcache_conn_by_hashclient(v):
    with PymemcacheCtl(v) as pymemcache_ctl:
        if pymemcache_ctl[1]:
            return common_get(pymemcache_ctl[1])
        else:
            return "pymemcache-{v} has not attr HashClient".format(v=v)
