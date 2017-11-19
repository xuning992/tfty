import random
import uuid


def common_insert_sql():
    i = random.random()
    i_ = random.random()
    name_ = "%sadd_by_test_%s" % (i, i_)
    content_type_id_ = random.randint(1, 10)
    codename_ = "%stype_for_test_%s" % (i, i_)
    sql = "INSERT INTO auth_permission (name, content_type_id, codename) VALUES ('%s', %s, '%s')" % (
        name_, content_type_id_, codename_)
    return sql


def diff_common_insert_sql():
    i = random.random()
    i_ = random.random()
    user_id_ = "%suser_%s" % (i, i_)
    group_id_ = "%sgroup_%s" % (i, i_)
    sql = "INSERT INTO auth_user_groups (user, group) VALUES (%s, %s, %s)" % (user_id_, group_id_)
    return sql


def common_insert_many_sql():
    data = []
    j = random.random()
    j_ = random.random()
    for i in range(2):
        name_ = "%sadd_by_test_%d" % (j, j_)
        content_type_id_ = random.randint(1, 10)
        codename_ = "%stype_for_test_%d" % (j, j_)
        data.append((name_, content_type_id_, codename_))
    sql = "INSERT INTO auth_permission (name, content_type_id, codename) VALUES (%s, %s, %s)"
    return sql, data


def common_oracle_insert_many_sql():
    data = []
    for i in range(2):
        _id = random.randint(1, 100000000)
        __id = random.randint(1, 1000000000000)
        name = 'tom'
        age = 18 if _id % 2 else 19
        data.append((_id+__id, name, age))
    sql = "insert into t_user_oracle (id, name, age) values (:1, :2, :3)"
    return sql, data


def common_sqlserver_insert_many_sql():
    data = []
    for i in range(2):
        _id = random.randint(1, 100000000)
        name = 'tom'
        age = 18 if _id % 2 else 19
        data.append((_id, name, age))
    sql = "insert into t_user_oracle (id, name, age) values (?,?,?)"
    return sql, data


def common_delete_sql():
    sql = "DELETE FROM auth_permission WHERE name='add_by_test1' AND content_type_id<=10"
    # sql = "DELETE FROM auth_permission WHERE id IN (SELECT id FROM auth_permission ORDER BY id DESC limit 1)"
    return sql


def diff_common_delete_sql():
    sql = "DELETE FROM auth_user_groups WHERE id=2"
    return sql


def common_update_sql():
    sql = "UPDATE auth_permission set name='update_by_test' where id=1"
    return sql


def diff_common_update_sql():
    sql = "UPDATE auth_user_group set user='update_user' where id=1"
    return sql


def common_select_sql():
    sql = "SELECT * FROM auth_permission where id<=100 and content_type_id<10"
    return sql


def diff_common_select_sql():
    sql = "SELECT * FROM auth_user_groups where id<=12"
    return sql


def common_table_error_sql():
    sql = "SELECT * FROM abcdefg"
    return sql


def common_field_error_sql():
    sql = "SELECT * FROM auth_permission WHERE a=1"
    return sql


def common_syntax_error_sql():
    sql = "SELEC * FROM auth_permission WHERE id=1"
    return sql


def common_execute(conn, sql):
    cursor = conn.cursor()
    try:
        cursor.execute(sql)
        conn.commit()
    except Exception as err:
        print "then execute sql, error was happened: %s " % err
        raise err


def common_execute_many(conn, sql, data):
    cursor = conn.cursor()
    res = cursor.executemany(sql, data)
    conn.commit()
    return str(res)


def common_select(conn, sql):
    cursor = conn.cursor()
    cursor.execute(sql)
    res = cursor.fetchall()
    return str(res)


def common_select_conn(conn, sql):
    cursor = conn.cursor()
    cursor.execute(sql)
    res = cursor.fetchall()
    cursor.close()
    conn.close()
    return str(res)


def common_fetch_one(conn, sql):
    cursor = conn.cursor()
    cursor.execute(sql)
    user = cursor.fetchone()

    tmp = {
        'id': user[0],
        'name': user[1],
        'age': user[2]
    }
    return str(tmp)


def common_fetch_many(conn, sql):
    cursor = conn.cursor()
    cursor.execute(sql)
    res = cursor.fetchmany(2)

    users = []
    for user in res:
        tmp = {
            'id': user[0],
            'name': user[1],
            'age': user[2]
        }
        users.append(tmp)
    return str(users)


def common_fetch_all(conn, sql):
    cursor = conn.cursor()
    cursor.execute(sql)
    res = cursor.fetchall()

    users = []
    for user in res:
        tmp = {
            'id': user[0],
            'name': user[1],
            'age': user[2]
        }
        users.append(tmp)
    return str(users)


def common_set(ctl):
    return str(ctl.set('name', str(uuid.uuid1())))


def common_set_multi(ctl):
    return str(ctl.set_multi({
        'name':'tom',
        'age': 18,
        'sex': 1
        }))


def common_set_many(ctl):
    return str(ctl.set_many({
        'name':'tom',
        'age': 18,
        'sex': 1
        }))


def common_delete(ctl):
    return str(ctl.delete('name'))


def common_delete_multi(ctl):
    return str(ctl.delete_multi(['age', 'sex']))


def common_delete_many(ctl):
    return str(ctl.delete_many(['age', 'sex']))


def common_get(ctl):
    return str(ctl.get('name'))


def common_get_multi(ctl):
    return str(ctl.get_multi(['name', 'age', 'sex']))


def common_get_many(ctl):
    return str(ctl.get_many(['name', 'age', 'sex']))


def common_hset(ctl):
    prop = "id:56"
    key = "name"
    res = ctl.hset(prop, key, str(uuid.uuid1()))
    return res


def common_hget(ctl):
    prop = "id:56"
    key = "name"
    res = ctl.hget(prop, key)
    return res


def common_hgetall(ctl):
    prop = "id:56"
    return str(ctl.hgetall(prop))


def common_rpush(ctl):
    key = "lres"
    ctl.rpush(key, str(uuid.uuid1()))
    return str(ctl.rpush(key, str(uuid.uuid1())))


def common_lpop(ctl):
    key = "res"
    ctl.lpop(key)
    return "redis lpop is success"


def common_lrange(ctl):
    key = "res"
    return str(ctl.lrange(key, 0, -1))


def common_sadd(ctl):
    key = 'set'
    uid1 = str(uuid.uuid1())
    uid2 = 'hello world'
    ctl.sadd(key, uid1)
    return str(ctl.sadd(key, uid2))


def common_srem(ctl):
    return str(ctl.srem('set', 'hello world'))


def common_smembers(ctl):
    return str(ctl.smembers('set'))


def common_zadd(ctl):
    ctl.zadd('sset', 'name', 1)
    return str(ctl.zadd('sset', 'age', 2))


def common_zrange(ctl):
    return str(ctl.zrange('sset', 0, -1))


def psycopg2_timeout_sql(millisecond):
    return "set statement_timeout to {millisecond};".format(millisecond=millisecond)


def psycopg2_sleep_sql(second):
    return "select pg_sleep({second});".format(second=second)