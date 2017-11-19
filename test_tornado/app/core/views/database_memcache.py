#!/usr/bin/env python
# -*- coding: utf-8 -*-
from core.views.base import BaseHandler
from public.db_memcache import db_binary_mamcached, db_mamcached, db_pymemcache


# python-memcached
class MemcacheSet(BaseHandler):
    def get(self):
        v = self.get_argument("v", "1.58.0")
        self.write(db_mamcached.memcache_set(v))


class MemcacheSetMulti(BaseHandler):
    def get(self):
        v = self.get_argument("v", "1.58.0")
        self.write(db_mamcached.memcache_set_multi(v))


class MemcacheGet(BaseHandler):
    def get(self):
        v = self.get_argument("v", "1.58.0")
        self.write(db_mamcached.memcache_get(v))


class MemcacheGetMulti(BaseHandler):
    def get(self):
        v = self.get_argument("v", "1.58.0")
        self.write(db_mamcached.memcache_get_multi(v))


class MemcacheDelete(BaseHandler):
    def get(self):
        v = self.get_argument("v", "1.58.0")
        self.write(db_mamcached.memcache_delete(v))


class MemcacheDeleteMulti(BaseHandler):
    def get(self):
        v = self.get_argument("v", "1.58.0")
        self.write(db_mamcached.memcache_delete_multi(v))


class MemcacheConnDefault(BaseHandler):
    def get(self):
        v = self.get_argument("v", "1.58.0")
        self.write(db_mamcached.memcache_conn_default(v))


# pymemcache
class PymemcacheSetMulti(BaseHandler):
    def get(self):
        v = self.get_argument("v", "1.4.0")
        self.write(db_pymemcache.pymemcache_set_multi(v))


class PymemcacheGet(BaseHandler):
    def get(self):
        v = self.get_argument("v", "1.4.0")
        self.write(db_pymemcache.pymemcache_get(v))


class PymemcacheGetMulti(BaseHandler):
    def get(self):
        v = self.get_argument("v", "1.4.0")
        self.write(db_pymemcache.pymemcache_get_multi(v))


class PymemcacheDelete(BaseHandler):
    def get(self):
        v = self.get_argument("v", "1.4.0")
        self.write(db_pymemcache.pymemcache_delete(v))


class PymemcacheDeleteMulti(BaseHandler):
    def get(self):
        v = self.get_argument("v", "1.4.0")
        self.write(db_pymemcache.pymemcache_delete_multi(v))


class PymemcacheConnByClient(BaseHandler):
    def get(self):
        v = self.get_argument("v", "1.4.0")
        self.write(db_pymemcache.pymemcache_conn_by_client(v))


class PymemcacheConnByHashClient(BaseHandler):
    def get(self):
        v = self.get_argument("v", "1.4.0")
        self.write(db_pymemcache.pymemcache_conn_by_hashclient(v))


# bmemcached
class BMemcachedSet(BaseHandler):
    def get(self):
        v = self.get_argument("v", "0.25.0")
        self.write(db_binary_mamcached.bmemcached_set(v))


class BMemcachedSetMulti(BaseHandler):
    def get(self):
        v = self.get_argument("v", "0.25.0")
        self.write(db_binary_mamcached.bmemcached_set_multi(v))


class BMemcachedGet(BaseHandler):
    def get(self):
        v = self.get_argument("v", "0.25.0")
        self.write(db_binary_mamcached.bmemcached_get(v))


class BMemcachedGetMulti(BaseHandler):
    def get(self):
        v = self.get_argument("v", "0.25.0")
        self.write(db_binary_mamcached.bmemcached_get_multi(v))


class BMemcachedDelete(BaseHandler):
    def get(self):
        v = self.get_argument("v", "0.25.0")
        self.write(db_binary_mamcached.bmemcached_delete(v))


class BMemcachedDeleteMulti(BaseHandler):
    def get(self):
        v = self.get_argument("v", "0.25.0")
        self.write(db_binary_mamcached.bmemcached_delete_multi(v))


class BMemcachedConnDefault(BaseHandler):
    def get(self):
        v = self.get_argument("v", "0.25.0")
        self.write(db_binary_mamcached.bmemcached_conn_default(v))
