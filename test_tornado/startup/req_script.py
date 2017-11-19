#coding:utf-8
from gevent import monkey; monkey.patch_socket()
import gevent
import requests
import sys
import getopt
import time
import signal

import logging
logging.basicConfig(level=logging.INFO)

urls = [
    ("GET", "/initialize/"),
    ("GET", "/prepare/"),
    ("GET", "/request-method/"),
    ("POST", "/request-method/"),
    ("DELETE", "/request-method/"),
    ("PUT", "/request-method/"),
    ("HEAD", "/request-method/"),
    ("OPTIONS", "/request-method/"),
    ("PATCH", "/request-method/"),
    ("GET", "/render/"),
    ("GET", "/httpclient/"),
    ("GET", "/asynchttpclient/"),
    ("GET", "/coroutine/"),

    # # db oracle cx_Oracle 16
    # ('GET', '/db/oracle/position-conn/'),
    # ('GET', '/db/oracle/connecting-conn/'),
    # ('GET', '/db/oracle/makedsn-conn/'),
    # ('GET', '/db/oracle/insert/'),
    # ('GET', '/db/oracle/delete/'),
    # ('GET', '/db/oracle/update/'),
    # ('GET', '/db/oracle/select/'),
    # ('GET', '/db/oracle/fetch-one/'),
    # ('GET', '/db/oracle/fetch-many/'),
    # ('GET', '/db/oracle/fetch-all/'),
    # ('GET', '/db/oracle/execute-many/'),
    # ('GET', '/db/oracle/table-error/'),
    # ('GET', '/db/oracle/field-error/'),
    # ('GET', '/db/oracle/syntax-error/'),
    # ('GET', '/db/oracle/operates/'),
    # ('GET', '/db/oracle/connections/'),

    # db mysql mysqldb 16
    ('GET', '/db/mysql/mysqldb-position-connect/'),
    ('GET', '/db/mysql/mysqldb-keyword-connect/'),
    ('GET', '/db/mysql/mysqldb-pool-connect/'),
    ('GET', '/db/mysql/mysqldb-insert/'),
    ('GET', '/db/mysql/mysqldb-delete/'),
    ('GET', '/db/mysql/mysqldb-update/'),
    ('GET', '/db/mysql/mysqldb-select/'),
    ('GET', '/db/mysql/mysqldb-fetch-one/'),
    ('GET', '/db/mysql/mysqldb-fetch-many/'),
    ('GET', '/db/mysql/mysqldb-fetch-all/'),
    ('GET', '/db/mysql/mysqldb-execute-many/'),
    ('GET', '/db/mysql/mysqldb-table-error/'),
    ('GET', '/db/mysql/mysqldb-field-error/'),
    ('GET', '/db/mysql/mysqldb-syntax-error/'),
    ('GET', '/db/mysql/mysqldb-operates/'),
    ('GET', '/db/mysql/mysqldb-connections/'),

    # db mysql pysqldb 17
    ('GET', '/db/mysql/pymysql-no-port-connect/'),
    ('GET', '/db/mysql/pymysql-dict-connect/'),
    ('GET', '/db/mysql/pymysql-position-connect/'),
    ('GET', '/db/mysql/pymysql-keyword-connect/'),
    ('GET', '/db/mysql/pymysql-insert/'),
    ('GET', '/db/mysql/pymysql-delete/'),
    ('GET', '/db/mysql/pymysql-update/'),
    ('GET', '/db/mysql/pymysql-select/'),
    ('GET', '/db/mysql/pymysql-fetch-one/'),
    ('GET', '/db/mysql/pymysql-fetch-many/'),
    ('GET', '/db/mysql/pymysql-fetch-all/'),
    ('GET', '/db/mysql/pymysql-execute-many/'),
    ('GET', '/db/mysql/pymysql-table-error/'),
    ('GET', '/db/mysql/pymysql-field-error/'),
    ('GET', '/db/mysql/pymysql-syntax-error/'),
    ('GET', '/db/mysql/pymysql-operates/'),
    ('GET', '/db/mysql/pymysql-connections/'),

    # db mysql oursql 12
    ('GET', '/db/mysql/oursql-keyword-connect/'),
    ('GET', '/db/mysql/oursql-position-connect/'),
    ('GET', '/db/mysql/oursql-no-port-connect/'),
    ('GET', '/db/mysql/oursql-insert/'),
    ('GET', '/db/mysql/oursql-delete/'),
    ('GET', '/db/mysql/oursql-update/'),
    ('GET', '/db/mysql/oursql-select/'),
    ('GET', '/db/mysql/oursql-fetch-one/'),
    ('GET', '/db/mysql/oursql-fetch-many/'),
    ('GET', '/db/mysql/oursql-fetch-all/'),
    ('GET', '/db/mysql/oursql-operates/'),
    ('GET', '/db/mysql/oursql-connections/'),

    # db mongodb pymongo 7
    ('GET', '/db/mongodb/insert/'),
    ('GET', '/db/mongodb/delete/'),
    ('GET', '/db/mongodb/update/'),
    ('GET', '/db/mongodb/select/'),
    ('GET', '/db/mongodb/conn/connection/'),
    ('GET', '/db/mongodb/conn/mongoclient/params/'),
    ('GET', '/db/mongodb/conn/mongoclient/str/'),

    # db postgresql psycopg2 20
    ('GET', '/db/postgresql/psycopg2-parameters-connect/'),
    ('GET', '/db/postgresql/psycopg2-keyword-database-connect/'),
    ('GET', '/db/postgresql/psycopg2-uri-connect/'),
    ('GET', '/db/postgresql/psycopg2-uri-no-port-connect/'),
    ('GET', '/db/postgresql/psycopg2-connectstring-no-port-connect/'),
    ('GET', '/db/postgresql/psycopg2-connectstring-connect/'),
    ('GET', '/db/postgresql/psycopg2-keyword-dbname-connect/'),
    ('GET', '/db/postgresql/psycopg2-no-port-connect/'),
    ('GET', '/db/postgresql/psycopg2-insert/'),
    ('GET', '/db/postgresql/psycopg2-update/'),
    ('GET', '/db/postgresql/psycopg2-select/'),
    ('GET', '/db/postgresql/psycopg2-delete/'),
    ('GET', '/db/postgresql/psycopg2-connection-pool/'),
    ('GET', '/db/postgresql/psycopg2-timeout-error/'),
    ('GET', '/db/postgresql/psycopg2-timeout-ok/'),
    ('GET', '/db/postgresql/psycopg2-table-error/'),
    ('GET', '/db/postgresql/psycopg2-field-error/'),
    ('GET', '/db/postgresql/psycopg2-syntax-error/'),
    ('GET', '/db/postgresql/psycopg2-operates/'),
    ('GET', '/db/postgresql/psycopg2-connections/'),

    # db postgresql psycopg2ct 18
    ('GET', '/db/postgresql/psycopg2ct-parameters-connect/'),
    ('GET', '/db/postgresql/psycopg2ct-keyword-database-connect/'),
    ('GET', '/db/postgresql/psycopg2ct-uri-connect/'),
    ('GET', '/db/postgresql/psycopg2ct-uri-no-port-connect/'),
    ('GET', '/db/postgresql/psycopg2ct-connectstring-no-port-connect/'),
    ('GET', '/db/postgresql/psycopg2ct-connectstring-connect/'),
    ('GET', '/db/postgresql/psycopg2ct-keyword-dbname-connect/'),
    ('GET', '/db/postgresql/psycopg2ct-no-port-connect/'),
    ('GET', '/db/postgresql/psycopg2ct-insert/'),
    ('GET', '/db/postgresql/psycopg2ct-update/'),
    ('GET', '/db/postgresql/psycopg2ct-select/'),
    ('GET', '/db/postgresql/psycopg2ct-delete/'),
    ('GET', '/db/postgresql/psycopg2ct-connection-pool/'),
    ('GET', '/db/postgresql/psycopg2ct-timeout-error/'),
    ('GET', '/db/postgresql/psycopg2ct-timeout-ok/'),
    ('GET', '/db/postgresql/psycopg2ct-table-error/'),
    ('GET', '/db/postgresql/psycopg2ct-field-error/'),
    ('GET', '/db/postgresql/psycopg2ct-syntax-error/'),

    # db postgresql psycopg2cffi 16
    ('GET', '/db/postgresql/psycopg2cffi-parameters-connect/'),
    ('GET', '/db/postgresql/psycopg2cffi-keyword-database-connect/'),
    ('GET', '/db/postgresql/psycopg2cffi-uri-connect/'),
    ('GET', '/db/postgresql/psycopg2cffi-uri-no-port-connect/'),
    ('GET', '/db/postgresql/psycopg2cffi-connectstring-no-port-connect/'),
    ('GET', '/db/postgresql/psycopg2cffi-connectstring-connect/'),
    ('GET', '/db/postgresql/psycopg2cffi-keyword-dbname-connect/'),
    ('GET', '/db/postgresql/psycopg2cffi-no-port-connect/'),
    ('GET', '/db/postgresql/psycopg2cffi-insert/'),
    ('GET', '/db/postgresql/psycopg2cffi-update/'),
    ('GET', '/db/postgresql/psycopg2cffi-select/'),
    ('GET', '/db/postgresql/psycopg2cffi-delete/'),
    ('GET', '/db/postgresql/psycopg2cffi-connection-pool/'),
    ('GET', '/db/postgresql/psycopg2cffi-table-error/'),
    ('GET', '/db/postgresql/psycopg2cffi-field-error/'),
    ('GET', '/db/postgresql/psycopg2cffi-syntax-error/'),

    # db redis 16
    ('GET', '/db/redis/set/'),
    ('GET', '/db/redis/get/'),
    ('GET', '/db/redis/hset/'),
    ('GET', '/db/redis/hget/'),
    ('GET', '/db/redis/hgetall/'),
    ('GET', '/db/redis/rpush/'),
    ('GET', '/db/redis/lpop/'),
    ('GET', '/db/redis/lrange/'),
    ('GET', '/db/redis/sadd/'),
    ('GET', '/db/redis/srem/'),
    ('GET', '/db/redis/smembers/'),
    ('GET', '/db/redis/zadd/'),
    ('GET', '/db/redis/zrange/'),
    ('GET', '/db/redis/conn/default/'),
    ('GET', '/db/redis/conn/strictredis/'),
    ('GET', '/db/redis/conn/pool/'),

    # db memcached 21
    ('GET', '/db/memcache/memcache-set/'),
    ('GET', '/db/memcache/memcache-set-multi/'),
    ('GET', '/db/memcache/memcache-get/'),
    ('GET', '/db/memcache/memcache-get-multi/'),
    ('GET', '/db/memcache/memcache-delete/'),
    ('GET', '/db/memcache/memcache-delete-multi/'),
    ('GET', '/db/memcache/conn/default/'),

    ('GET', '/db/memcache/pymemcache-set-multi/'),
    ('GET', '/db/memcache/pymemcache-get/'),
    ('GET', '/db/memcache/pymemcache-get-multi/'),
    ('GET', '/db/memcache/pymemcache-delete/'),
    ('GET', '/db/memcache/pymemcache-delete-multi/'),
    ('GET', '/db/memcache/pymemcache/conn/client/'),
    ('GET', '/db/memcache/pymemcache/conn/hashclient/'),

    ('GET', '/db/memcache/bmemcached-set/'),
    ('GET', '/db/memcache/bmemcached-set-multi/'),
    ('GET', '/db/memcache/bmemcached-get/'),
    ('GET', '/db/memcache/bmemcached-get-multi/'),
    ('GET', '/db/memcache/bmemcached-delete/'),
    ('GET', '/db/memcache/bmemcached-delete-multi/'),
    ('GET', '/db/memcache/bmemcached/conn/default/'),

    # external httplib2
    ('GET', '/httplib2/get/'),
    ('GET', '/httplib2/post/'),
    ('GET', '/httplib2/error/900/'),

    # external requests
    ('GET', '/requests/get/'),
    ('GET', '/external/requests/get/'),
    ('GET', '/requests/post/'),
    ('GET', '/external/requests/post/'),
    ('GET', '/requests/error/900/'),

    # external urllib
    ('GET', '/urllib/get/'),
    ('GET', '/urllib/post/'),
    ('GET', '/urllib/urlencode/'),

    # external urllib2
    ('GET', '/urllib2/get/'),
    ('GET', '/urllib2/post/'),
    ('GET', '/urllib2/cookie/'),

    # external urllib3
    ('GET', '/urllib3/get/'),
    ('GET', '/urllib3/post/'),
    ('GET', '/urllib3/error/900/'),

    # block code
    ("GET", "/resp_200/"),
    ("GET", "/resp_500/"),
    ("GET", "/resp_json/"),
    ("GET", "/no_html_start/"),
    ("GET", "/no_html_end/"),
    ("GET", "/no_head_start/"),
    ("GET", "/no_head_end/"),
    ("GET", "/no_title_start/"),
    ("GET", "/no_title_end/"),
    ("GET", "/no_head_start_title_start/"),
    ("GET", "/no_head_start_title_end/"),
    ("GET", "/no_head/"),
    ("GET", "/no_title/"),
    ("GET", "/no_head_end_title_start/"),
    ("GET", "/no_head_end_title_end/"),
    ("GET", "/no_head_start_title/"),
    ("GET", "/no_head_title_start/"),
    ("GET", "/no_head_end_title/"),
    ("GET", "/html_start_has_attr/"),
    ("GET", "/html_end_has_attr/"),
    ("GET", "/html_has_attr_lang_en/"),
    ("GET", "/html_has_attr_lang_zh/"),
    ("GET", "/head_start_has_attr/"),
    ("GET", "/head_end_has_attr/"),
    ("GET", "/title_start_has_attr/"),
    ("GET", "/title_end_has_attr/"),
    ("GET", "/head_start_title_start_has_attr/"),
    ("GET", "/head_start_title_end_has_attr/"),
    ("GET", "/head_end_title_start_has_attr/"),
    ("GET", "/head_end_title_end_has_attr/"),
    ("GET", "/befor_head_start_has_head_note/"),
    ("GET", "/befor_title_start_has_head_note/"),
    ("GET", "/befor_title_end_has_head_note/"),
    ("GET", "/befor_head_end_has_head_note/"),
    ("GET", "/after_head_end_has_head_note/"),
    ("GET", "/befor_head_start_has_title_note/"),
    ("GET", "/befor_title_start_has_title_note/"),
    ("GET", "/befor_title_end_has_title_note/"),
    ("GET", "/befor_head_end_has_title_note/"),
    ("GET", "/after_head_end_has_title_note/"),
    ("GET", "/title_has_special_char/"),
    ("GET", "/head_has_special_char/"),
    ("GET", "/html_has_special_char/"),
    ("GET", "/size_gt_64k/"),

    ('GET', "/rabbitmq/producer/select-connect/")
]

HOSTS = ["http://192.168.177.150:8088"]
NUM = 0


def req(number, method, url):
    try:
        resp = requests.request(method, url)
        status_code = resp.status_code
        logging.info("【{number}】 req url: [{url}] get status code {code}========>>>>>>>>".format(number=number, url=url, code=status_code))
    except Exception as e:
        logging.error("【{number}】 req url: [{url}] error ==>> {e}".format(number={number}, url=url, e=e))

def main():
    global NUM
    spawns = []
    for url in urls:
        method = url[0]
        for host in HOSTS:
            NUM += 1
            url_ = "{host}/{url}".format(host=host.strip("/"), url=url[1].lstrip("/"))
            # req(NUM, method, url_)
            spawns.append(gevent.spawn(req, NUM, method, url_))
    gevent.joinall(spawns)

def signal_handler(signal, frame):
    logging.error("total {num} url requested ==>>".format(num=NUM))
    sys.exit(0)

if __name__ == "__main__":
    # 处理信号
    signal.signal(signal.SIGINT, signal_handler)

    # 解析参数
    request_time = None
    opts, args = getopt.getopt(sys.argv[1:],"ht:",["t="])
    for opt, arg in opts:
        if opt in ("-t", "-time"):
            request_time = arg

    if request_time is None:
        # 没有"-t"参数情况
        while 1:
            main()
    else:
        # 有 "-t"参数情况
        start_time = time.time()
        while 1:
            if int(time.time() - start_time) >= int(request_time):
                break
            main()