#!/usr/bin/env python
# -*- coding: utf-8 -*-
# from flask import Blueprint

from public.db_util import common_set, common_get, common_hset, common_hget, common_hgetall,\
        common_rpush, common_lpop, common_lrange, common_sadd, common_srem, common_smembers, \
        common_zadd, common_zrange
from ..config import REDIS_CONF


# db_redis_blueprint = Blueprint(__name__, __name__)


class RedisCtl():
    def __init__(self, v):
        self.v = v

    def __enter__(self):
        if self.v == "2.6.0":
            from public.packages.redis.v260 import redis
        elif self.v == "2.7.0":
            from public.packages.redis.v270 import redis
        elif self.v == "2.8.0":
            from public.packages.redis.v280 import redis
        elif self.v == "2.9.0":
            from public.packages.redis.v290 import redis
        elif self.v == "2.10.5":
            from public.packages.redis.v2105 import redis

        self.conn1 = redis.Redis(host=REDIS_CONF['host'], port=REDIS_CONF['port'], db=15)
        self.conn2 =  redis.StrictRedis(host=REDIS_CONF['host'], port=REDIS_CONF['port'], db=15)
        pool = redis.ConnectionPool(host=REDIS_CONF['host'], port=REDIS_CONF['port'], db=15)
        self.conn3 = redis_ctl = redis.Redis(connection_pool=pool)
        return self.conn1, self.conn2, self.conn3

    def __exit__(self, type, value, tb):
        del self.conn1
        del self.conn2
        del self.conn3


def redis_set(v):
    with RedisCtl(v) as redis_ctl:
        common_set(redis_ctl[0])
        return "success"


def redis_get(v):
    with RedisCtl(v) as redis_ctl:
        return common_get(redis_ctl[0])


def redis_hset(v):
    with RedisCtl(v) as redis_ctl:
        common_hset(redis_ctl[0])
        return "success"


def redis_hget(v):
    with RedisCtl(v) as redis_ctl:
        return common_hget(redis_ctl[0])


def redis_hgetall(v):
    with RedisCtl(v) as redis_ctl:
        return common_hgetall(redis_ctl[0])


def redis_rpush(v):
    with RedisCtl(v) as redis_ctl:
        return common_rpush(redis_ctl[0])


def redis_lpop(v):
    with RedisCtl(v) as redis_ctl:
        return common_lpop(redis_ctl[0])


def redis_lrange(v):
    with RedisCtl(v) as redis_ctl:
        return common_lrange(redis_ctl[0])


def redis_sadd(v):
    with RedisCtl(v) as redis_ctl:
        return common_sadd(redis_ctl[0])


def redis_srem(v):
    with RedisCtl(v) as redis_ctl:
        return common_srem(redis_ctl[0])


def redis_smembers(v):
    with RedisCtl(v) as redis_ctl:
        return common_smembers(redis_ctl[0])


def redis_zadd(v):
    with RedisCtl(v) as redis_ctl:
        return common_zadd(redis_ctl[0])


def redis_zrange(v):
    with RedisCtl(v) as redis_ctl:
        return common_zrange(redis_ctl[0])


def redis_conn_by_redis(v):
    with RedisCtl(v) as redis_ctl:
        return common_hget(redis_ctl[0])


def redis_conn_by_strictredis(v):
    with RedisCtl(v) as redis_ctl:
        return common_hget(redis_ctl[1])


def redis_conn_pool(v):
    with RedisCtl(v) as redis_ctl:
        return common_hget(redis_ctl[2])
