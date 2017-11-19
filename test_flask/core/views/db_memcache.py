#!/usr/bin/env python
# -*- coding: utf-8 -*-


from flask import Blueprint, request
from public.db_memcache import db_binary_mamcached, db_mamcached, db_pymemcache


db_memcache_blueprint = Blueprint(__name__, __name__)


# python-memcached
@db_memcache_blueprint.route("/db/memcache/memcache-set/")
def memcache_set():
    v = request.args.get("v", "1.58.0")
    return db_mamcached.memcache_set(v)


@db_memcache_blueprint.route("/db/memcache/memcache-set-multi/")
def memcache_set_multi():
    v = request.args.get("v", "1.58.0")
    return db_mamcached.memcache_set_multi(v)


@db_memcache_blueprint.route("/db/memcache/memcache-get/")
def memcache_get():
    v = request.args.get("v", "1.58.0")
    return db_mamcached.memcache_get(v)


@db_memcache_blueprint.route("/db/memcache/memcache-get-multi/")
def memcache_get_multi():
    v = request.args.get("v", "1.58.0")
    return db_mamcached.memcache_get_multi(v)


@db_memcache_blueprint.route("/db/memcache/memcache-delete/")
def memcache_delete():
    v = request.args.get("v", "1.58.0")
    return db_mamcached.memcache_delete(v)


@db_memcache_blueprint.route("/db/memcache/memcache-delete-multi/")
def memcache_delete_multi():
    v = request.args.get("v", "1.58.0")
    return db_mamcached.memcache_delete_multi(v)


@db_memcache_blueprint.route("/db/memcache/conn/default/")
def memcache_conn_default():
    v = request.args.get("v", "1.58.0")
    return db_mamcached.memcache_conn_default(v)


# pymemcache
@db_memcache_blueprint.route("/db/memcache/pymemcache-set-multi/")
def pymemcache_set_multi():
    v = request.args.get("v", "1.4.0")
    return db_pymemcache.pymemcache_set_multi(v)


@db_memcache_blueprint.route("/db/memcache/pymemcache-get/")
def pymemcache_get():
    v = request.args.get("v", "1.4.0")
    return db_pymemcache.pymemcache_get(v)


@db_memcache_blueprint.route("/db/memcache/pymemcache-get-multi/")
def pymemcache_get_multi():
    v = request.args.get("v", "1.4.0")
    return db_pymemcache.pymemcache_get_multi(v)


@db_memcache_blueprint.route("/db/memcache/pymemcache-delete/")
def pymemcache_delete():
    v = request.args.get("v", "1.4.0")
    return db_pymemcache.pymemcache_delete(v)


@db_memcache_blueprint.route("/db/memcache/pymemcache-delete-multi/")
def pymemcache_delete_multi():
    v = request.args.get("v", "1.4.0")
    return db_pymemcache.pymemcache_delete_multi(v)


@db_memcache_blueprint.route("/db/memcache/pymemcache/conn/client/")
def pymemcache_conn_by_client():
    v = request.args.get("v", "1.4.0")
    return db_pymemcache.pymemcache_conn_by_client(v)


@db_memcache_blueprint.route("/db/memcache/pymemcache/conn/hashclient/")
def pymemcache_conn_by_hashclient():
    v = request.args.get("v", "1.4.0")
    return db_pymemcache.pymemcache_conn_by_hashclient(v)


# bmemcached
@db_memcache_blueprint.route("/db/memcache/bmemcached-set/")
def bmemcached_set():
    v = request.args.get("v", "0.25.0")
    return db_binary_mamcached.bmemcached_set(v)


@db_memcache_blueprint.route("/db/memcache/bmemcached-set-multi/")
def bmemcached_set_multi():
    v = request.args.get("v", "0.25.0")
    return db_binary_mamcached.bmemcached_set_multi(v)


@db_memcache_blueprint.route("/db/memcache/bmemcached-get/")
def bmemcached_get():
    v = request.args.get("v", "0.25.0")
    return db_binary_mamcached.bmemcached_get(v)


@db_memcache_blueprint.route("/db/memcache/bmemcached-get-multi/")
def bmemcached_get_multi():
    v = request.args.get("v", "0.25.0")
    return db_binary_mamcached.bmemcached_get_multi(v)


@db_memcache_blueprint.route("/db/memcache/bmemcached-delete/")
def bmemcached_delete():
    v = request.args.get("v", "0.25.0")
    return db_binary_mamcached.bmemcached_delete(v)


@db_memcache_blueprint.route("/db/memcache/bmemcached-delete-multi/")
def bmemcached_delete_multi():
    v = request.args.get("v", "0.25.0")
    return db_binary_mamcached.bmemcached_delete_multi(v)


@db_memcache_blueprint.route("/db/memcache/bmemcached/conn/default/")
def bmemcached_conn_default():
    v = request.args.get("v", "0.25.0")
    return db_binary_mamcached.bmemcached_conn_default(v)
