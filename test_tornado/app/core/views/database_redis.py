#!/usr/bin/env python
# -*- coding: utf-8 -*-
from core.views.base import BaseHandler
from public.db_redis import db_redis


class RedisSet(BaseHandler):
    def get(self):
        v = self.get_argument("v", "2.10.5")
        self.write(db_redis.redis_set(v))


class RedisGet(BaseHandler):
    def get(self):
        v = self.get_argument("v", "2.10.5")
        self.write(db_redis.redis_get(v))


class RedisHSet(BaseHandler):
    def get(self):
        v = self.get_argument("v", "2.10.5")
        self.write(db_redis.redis_hset(v))


class RedisHGet(BaseHandler):
    def get(self):
        v = self.get_argument("v", "2.10.5")
        self.write(db_redis.redis_hget(v))


class RedisHGetAll(BaseHandler):
    def get(self):
        v = self.get_argument("v", "2.10.5")
        self.write(db_redis.redis_hgetall(v))


class RedisRPush(BaseHandler):
    def get(self):
        v = self.get_argument("v", "2.10.5")
        self.write(db_redis.redis_rpush(v))


class RedisLPop(BaseHandler):
    def get(self):
        v = self.get_argument("v", "2.10.5")
        self.write(db_redis.redis_lpop(v))


class RedisLRange(BaseHandler):
    def get(self):
        v = self.get_argument("v", "2.10.5")
        self.write(db_redis.redis_lrange(v))


class RedisSAdd(BaseHandler):
    def get(self):
        v = self.get_argument("v", "2.10.5")
        self.write(db_redis.redis_sadd(v))


class RedisSRem(BaseHandler):
    def get(self):
        v = self.get_argument("v", "2.10.5")
        self.write(db_redis.redis_srem(v))


class RedisSMembers(BaseHandler):
    def get(self):
        v = self.get_argument("v", "2.10.5")
        self.write(db_redis.redis_smembers(v))


class RedisZAdd(BaseHandler):
    def get(self):
        v = self.get_argument("v", "2.10.5")
        self.write(db_redis.redis_zadd(v))


class RedisZRange(BaseHandler):
    def get(self):
        v = self.get_argument("v", "2.10.5")
        self.write(db_redis.redis_zrange(v))


class RedisConnByRedis(BaseHandler):
    def get(self):
        v = self.get_argument("v", "2.10.5")
        self.write(db_redis.redis_conn_by_redis(v))


class RedisConnByStrictredis(BaseHandler):
    def get(self):
        v = self.get_argument("v", "2.10.5")
        self.write(db_redis.redis_conn_by_strictredis(v))


class RedisConnPool(BaseHandler):
    def get(self):
        v = self.get_argument("v", "2.10.5")
        self.write(db_redis.redis_conn_pool(v))
