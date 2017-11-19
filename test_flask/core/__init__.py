# -*- coding: utf-8 -*-


ALL_URI = {

    "dc_config_test": [
        "/normal/a",  # 'a' 作为参数，可替换任意字母，区分URI
        "/normal/with/sql",
        "/slow/action/with/sql",
        "/slow/action/a?timer=2000",  # 'a' 作为参数，可替换任意字母，区分URI; 'timer'作为参数传入，控制网页响应时间，单位：ms
        "/error/a?code=404",  # 'a' 作为参数，可甜任意字母，区分URI；'code'; 'code'作为参数传入，控制网页响应状态
        "/stack?num=3&timer=500",  # 'num'作为参数传入，控制sleep次数； 'timer'作为参数传入，控制一次sleep的时长，单位：ms
    ],

    "frame_flask_test": [
        "/add_url_rule",  #  flask的add_url_rule方法
        "/blueprint/error/a?code=404",   # 'a' 作为参数，可替换任意字母，区分URI；'code'; 'code'作为参数传入，控制网页响应状态
    ],

    "db_mysql": [
        "/db/mysql/mysqldb-position-connect/",
        "/db/mysql/mysqldb-keyword-connect/",
        "/db/mysql/mysqldb-pool-connect/",
        "/db/mysql/mysqldb-insert/",
        "/db/mysql/mysqldb-delete/",
        "/db/mysql/mysqldb-update/",
        "/db/mysql/mysqldb-select/?count=3",  # 'count'作为参数传入，控制页面中sql执行次数
        "/db/mysql/mysqldb-fetch-one/",
        "/db/mysql/mysqldb-fetch-many/",
        "/db/mysql/mysqldb-fetch-all/",
        "/db/mysql/mysqldb-execute-many/",
        "/db/mysql/mysqldb-table-error/",
        "/db/mysql/mysqldb-field-error/",
        "/db/mysql/mysqldb-syntax-error/",

        "/db/mysql/pymysql-no-port-connect/",
        "/db/mysql/pymysql-dict-connect/",
        "/db/mysql/pymysql-position-connect/",
        "/db/mysql/pymysql-keyword-connect/",
        "/db/mysql/pymysql-insert/",
        "/db/mysql/pymysql-delete/",
        "/db/mysql/pymysql-update/",
        "/db/mysql/pymysql-select/",
        "/db/mysql/pymysql-table-error/",
        "/db/mysql/pymysql-field-error/",
        "/db/mysql/pymysql-syntax-error/",
        "/db/mysql/pymysql-fetch-one/",
        "/db/mysql/pymysql-fetch-many/",
        "/db/mysql/pymysql-fetch-all/",
        "/db/mysql/pymysql-execute-many/",

        "/db/mysql/oursql-keyword-connect/",
        "/db/mysql/oursql-position-connect/",
        "/db/mysql/oursql-no-port-connect/",
        "/db/mysql/oursql-insert/",
        "/db/mysql/oursql-delete/",
        "/db/mysql/oursql-update/",
        "/db/mysql/oursql-select/",
        "/db/mysql/oursql-fetch-one/",
        "/db/mysql/oursql-fetch-many/",
        "/db/mysql/oursql-fetch-all/",
    ],

    "db_oracle": [
        "/db/oracle/position-conn/",
        "/db/oracle/connecting-conn/",
        "/db/oracle/makedsn-conn/",
        "/db/oracle/insert/",
        "/db/oracle/delete/",
        "/db/oracle/update/",
        "/db/oracle/select/?count=4",  # 'count'作为参数传入，控制页面中sql执行次数
        "/db/oracle/fetch-one/",
        "/db/oracle/fetch-many/",
        "/db/oracle/fetch-all/",
        "/db/oracle/execute-many/",
        "/db/oracle/table-error/",
        "/db/oracle/field-error/",
        "/db/oracle/syntax-error/",
    ],

    "db_psycopg2": [
        "/db/postgresql/psycopg2-keyword-database-connect/",
        "/db/postgresql/psycopg2-uri-connect/",
        "/db/postgresql/psycopg2-uri-no-port-connect/",
        "/db/postgresql/psycopg2-connectstring-no-port-connect/",
        "/db/postgresql/psycopg2-connectstring-connect/",
        "/db/postgresql/psycopg2-keyword-dbname-connect/",
        "/db/postgresql/psycopg2-no-port-connect/",
        "/db/postgresql/psycopg2-insert/",
        "/db/postgresql/psycopg2-update/",
        "/db/postgresql/psycopg2-select/",
        "/db/postgresql/psycopg2-delete/",
        "/db/postgresql/psycopg2-connection-pool/",
        "/db/postgresql/psycopg2-table-error/",
        "/db/postgresql/psycopg2-field-error/",
        "/db/postgresql/psycopg2-syntax-error/"
    ],

    "db_psycopg2cffi": [
        "/db/postgresql/psycopg2cffi-keyword-database-connect/",
        "/db/postgresql/psycopg2cffi-uri-connect/",
        "/db/postgresql/psycopg2cffi-uri-no-port-connect/",
        "/db/postgresql/psycopc2ffig-connectstring-no-port-connect/",
        "/db/postgresql/psycopg2cffi-connectstring-connect/",
        "/db/postgresql/psycopg2cffi-keyword-dbname-connect/",
        "/db/postgresql/psycopg2cffi-no-port-connect/",
        "/db/postgresql/psycopg2cffi-insert/",
        "/db/postgresql/psycopg2cffi-update/",
        "/db/postgresql/psycopg2cffi-select/",
        "/db/postgresql/psycopg2cffi-delete/",
        "/db/postgresql/psycopg2cffi-connection-pool/",
        "/db/postgresql/psycopg2cffi-table-error/",
        "/db/postgresql/psycopg2cffi-field-error/",
        "/db/postgresql/psycopg2cffi-syntax-error/"
    ],

    "db_psycopg2ct": [
        "/db/postgresql/psycopg2ct-keyword-database-connect/",
        "/db/postgresql/psycopg2ct-uri-connect/",
        "/db/postgresql/psycopg2ct-uri-no-port-connect/",
        "/db/postgresql/psycopc2ct-connectstring-no-port-connect/",
        "/db/postgresql/psycopg2ct-connectstring-connect/",
        "/db/postgresql/psycopg2ct-keyword-dbname-connect/",
        "/db/postgresql/psycopg2ct-no-port-connect/",
        "/db/postgresql/psycopg2ct-insert/",
        "/db/postgresql/psycopg2ct-update/",
        "/db/postgresql/psycopg2ct-select/",
        "/db/postgresql/psycopg2ct-delete/",
        "/db/postgresql/psycopg2ct-connection-pool/",
        "/db/postgresql/psycopg2ct-table-error/",
        "/db/postgresql/psycopg2ct-field-error/",
        "/db/postgresql/psycopg2ct-syntax-error/"
    ],

    "db_sqlserver": [
        "/db/sqlserver/keyword-connect/",
        "/db/sqlserver/server-connect/",
        "/db/sqlserver/insert/",
        "/db/sqlserver/delete/",
        "/db/sqlserver/update/",
        "/db/sqlserver/select/",
        "/db/sqlserver/fetch-one/",
        "/db/sqlserver/fetch-many/",
        "/db/sqlserver/fetch-all/",
        "/db/sqlserver/execute-many/",
        "/db/sqlserver/table-error/",
        "/db/sqlserver/field-error/",
        "/db/sqlserver/syntax-error/"
    ],

    # "ver"作为参数传入，控制mongodb驱动版本， 默认为3.4.0
    # vers = [2.0, 2.1, 2.2, 2.3, 2.4, 2.5, 2.6, 2.7, 2.8, 2.9, 3.0, 3.1, 3.2, 3.3, 3.4.0]
    "db_mongodb": [
        "/db/mongodb/insert/?ver=3.4.0",
        "/db/mongodb/delete/?ver=3.4.0",
        "/db/mongodb/update/?ver=3.4.0",
        "/db/mongodb/select/?ver=3.4.0",
        "/db/mongodb/conn/connection/?ver=3.4.0",
        "/db/mongodb/conn/mongoclient/params/?ver=3.4.0"
        "/db/mongodb/conn/mongoclient/str/?ver=3.4.0"
    ],

    # "v"作为参数传入，控制redis驱动版本，默认为2.10.5
    # vs = [2.6.0, 2.7.0, 2.8.0, 2.9.0, 2.10.5]
    "db_redis": [
        "/db/redis/set/v=2.10.5",
        "/db/redis/get/v=2.10.5",
        "/db/redis/hset/v=2.10.5",
        "/db/redis/hget/v=2.10.5",
        "/db/redis/hgetall/v=2.10.5",
        "/db/redis/rpush/v=2.10.5",
        "/db/redis/lpop/v=2.10.5",
        "/db/redis/lrange/v=2.10.5",
        "/db/redis/sadd/v=2.10.5",
        "/db/redis/srem/v=2.10.5",
        "/db/redis/smembers/v=2.10.5",
        "/db/redis/zadd/v=2.10.5",
        "/db/redis/zrange/v=2.10.5",
        "/db/redis/conn/default/v=2.10.5",
        "/db/redis/conn/strictredis/v=2.10.5",
        "/db/redis/conn/pool/v=2.10.5"
    ],

    # "v"作为参数传入，控制memcached、pymemcache、python-binary-memcached驱动版本，默认分别为1.58.0、1.4.0、0.25.0
    # memcached: vs = [1.58.0, 1.47.0]
    # pymemcache: vs = [1.4.0, 1.3.0, 1.2.0]
    # python-binary-memcached: vs = [0.20.0, 0.21.0, 0.22.0, 0.23.0, 0.24.0, 0.25.0]
    "db_memcache": [
        "/db/memcache/memcache-set/v=1.58.0",
        "/db/memcache/memcache-set-multi/v=1.58.0",
        "/db/memcache/memcache-get/v=1.58.0",
        "/db/memcache/memcache-get-multi/v=1.58.0",
        "/db/memcache/memcache-delete/v=1.58.0",
        "/db/memcache/memcache-delete-multi/v=1.58.0",
        "/db/memcache/conn/default/v=1.58.0",

        "/db/memcache/pymemcache-set-multi/v=1.4.0",
        "/db/memcache/pymemcache-get/v=1.4.0",
        "/db/memcache/pymemcache-get-multi/v=1.4.0",
        "/db/memcache/pymemcache-delete/v=1.4.0",
        "/db/memcache/pymemcache-delete-multi/v=1.4.0",
        "/db/memcache/pymemcache/conn/client/v=1.4.0",
        "/db/memcache/pymemcache/conn/hashclient/v=1.4.0",

        "/db/memcache/bmemcached-set/v=0.25.0",
        "/db/memcache/bmemcached-set-multi/v=0.25.0",
        "/db/memcache/bmemcached-get/v=0.25.0",
        "/db/memcache/bmemcached-get-multi/v=0.25.0",
        "/db/memcache/bmemcached-delete/v=0.25.0",
        "/db/memcache/bmemcached-delete-multi/v=0.25.0",
        "/db/memcache/bmemcached/conn/default/v=0.25.0"
    ],

    "ex_urllib": [
        "/urllib/get",
        "/urllib/urlencode",
        "/urllib/post"
    ],

    "ex_urllib2": [
        "/urllib2/get",
        "/urllib2/post",
        "/urllib2/cookie"
    ],

    "ex_urllib3": [
        "/urllib3/poolmanager/get",
        "/urllib3/poolmanager/post",
        "/urllib3/timeout_error",
        "/urllib3/timeout_ok"
    ],

    "ex_requests": [
        "/requests/api",
        "/requests/session",
        "/requests/timeout_error",
        "/requests/timeout_ok"
    ],

    "ex_httplib2": [
        "/httplib2/http",
        "/httplib2/http_timeout_error",
        "/httplib2/http_timeout_ok",
        "/httplib2/https_timeout_ok",
        "/httplib2/https_timeout_error",
    ],

    "ex_thrift": [
        "/ex/thrift/"
    ],

    "ex_network": [
        "/requests/error/InvalidURL",
        "/requests/error/URLRequired",
        "/requests/error/ConnectTimeout",
        "/requests/error/ConnectionError",
        "/requests/error/SSLError",
        "/requests/error/ReadTimeout",
        "/requests/error/InvalidSchema",
        "/requests/error/MissingSchema",
        "/requests/error/ChunkedEncodingError",
        "/requests/error/ContentDecodingError",
        "/requests/error/StreamConsumedError",
        "/requests/error/TooManyRedirects",
        "/requests/error/RequestException",
        "/requests/error/HTTPError",
    ]

}
