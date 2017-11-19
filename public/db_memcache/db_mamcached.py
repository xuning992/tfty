#!/usr/bin/env python
# -*- coding: utf-8 -*-
from ..config import MEMCACHE_CONF
from public.db_util import common_set, common_get, common_delete, common_set_multi, common_get_multi, common_delete_multi


class MemcachedCtl():
    def __init__(self, v):
        self.v = v

    def __enter__(self):
        if self.v == "1.47.0":
            from public.packages.pythonmemcached.v1470 import memcache
        elif self.v == "1.58.0":
            from public.packages.pythonmemcached.v1580 import memcache

        host_port = ['%s:%s' % (MEMCACHE_CONF['host'], MEMCACHE_CONF['port'])]
        self.client = memcache.Client(host_port)
        return self.client

    def __exit__(self, type, value, tb):
        self.client.disconnect_all()
    

def memcache_set(v):
    with MemcachedCtl(v) as memcache_ctl:
        return common_set(memcache_ctl)


def memcache_set_multi(v):
    with MemcachedCtl(v) as memcache_ctl:
        return common_set_multi(memcache_ctl)


def memcache_get(v):
    with MemcachedCtl(v) as memcache_ctl:
        return common_get(memcache_ctl)


def memcache_get_multi(v):
    with MemcachedCtl(v) as memcache_ctl:
        return common_get_multi(memcache_ctl)


def memcache_delete(v):
    with MemcachedCtl(v) as memcache_ctl:
        return common_delete(memcache_ctl)


def memcache_delete_multi(v):
    with MemcachedCtl(v) as memcache_ctl:
        return common_delete_multi(memcache_ctl)


def memcache_conn_default(v):
    with MemcachedCtl(v) as memcache_ctl:
        return common_get(memcache_ctl)
