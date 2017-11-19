# -*- coding: utf-8 -*-

import random
import time
import logging
from django.http import HttpResponse
from django.http import request
from django.db import transaction, IntegrityError
from test_django.models import test_db
database = {"mysql": "mysql_mysqldb", "postgresql": "postgresql_psycopg2", "oracle": "oracle_cx_oracle"}
cls = test_db.DjangoOrmTest


def db_insert(request):
    """
    :param sql: 作为参数传入，控制sql的种类
    :return:
    """

    sql_type = request.GET.get("sql", "mysql")
    database_ = database[sql_type]

    rand = random.randint(1, 1000000000000000000)
    rand_ = random.randint(0, 150)
    id_rand = random.randint(1, 100000000)
    data = {
        "name": "M_%d" % rand,
        "address": "Q_%d" % rand,
        "school": "H_%d" % rand,
        "grade": rand_
    }

    if database_ == "oracle":
        data = {
            "id": int(id_rand),
            "name": "M_%d" % rand,
            "address": "Q_%d" % rand,
            "school": "H_%d" % rand,
            "grade": rand_
        }

    cls.objects.using(database_).create(**data)
    html = "<html><body>[%s] insert data is %s.</body></html>" % (sql_type, data)
    return HttpResponse(html)


def db_delete(request):

    sql_type = request.GET.get("sql", "mysql")
    database_ = database[sql_type]

    cls.objects.using(database_).last().delete()
    html = "<html><body>[%s] delete is success</body></html>" % sql_type
    return HttpResponse(html)


def db_update(request):

    sql_type = request.GET.get("sql", "mysql")
    database_ = database[sql_type]

    cls.objects.using(database_).last().update(name="MZ")
    html = "<html><body>[%s] update is success</body></html>" % sql_type
    return HttpResponse(html)


def db_select(request):

    sql_type = request.GET.get("sql", "mysql")
    database_ = database[sql_type]

    rlt = cls.objects.using(database_).all()
    values = []
    for row in rlt:
        value = (row.id, row.name, row.address, row.school, row.grade)
        values.append(value)
    html = "<html><body>[%s] select data is %s len [%s]</body></html>" % (sql_type, values, len(values))
    return HttpResponse(html)


@transaction.atomic
def db_transaction(request):
    """
    :param sql: 作为参数传入，控制sql的种类
    :return:
    """
    sql_type = request.GET.get("sql", "mysql")
    database_ = database[sql_type]

    rand = random.randint(1, 1000000000000000000)
    rand_ = random.randint(0, 150)
    id_rand = random.randint(1, 100000000)
    data = {
        "name": "M_%d" % rand,
        "address": "Q_%d" % rand,
        "school": "H_%d" % rand,
        "grade": rand_
    }

    data_error = {
        "name": "M_%d" % rand,
        "address": "Q_%d" % rand,
        "school": "H_%d" % rand,
        "grade": rand_,
        "age": 18
    }

    cls.objects.using(database_).create(**data)
    try:
        with transaction.atomic():
            cls.objects.using(database_).create(**data_error)
    except Exception as e:
        logging.error("create user error==>> %s", data_error)

    cls.objects.using(database_).create(**data)
    transaction.on_commit(send_email)
    return HttpResponse("create user success")


def send_email():
    import requests
    requests.get("http://127.0.0.1:9102/")
