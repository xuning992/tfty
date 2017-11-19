#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random
from ..config import MONGODB_CONF


def get_package(version):

    if version == "2.0":
        from public.packages.pymongo.v20 import pymongo
    elif version == "2.1":
        from public.packages.pymongo.v21 import pymongo
    elif version == "2.2":
        from public.packages.pymongo.v22 import pymongo
    elif version == "2.3":
        from public.packages.pymongo.v23 import pymongo
    elif version == "2.4":
        from public.packages.pymongo.v24 import pymongo
    elif version == "2.5":
        from public.packages.pymongo.v25 import pymongo
    elif version == "2.6":
        from public.packages.pymongo.v26 import pymongo
    elif version == "2.7":
        from public.packages.pymongo.v27 import pymongo
    elif version == "2.8":
        from public.packages.pymongo.v28 import pymongo
    elif version == "2.9":
        from public.packages.pymongo.v29 import pymongo
    elif version == "3.0":
        from public.packages.pymongo.v30 import pymongo
    elif version == "3.1":
        from public.packages.pymongo.v31 import pymongo
    elif version == "3.2":
        from public.packages.pymongo.v32 import pymongo
    elif version == "3.3":
        from public.packages.pymongo.v33 import pymongo
    elif version == "3.4.0":
        from public.packages.pymongo.v34 import pymongo

    return pymongo


def get_connection(version):

    pymongo = get_package(version)

    if version >= "2.9":
        # >=2.9
        mongo_conn = pymongo.MongoClient(MONGODB_CONF['host'], MONGODB_CONF['port'], connect=False)
        mongo_db = mongo_conn[MONGODB_CONF['db']]

    else:
        mongo_conn = pymongo.Connection(host=MONGODB_CONF['host'], port=MONGODB_CONF['port'])
        mongo_db = mongo_conn[MONGODB_CONF['db']]

    return mongo_db


def mongodb_insert(version):
    _id = random.randint(0, 100)
    name = 'tom'
    age = 18 if _id % 2 else 19
    query = {
        'id': _id,
        'name': name,
        'age': age
    }

    mongo_db = get_connection(version)
    # >=2.9
    # mongo_db.t_user.insert_one(query)

    # >=2.0
    mongo_db.t_user.insert(query)
    return "success"


def mongodb_delete(version):
    query = {
        'age': 18
    }

    mongo_db = get_connection(version)
    mongo_db.t_user.remove(query)
    return "success"


def mongodb_update(version):
    query1 = {
        'age': 18
    }
    query2 = {
        '$set': {
            'age': 20
        }
    }
    mongo_db = get_connection(version)
    mongo_db.t_user.update(query1, query2)
    return "success"


def mongodb_select(version):
    query = {
        'name': 'tom'
    }
    mongo_db = get_connection(version)
    cursors = mongo_db.t_user.find(query)
    users = []
    for cursor in cursors:
        users.append(str(cursor))

    return str(users)


def mongodb_conn_by_connection(version):

    pymongo = get_package(version)
    if hasattr(pymongo, "Connection"):
        mongo_conn = pymongo.Connection(host=MONGODB_CONF['host'], port=MONGODB_CONF['port'])
        mongo_db = mongo_conn[MONGODB_CONF['db']]
        query = {
            'name': 'tom'
        }
        cursors = mongo_db.t_user.find(query)
        users = []
        for cursor in cursors:
            users.append(str(cursor))

        return str(users)
    else:
        return "pymongo object has no attribute 'Connection'"


def mongodb_conn_by_mongoclient_params(version):

    pymongo = get_package(version)
    if hasattr(pymongo, "MongoClient"):
        mongo_conn = pymongo.MongoClient(MONGODB_CONF['host'], MONGODB_CONF['port'])
        mongo_db = mongo_conn[MONGODB_CONF['db']]
        query = {
            'name': 'tom'
        }
        cursors = mongo_db.t_user.find(query)
        users = []
        for cursor in cursors:
            users.append(str(cursor))

        return str(users)
    else:
        return "pymongo object has no attribute 'MongoClient'"


def mongodb_conn_by_mongoclient_str(version):

    pymongo = get_package(version)
    if hasattr(pymongo, "MongoClient"):
        mongo_conn = pymongo.MongoClient('mongodb://{host}:{port}/'.format(host=MONGODB_CONF['host'], port=MONGODB_CONF['port']))
        mongo_db = mongo_conn[MONGODB_CONF['db']]
        query = {
            'name': 'tom'
        }
        cursors = mongo_db.t_user.find(query)
        users = []
        for cursor in cursors:
            users.append(str(cursor))

        return str(users)
    else:
        return "pymongo object has no attribute 'MongoClient'"
