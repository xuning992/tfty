# -*- coding: utf-8 -*-
from core.views.base import BaseHandler
from public.db_postgresql import db_psycopg2, db_psycopg2ct, db_psycopg2cffi


# psycopg2
class Psycopg2ParametersConnect(BaseHandler):
    def get(self):
        self.write(db_psycopg2.psycopg2_no_support_connect())


class Psycopg2BaseDataConnect(BaseHandler):
    def get(self):
        self.write(db_psycopg2.psycopg2_database_connect())


class Psycopg2UriConnect(BaseHandler):
    def get(self):
        self.write(db_psycopg2.psycopg2_uri_connect())


class Psycopg2UriNoPortConnect(BaseHandler):
    def get(self):
        self.write(db_psycopg2.psycopg2_uri_no_port_connect())


class Psycopg2ConnectStringNoPort(BaseHandler):
    def get(self):
        self.write(db_psycopg2.psycopg2_connectstring_no_port_connect())


class Psycopg2DBNameUserConnect(BaseHandler):
    def get(self):
        self.write(db_psycopg2.psycopg2_connectstring_connect())


class Psycopg2DBNameConnect(BaseHandler):
    def get(self):
        self.write(db_psycopg2.psycopg2_dbname_connect())


class Psycopg2NoPortConnect(BaseHandler):
    def get(self):
        self.write(db_psycopg2.psycopg2_no_port_connect())


class Psycopg2Insert(BaseHandler):
    def get(self):
        self.write(db_psycopg2.test_psycopg2_insert())


class Psycopg2Update(BaseHandler):
    def get(self):
        self.write(db_psycopg2.test_psycopg2_update())


class Psycopg2Select(BaseHandler):
    def get(self):
        self.write(db_psycopg2.test_psycopg2_select())


class Psycopg2Delete(BaseHandler):
    def get(self):
        self.write(db_psycopg2.test_psycopg2_delete())


class Psycopg2ConnectionPool(BaseHandler):
    def get(self):
        self.write(db_psycopg2.test_psycopg2_connection_pool())


class Psycopg2TimeoutError(BaseHandler):
    def get(self):
        self.write(db_psycopg2.test_psycopg2_timeout_error())


class Psycopg2TimeoutOk(BaseHandler):
    def get(self):
        self.write(db_psycopg2.test_psycopg2_timeout_ok())


class Psycopg2TableError(BaseHandler):
    def get(self):
        self.write(db_psycopg2.test_psycopg2_table_error())


class Psycopg2FieldError(BaseHandler):
    def get(self):
        self.write(db_psycopg2.test_psycopg2_field_error())


class Psycopg2SyntaxError(BaseHandler):
    def get(self):
        self.write(db_psycopg2.test_psycopg2_syntax_error())


class Psycopg2Operates(BaseHandler):
    def get(self):
        res_1 = db_psycopg2.test_psycopg2_insert()
        res_2 = db_psycopg2.test_psycopg2_delete()
        res_3 = db_psycopg2.test_psycopg2_update()
        res_4 = db_psycopg2.test_psycopg2_select()
        self.write("psycopg2\ninsert: %s\ndelete: %s\nupdate: %s\nselect: %s" % (res_1, res_2, res_3, res_4))


class Psycopg2Connections(BaseHandler):
    def get(self):
        res_1 = db_psycopg2.test_psycopg2_connection_pool()
        res_2 = db_psycopg2.psycopg2_no_port_connect()
        res_3 = db_psycopg2.psycopg2_connectstring_connect()
        res_4 = db_psycopg2.psycopg2_connectstring_no_port_connect()
        res_5 = db_psycopg2.psycopg2_uri_connect()
        res_6 = db_psycopg2.psycopg2_uri_no_port_connect()
        res_7 = db_psycopg2.psycopg2_database_connect()
        res_8 = db_psycopg2.psycopg2_dbname_connect()
        self.write("psycopg2\npool: %s\nno_port: %s\nconnectstring: %s\nconnectstring_no_port: %s\nuri: %s\nuri_no_port:"
                   " %s\ndatabase: %s\ndbname: %s" % (res_1, res_2, res_3, res_4, res_5, res_6, res_7, res_8))


# psycopg2ct
class Psycopg2ctParametersConnect(BaseHandler):
    def get(self):
        self.write(db_psycopg2ct.psycopg2ct_no_support_connect())


class Psycopg2ctBaseDataConnect(BaseHandler):
    def get(self):
        self.write(db_psycopg2ct.psycopg2ct_database_connect())


class Psycopg2ctUriConnect(BaseHandler):
    def get(self):
        self.write(db_psycopg2ct.psycopg2ct_uri_connect())


class Psycopg2ctUriNoPortConnect(BaseHandler):
    def get(self):
        self.write(db_psycopg2ct.psycopg2ct_uri_no_port_connect())


class Psycopg2ctConnectStringNoPort(BaseHandler):
    def get(self):
        self.write(db_psycopg2ct.psycopg2ct_connectstring_no_port_connect())


class Psycopg2ctDBNameUserConnect(BaseHandler):
    def get(self):
        self.write(db_psycopg2ct.psycopg2ct_connectstring_connect())


class Psycopg2ctDBNameConnect(BaseHandler):
    def get(self):
        self.write(db_psycopg2ct.psycopg2ct_dbname_connect())


class Psycopg2ctNoPortConnect(BaseHandler):
    def get(self):
        self.write(db_psycopg2ct.psycopg2ct_no_port_connect())


class Psycopg2ctInsert(BaseHandler):
    def get(self):
        self.write(db_psycopg2ct.test_psycopg2ct_insert())


class Psycopg2ctUpdate(BaseHandler):
    def get(self):
        self.write(db_psycopg2ct.test_psycopg2ct_update())


class Psycopg2ctSelect(BaseHandler):
    def get(self):
        self.write(db_psycopg2ct.test_psycopg2ct_select())


class Psycopg2ctDelete(BaseHandler):
    def get(self):
        self.write(db_psycopg2ct.test_psycopg2ct_delete())


class Psycopg2ctConnectionPool(BaseHandler):
    def get(self):
        self.write(db_psycopg2ct.test_psycopg2ct_connection_pool())


class Psycopg2ctTimeoutError(BaseHandler):
    def get(self):
        self.write(db_psycopg2ct.test_psycopg2ct_timeout_error())


class Psycopg2ctTimeoutOk(BaseHandler):
    def get(self):
        self.write(db_psycopg2ct.test_psycopg2ct_timeout_ok())


class Psycopg2ctTableError(BaseHandler):
    def get(self):
        self.write(db_psycopg2ct.test_psycopg2ct_table_error())


class Psycopg2ctFieldError(BaseHandler):
    def get(self):
        self.write(db_psycopg2ct.test_psycopg2ct_field_error())


class Psycopg2ctSyntaxError(BaseHandler):
    def get(self):
        self.write(db_psycopg2ct.test_psycopg2ct_syntax_error())


# psycopg2cffi
class Psycopg2cffiParametersConnect(BaseHandler):
    def get(self):
        self.write(db_psycopg2cffi.psycopg2cffi_no_support_connect())


class Psycopg2cffiBaseDataConnect(BaseHandler):
    def get(self):
        self.write(db_psycopg2cffi.psycopg2cffi_database_connect())


class Psycopg2cffiUriConnect(BaseHandler):
    def get(self):
        self.write(db_psycopg2cffi.psycopg2cffi_uri_connect())


class Psycopg2cffiUriNoPortConnect(BaseHandler):
    def get(self):
        self.write(db_psycopg2cffi.psycopg2cffi_uri_no_port_connect())


class Psycopg2cffiConnecStringNoPort(BaseHandler):
    def get(self):
        self.write(db_psycopg2cffi.psycopg2cffi_connectstring_no_port_connect())


class Psycopg2cffiDBNameUserConnect(BaseHandler):
    def get(self):
        self.write(db_psycopg2cffi.psycopg2cffi_connectstring_connect())


class Psycopg2cffiDBNameConnect(BaseHandler):
    def get(self):
        self.write(db_psycopg2cffi.psycopg2cffi_dbname_connect())


class Psycopg2cffiNoPortConnect(BaseHandler):
    def get(self):
        self.write(db_psycopg2cffi.psycopg2cffi_no_port_connect())


class Psycopg2cffiInsert(BaseHandler):
    def get(self):
        self.write(db_psycopg2cffi.test_psycopg2cffi_insert())


class Psycopg2cffiUpdate(BaseHandler):
    def get(self):
        self.write(db_psycopg2cffi.test_psycopg2cffi_update())


class Psycopg2cffiSelect(BaseHandler):
    def get(self):
        self.write(db_psycopg2cffi.test_psycopg2cffi_select())


class Psycopg2cffiDelete(BaseHandler):
    def get(self):
        self.write(db_psycopg2cffi.test_psycopg2cffi_delete())


class Psycopg2cffiConnectionPool(BaseHandler):
    def get(self):
        self.write(db_psycopg2cffi.test_psycopg2cffi_connection_pool())


class Psycopg2cffiTableError(BaseHandler):
    def get(self):
        self.write(db_psycopg2cffi.test_psycopg2cffi_table_error())


class Psycopg2cffiFieldError(BaseHandler):
    def get(self):
        self.write(db_psycopg2cffi.test_psycopg2cffi_field_error())


class Psycopg2cffiSyntaxError(BaseHandler):
    def get(self):
        self.write(db_psycopg2cffi.test_psycopg2cffi_syntax_error())
