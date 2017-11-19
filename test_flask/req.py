# !/usr/bin/python
# -*- coding: utf-8 -*-
import time
import logging
import requests


pymongo_versions = ["2.0", "2.1", "2.2", "2.3", "2.4", "2.5", "2.6", "2.7", "2.8", "2.9", "3.0", "3.1", "3.2", "3.3", "3.4"]
python_memcached_versions = ["1.47.0", "1.58.0"]
pymemcache_versions = ["1.2.0", "1.3.0", "1.4.0"]
bmemcached_versions = ["0.20.0", "0.21.0", "0.22.0", "0.23.0", "0.24.0", "0.25.0"]
redis_versions = ["2.6.0", "2.7.0", "2.8.0", "2.9.0", "2.10.5"]


pymongo_uri = [
    "/db/mongodb/insert/",
    "/db/mongodb/delete/",
    "/db/mongodb/update/",
    "/db/mongodb/select/",
    "/db/mongodb/conn/connection/",
    "/db/mongodb/conn/mongoclient/params/",
    "/db/mongodb/conn/mongoclient/str/"
]


python_memcached_uri = [
    "/db/memcache/memcache-set/",
    "/db/memcache/memcache-set-multi/",
    "/db/memcache/memcache-get/",
    "/db/memcache/memcache-get-multi/",
    "/db/memcache/memcache-delete/",
    "/db/memcache/memcache-delete-multi/",
    "/db/memcache/conn/default/"
]


pymemcache_uri = [
    "/db/memcache/pymemcache-set-multi/",
    "/db/memcache/pymemcache-get/",
    "/db/memcache/pymemcache-get-multi/",
    "/db/memcache/pymemcache-delete/",
    "/db/memcache/pymemcache-delete-multi/",
    "/db/memcache/pymemcache/conn/client/",
    "/db/memcache/pymemcache/conn/hashclient/"
]


bmemcached_uri = [
    "/db/memcache/bmemcached-set/",
    "/db/memcache/bmemcached-set-multi/",
    "/db/memcache/bmemcached-get/",
    "/db/memcache/bmemcached-get-multi/",
    "/db/memcache/bmemcached-delete/",
    "/db/memcache/bmemcached-delete-multi/",
    "/db/memcache/bmemcached/conn/default/"
]


redis_uri = [
    "/db/redis/set/",
    "/db/redis/get/",
    "/db/redis/hset/",
    "/db/redis/hget/",
    "/db/redis/hgetall/",
    "/db/redis/rpush/",
    "/db/redis/lpop/",
    "/db/redis/lrange/",
    "/db/redis/sadd/",
    "/db/redis/srem/",
    "/db/redis/smembers/",
    "/db/redis/zadd/",
    "/db/redis/zrange/",
    "/db/redis/conn/default/",
    "/db/redis/conn/strictredis/",
    "/db/redis/conn/pool/"
]


def req_pymango(host):
    for v in pymongo_versions:
        for uri in pymongo_uri:
            do_req(host, uri, v, m="pymongo")


def req_python_memcached(host):
    for v in python_memcached_versions:
        for uri in python_memcached_uri:
            do_req(host, uri, v)


def req_pymemcache(host):
    for v in pymemcache_versions:
        for uri in pymemcache_uri:
            do_req(host, uri, v)


def req_bmemcached(host):
    for v in bmemcached_versions:
        for uri in bmemcached_uri:
            do_req(host, uri, v)


def req_redis(host):
    for v in redis_versions:
        for uri in redis_uri:
            do_req(host, uri, v)


def do_req(host, uri, v, m=None):
    time.sleep(1)
    if m is None:
        url = "{host}/{uri}?v={v}".format(host=host.strip("/"), uri=uri.lstrip("/"), v=v)
    elif m == "pymongo":
        url = "{host}/{uri}?ver={v}".format(host=host.strip("/"), uri=uri.lstrip("/"), v=v)

    try:
        res = requests.get(url)
        logging.info("req {url} resp code: {resp_code}".format(url=url, resp_code=res.status_code))
    except Exception as e:
        logging.error("req {url} error: {err}".format(url=url, err=e))


if __name__ == "__main__":
    host = "http://127.0.0.1:5562"
    while 1:
        req_pymango(host)
        req_python_memcached(host)
        req_pymemcache(host)
        req_bmemcached(host)
        req_redis(host)
        time.sleep(30)
