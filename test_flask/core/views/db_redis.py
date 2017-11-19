#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Blueprint, request
from public.db_redis import db_redis


db_redis_blueprint = Blueprint(__name__, __name__)


@db_redis_blueprint.route("/db/redis/set/")
def redis_set():
    v = request.args.get("v", "2.10.5")
    return db_redis.redis_set(v)


@db_redis_blueprint.route("/db/redis/get/")
def redis_get():
    v = request.args.get("v", "2.10.5")
    return db_redis.redis_get(v)


@db_redis_blueprint.route("/db/redis/hset/")
def redis_hset():
    v = request.args.get("v", "2.10.5")
    return db_redis.redis_hset(v)


@db_redis_blueprint.route("/db/redis/hget/")
def redis_hget():
    v = request.args.get("v", "2.10.5")
    return db_redis.redis_hget(v)


@db_redis_blueprint.route("/db/redis/hgetall/")
def redis_hgetall():
    v = request.args.get("v", "2.10.5")
    return db_redis.redis_hgetall(v)


@db_redis_blueprint.route("/db/redis/rpush/")
def redis_rpush():
    v = request.args.get("v", "2.10.5")
    return db_redis.redis_rpush(v)


@db_redis_blueprint.route("/db/redis/lpop/")
def redis_lpop():
    v = request.args.get("v", "2.10.5")
    return db_redis.redis_lpop(v)


@db_redis_blueprint.route("/db/redis/lrange/")
def redis_lrange():
    v = request.args.get("v", "2.10.5")
    return db_redis.redis_lrange(v)


@db_redis_blueprint.route("/db/redis/sadd/")
def redis_sadd():
    v = request.args.get("v", "2.10.5")
    return db_redis.redis_sadd(v)


@db_redis_blueprint.route("/db/redis/srem/")
def redis_srem():
    v = request.args.get("v", "2.10.5")
    return db_redis.redis_srem(v)


@db_redis_blueprint.route("/db/redis/smembers/")
def redis_smembers():
    v = request.args.get("v", "2.10.5")
    return db_redis.redis_smembers(v)


@db_redis_blueprint.route("/db/redis/zadd/")
def redis_zadd():
    v = request.args.get("v", "2.10.5")
    return db_redis.redis_zadd(v)


@db_redis_blueprint.route("/db/redis/zrange/")
def redis_zrange():
    v = request.args.get("v", "2.10.5")
    return db_redis.redis_zrange(v)


@db_redis_blueprint.route("/db/redis/conn/default/")
def redis_conn_by_redis():
    v = request.args.get("v", "2.10.5")
    return db_redis.redis_conn_by_redis(v)


@db_redis_blueprint.route("/db/redis/conn/strictredis/")
def redis_conn_by_strictredis():
    v = request.args.get("v", "2.10.5")
    return db_redis.redis_conn_by_strictredis(v)


@db_redis_blueprint.route("/db/redis/conn/pool/")
def redis_conn_pool():
    v = request.args.get("v", "2.10.5")
    return db_redis.redis_conn_pool(v)
