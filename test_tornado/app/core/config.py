# -*- coding: utf-8 -*-
"""
"""

''' web服务器配置项 '''
WEB_SERVER = {
    'host': '127.0.0.1',                                        # web服务器ip地址
    'port': 9001,
    'gevent_port': 9002,                                         # web服务器端口号
    'uwsgi_port': 9003,                                         # web服务器端口号
    'agreement': 'http'                                         # 协议   
}

''' Oracle数据库服务器配置项 '''
DB_ORACLE = {
    'host': '192.168.1.15',
    'port': 1521,
    'xe': 'nbsdb',
    'login_name': 'test',
    'pwd': 'test',
    'agreement': 'http',
}

''' mysql数据库服务器配置项 '''
DB_MYSQL = {
    'host': '127.0.0.1',
    'port': 3306,
    'login_name': 'root',
    'pwd': 'heianbojue',
    'db': 'test'
}

''' mongodb数据库服务器配置项 '''
DB_MONGODB = {
    'host': '127.0.0.1',
    'port': 27017,
    'db': 'test'
}

''' redis数据库服务器配置项'''
DB_REDIS = {
    'host': '127.0.0.1',
    'port': 6379,
    'db': 0
}

''' memcache数据库服务器配置项'''
DB_MEMCACHE = {
    'host': '127.0.0.1',
    'port': 11211
}

''' tingyun agent config file env'''
TINGYUN_AGENT = {
    'default_config_path': '/tmp/tingyun.ini',
    'gevent_config_path': '/tmp/tingyun_gevent.ini'
}