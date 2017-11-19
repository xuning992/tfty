#!/usr/bin/env python
# -*- coding: utf-8 -*-
from public.db_util import common_set, common_get, common_delete, common_set_multi, common_get_multi, common_delete_multi
from ..config import MEMCACHE_CONF


class BmemcachedCtl():
    def __init__(self, v):
        self.v = v

    def __enter__(self):
        if self.v == "0.20.0":
            from public.packages.bmemcached.v0200 import bmemcached
        elif self.v == "0.21.0":
            from public.packages.bmemcached.v0210 import bmemcached
        elif self.v == "0.22.0":
            from public.packages.bmemcached.v0220 import bmemcached
        elif self.v == "0.23.0":
            from public.packages.bmemcached.v0230 import bmemcached
        elif self.v == "0.24.0":
            from public.packages.bmemcached.v0240 import bmemcached
        elif self.v == "0.25.0":
            from public.packages.bmemcached.v0250 import bmemcached

        b_host_port = "%s:%s" % (MEMCACHE_CONF['host'], MEMCACHE_CONF['port'])
        self.bmemcached_ctl = bmemcached.Client((b_host_port,))
        return self.bmemcached_ctl

    def __exit__(self, type, value, tb):
        self.bmemcached_ctl.disconnect_all()


def bmemcached_set(v):
    with BmemcachedCtl(v) as bmemcached_ctl:
        return common_set(bmemcached_ctl)


def bmemcached_set_multi(v):
    with BmemcachedCtl(v) as bmemcached_ctl:
        return common_set_multi(bmemcached_ctl)


def bmemcached_get(v):
    with BmemcachedCtl(v) as bmemcached_ctl:
        return common_get(bmemcached_ctl)


def bmemcached_get_multi(v):
    with BmemcachedCtl(v) as bmemcached_ctl:
        return common_get_multi(bmemcached_ctl)


def bmemcached_delete(v):
    with BmemcachedCtl(v) as bmemcached_ctl:
        return common_delete(bmemcached_ctl)


def bmemcached_delete_multi(v):
    if v in ["0.25.0"]:
        with BmemcachedCtl(v) as bmemcached_ctl:
            return common_delete_multi(bmemcached_ctl)
    return "binary memcached module has no attribute delete_multi"


def bmemcached_conn_default(v):
    with BmemcachedCtl(v) as bmemcached_ctl:
        return common_get(bmemcached_ctl)
