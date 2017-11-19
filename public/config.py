#!/usr/bin/env python
# -*- coding: utf-8 -*-


ORACLE_CONF = {
    'host': 'oracle.db.com',
    'port': 1521,
    'xe': 'nbsdb',
    'name': 'test',
    'pwd': 'test',
    'sid': 'nbsdb'
}

MYSQL_CONF = {
    'host': 'mysql.db.com',
    'port': 3306,
    'name': 'tingyun',
    'pwd': 'tingyun',
    'db': 'xiguago',
}

SQL_SERVER_CONF = {
    'host': 'sqlserver.db.com',
    'port': 1433,
    'name': 'leng',
    'pwd': 'Windows2008',
    'db': 'python_test',
    'tds_version': 7.0
}

MONGODB_CONF = {
    'host': 'mongodb.db.com',
    'port': 27017,
    'db': 'test'
}

MEMCACHE_CONF = {
    'host': 'memcache.db.com',
    'port': 11211
}

REDIS_CONF = {
    'host': 'redis.db.com',
    'port': 6379,
}

THRIFT_CONF = {
    'host': 'thrift.external.com',
    'port': 9090
}

PG_CONF = {
    'host': 'postgresql.db.com',
    'port': '5432',
    'user': 'tingyun',
    'password': 'tingyun',
    'database': 'xiguago',
    'minconn': 1,
    'maxconn': 4,
}


URL = 'http://127.0.0.1:5561/external/normal/a'
URL_ = 'http://www.example.com'
EX_URL = 'http://127.0.0.1:10001/normal/a'
# NO_AGENT_URL = 'http://127.0.0.1:5562/normal/a'
SELF_URL = 'http://127.0.0.1:5587/slow/action/a?timer=2500'

URLS = {
    'java': 'http://192.168.5.140:8080/jdk1.6_AgentTest_External_01/',
    'dotnet': 'http://192.168.5.226:8011/',
    'nodejs': 'http://192.168.3.15',
    'php': 'http://192.168.2.106/ob.php',
    'ruby': 'http://192.168.2.152:4000/tst'
}

DATA = FIELDS = {'key': 'value'}
TIME_OUT = 0.000001
CROSS_APP_TRACE_URL = "http://wiki.http.com"
BODY = "it`s body"

RBT_HOST = 'rabbitmq.message.com'
DEFAULT_PIKA_VERSION = '0.10.0'

