import sys

path = '/home/nb/webapps/tfty/test_tornado/app/'
if path not in sys.path:
    sys.path.append(path)

from core.views.framework import HelloHandler
from core.views.framework import RespError500
from core.views.framework import FinishHandler
from core.views.framework import OnFinishHandler
from core.views.framework import InitializeHandler
from core.views.framework import PrepareHandler
from core.views.framework import RequestMethodHandler
from core.views.framework import RenderHandler
from core.views.framework import HttpClientHandler
from core.views.framework import AsyncHttpClientHandler
from core.views.framework import CoroutineHandler

# db oracle cx_Oracle 16
from core.views.database_oracle import OraclePositionConn
from core.views.database_oracle import OracleConnectingConn
from core.views.database_oracle import OracleMakesnConn
from core.views.database_oracle import OracleInsert
from core.views.database_oracle import OracleDelete
from core.views.database_oracle import OracleUpdate
from core.views.database_oracle import OracleSelect
from core.views.database_oracle import OracleFetchOne
from core.views.database_oracle import OracleFetchMany
from core.views.database_oracle import OracleFetchAll
from core.views.database_oracle import OracleExecuteMany
from core.views.database_oracle import OracleTableError
from core.views.database_oracle import OracleFieldError
from core.views.database_oracle import OracleSyntaxError
from core.views.database_oracle import OracleOperates
from core.views.database_oracle import OracleConnections

# db mysql mysqldb 16
from core.views.database_mysql import MysqldbPositionConnect
from core.views.database_mysql import MysqldbKeyworkConnect
from core.views.database_mysql import MysqldbPoolConnect
from core.views.database_mysql import MysqldbInsert
from core.views.database_mysql import MysqldbDelete
from core.views.database_mysql import MysqldbUpdate
from core.views.database_mysql import MysqldbSelect
from core.views.database_mysql import MysqldbFetchOne
from core.views.database_mysql import MysqldbFetchMany
from core.views.database_mysql import MysqldbFetchAll
from core.views.database_mysql import MysqldbExecuteMany
from core.views.database_mysql import MysqldbTableError
from core.views.database_mysql import MysqldbFieldError
from core.views.database_mysql import MysqldbSyntaxError
from core.views.database_mysql import MysqldbOperates
from core.views.database_mysql import MysqldbConnections

# db mysql pymysql 17
from core.views.database_mysql import PymysqlNoPortConnect
from core.views.database_mysql import PymysqlDictConnect
from core.views.database_mysql import PymysqlPositionConnect
from core.views.database_mysql import PymysqlKeywordConnect
from core.views.database_mysql import PymysqlInsert
from core.views.database_mysql import PymysqlDelete
from core.views.database_mysql import PymysqlUpdate
from core.views.database_mysql import PymysqlSelect
from core.views.database_mysql import PymysqlFetchOne
from core.views.database_mysql import PymysqlFetchMany
from core.views.database_mysql import PymysqlFetchAll
from core.views.database_mysql import PymysqlExecuteMany
from core.views.database_mysql import PymysqlTableError
from core.views.database_mysql import PymysqlFieldError
from core.views.database_mysql import PymysqlSyntaxError
from core.views.database_mysql import PymysqlOperates
from core.views.database_mysql import PymysqlConnections

# db mysql oursql 12
from core.views.database_mysql import OursqlKeywordConnect
from core.views.database_mysql import OursqlPositionConnect
from core.views.database_mysql import OursqlNoPortConnect
from core.views.database_mysql import OursqlInsert
from core.views.database_mysql import OursqlDelete
from core.views.database_mysql import OursqlUpdate
from core.views.database_mysql import OursqlSelect
from core.views.database_mysql import OursqlFetchOne
from core.views.database_mysql import OursqlFetchMany
from core.views.database_mysql import OursqlFetchAll
from core.views.database_mysql import OursqlOperates
from core.views.database_mysql import OursqlConnections

# db mongodb pymongo 7
from core.views.database_mongodb import MongodbInsert
from core.views.database_mongodb import MongodbDelete
from core.views.database_mongodb import MongodbUpdate
from core.views.database_mongodb import MongodbSelect
from core.views.database_mongodb import MongodbConnClass
from core.views.database_mongodb import MongodbConnParams
from core.views.database_mongodb import MongodbConnStr

# redis 16
from core.views.database_redis import RedisSet
from core.views.database_redis import RedisGet
from core.views.database_redis import RedisHSet
from core.views.database_redis import RedisHGet
from core.views.database_redis import RedisHGetAll
from core.views.database_redis import RedisRPush
from core.views.database_redis import RedisLPop
from core.views.database_redis import RedisLRange
from core.views.database_redis import RedisSAdd
from core.views.database_redis import RedisSRem
from core.views.database_redis import RedisSMembers
from core.views.database_redis import RedisZAdd
from core.views.database_redis import RedisZRange
from core.views.database_redis import RedisConnByRedis
from core.views.database_redis import RedisConnByStrictredis
from core.views.database_redis import RedisConnPool

# memcached 21
from core.views.database_memcache import MemcacheSet
from core.views.database_memcache import MemcacheSetMulti
from core.views.database_memcache import MemcacheGet
from core.views.database_memcache import MemcacheGetMulti
from core.views.database_memcache import MemcacheDelete
from core.views.database_memcache import MemcacheDeleteMulti
from core.views.database_memcache import MemcacheConnDefault

from core.views.database_memcache import PymemcacheSetMulti
from core.views.database_memcache import PymemcacheGet
from core.views.database_memcache import PymemcacheGetMulti
from core.views.database_memcache import PymemcacheDelete
from core.views.database_memcache import PymemcacheDeleteMulti
from core.views.database_memcache import PymemcacheConnByClient
from core.views.database_memcache import PymemcacheConnByHashClient

from core.views.database_memcache import BMemcachedSet
from core.views.database_memcache import BMemcachedSetMulti
from core.views.database_memcache import BMemcachedGet
from core.views.database_memcache import BMemcachedGetMulti
from core.views.database_memcache import BMemcachedDelete
from core.views.database_memcache import BMemcachedDeleteMulti
from core.views.database_memcache import BMemcachedConnDefault

# db postgresql psycopg2 20
from core.views.database_postgresql import Psycopg2ParametersConnect
from core.views.database_postgresql import Psycopg2BaseDataConnect
from core.views.database_postgresql import Psycopg2UriConnect
from core.views.database_postgresql import Psycopg2UriNoPortConnect
from core.views.database_postgresql import Psycopg2ConnectStringNoPort
from core.views.database_postgresql import Psycopg2DBNameUserConnect
from core.views.database_postgresql import Psycopg2DBNameConnect
from core.views.database_postgresql import Psycopg2NoPortConnect
from core.views.database_postgresql import Psycopg2Insert
from core.views.database_postgresql import Psycopg2Update
from core.views.database_postgresql import Psycopg2Select
from core.views.database_postgresql import Psycopg2Delete
from core.views.database_postgresql import Psycopg2ConnectionPool
from core.views.database_postgresql import Psycopg2TimeoutError
from core.views.database_postgresql import Psycopg2TimeoutOk
from core.views.database_postgresql import Psycopg2TableError
from core.views.database_postgresql import Psycopg2FieldError
from core.views.database_postgresql import Psycopg2SyntaxError
from core.views.database_postgresql import Psycopg2Operates
from core.views.database_postgresql import Psycopg2Connections

# db postgresql psycopg2ct 18
from core.views.database_postgresql import Psycopg2ctParametersConnect
from core.views.database_postgresql import Psycopg2ctBaseDataConnect
from core.views.database_postgresql import Psycopg2ctUriConnect
from core.views.database_postgresql import Psycopg2ctUriNoPortConnect
from core.views.database_postgresql import Psycopg2ctConnectStringNoPort
from core.views.database_postgresql import Psycopg2ctDBNameUserConnect
from core.views.database_postgresql import Psycopg2ctDBNameConnect
from core.views.database_postgresql import Psycopg2ctNoPortConnect
from core.views.database_postgresql import Psycopg2ctInsert
from core.views.database_postgresql import Psycopg2ctUpdate
from core.views.database_postgresql import Psycopg2ctSelect
from core.views.database_postgresql import Psycopg2ctDelete
from core.views.database_postgresql import Psycopg2ctConnectionPool
from core.views.database_postgresql import Psycopg2ctTimeoutError
from core.views.database_postgresql import Psycopg2ctTimeoutOk
from core.views.database_postgresql import Psycopg2ctTableError
from core.views.database_postgresql import Psycopg2ctFieldError
from core.views.database_postgresql import Psycopg2ctSyntaxError

# db postgresql psycopg2cffi 16
from core.views.database_postgresql import Psycopg2cffiParametersConnect
from core.views.database_postgresql import Psycopg2cffiBaseDataConnect
from core.views.database_postgresql import Psycopg2cffiUriConnect
from core.views.database_postgresql import Psycopg2cffiUriNoPortConnect
from core.views.database_postgresql import Psycopg2cffiConnecStringNoPort
from core.views.database_postgresql import Psycopg2cffiDBNameUserConnect
from core.views.database_postgresql import Psycopg2cffiDBNameConnect
from core.views.database_postgresql import Psycopg2cffiNoPortConnect
from core.views.database_postgresql import Psycopg2cffiInsert
from core.views.database_postgresql import Psycopg2cffiUpdate
from core.views.database_postgresql import Psycopg2cffiSelect
from core.views.database_postgresql import Psycopg2cffiDelete
from core.views.database_postgresql import Psycopg2cffiConnectionPool
from core.views.database_postgresql import Psycopg2cffiTableError
from core.views.database_postgresql import Psycopg2cffiFieldError
from core.views.database_postgresql import Psycopg2cffiSyntaxError

# external httplib2
from core.views.external_httplib2 import Httplib2Get
from core.views.external_httplib2 import Httplib2Post
from core.views.external_httplib2 import Httplib2Error

# external requests
from core.views.external_requests import RequestsGet
from core.views.external_requests import ExternalRequestsGet
from core.views.external_requests import RequestsPost
from core.views.external_requests import ExternalRequestsPost
from core.views.external_requests import RequestsError

# external urllib
from core.views.external_urllib import UrllibGet
from core.views.external_urllib import UrllibPost
from core.views.external_urllib import UrllibUrlencode

# external urllib2
from core.views.external_urllib2 import Urllib2Get
from core.views.external_urllib2 import Urllib2Post
from core.views.external_urllib2 import Urllib2Cookie

# external urllib3
from core.views.external_urllib3 import Urllib3Get
from core.views.external_urllib3 import Urllib3Post
from core.views.external_urllib3 import Urllib3Error

# block code
from core.views.block_code import Resp200
from core.views.block_code import Resp500
from core.views.block_code import RespJson
from core.views.block_code import NoHtmlStart
from core.views.block_code import NoHtmlEnd
from core.views.block_code import NoHeadStart
from core.views.block_code import NoHeadEnd
from core.views.block_code import NoTitleStart
from core.views.block_code import NoTitleEnd
from core.views.block_code import NoHeadStartTitleStart
from core.views.block_code import NoHeadStartTitleEnd
from core.views.block_code import NoHead
from core.views.block_code import NoTitle
from core.views.block_code import NoHeadEndTitleStart
from core.views.block_code import NoHeadEndTitleEnd
from core.views.block_code import NoHeadStartTitle
from core.views.block_code import NoHeadTitleStart
from core.views.block_code import NoHeadEndTitle
from core.views.block_code import HtmlStartHasAttr
from core.views.block_code import HtmlEndHasAttr
from core.views.block_code import HtmlHasAttrLangEN
from core.views.block_code import HtmlHasAttrLangZH
from core.views.block_code import HeadStartHasAttr
from core.views.block_code import HeadEndHasAttr
from core.views.block_code import TitleStartHasAttr
from core.views.block_code import TitleEndHasAttr
from core.views.block_code import HeadStartTitleStartHasAttr
from core.views.block_code import HeadStartTitleEndHasAttr
from core.views.block_code import HeadEndTitleStartHasAttr
from core.views.block_code import HeadEndTitleEndHasAttr
from core.views.block_code import BeforHeadStartHasHeadNote
from core.views.block_code import BeforTitleStartHasHeadNote
from core.views.block_code import BeforTitleEndHasHeadNote
from core.views.block_code import BeforHeadEndHasHeadNote
from core.views.block_code import AfterHeadEndHasHeadNote
from core.views.block_code import BeforHeadStartHasTitleNote
from core.views.block_code import BeforTitleStartHasTitleNote
from core.views.block_code import BeforTitleEndHasTitleNote
from core.views.block_code import BeforHeadEndHasTitleNote
from core.views.block_code import AfterHeadEndHasTitleNote
from core.views.block_code import TitleHasSpecialChar
from core.views.block_code import HeadHasSpecialChar
from core.views.block_code import HtmlHasSpecialChar
from core.views.block_code import SizeGt64k


# rabbitmq
from core.views.message_rabbitmq import RabbitmqAsynConnection

urls = [
    # framework
    (r"/hello/?", HelloHandler),
    (r"/500/?", RespError500),
    (r"/finish/?", FinishHandler),
    (r"/on-finish/?", OnFinishHandler),
    (r"/initialize/?$", InitializeHandler, dict(db="mysql")),
    (r"/prepare/?", PrepareHandler),
    (r"/request-method/?", RequestMethodHandler),
    (r"/render/?", RenderHandler),
    (r"/httpclient/?", HttpClientHandler),
    (r"/asynchttpclient/?", AsyncHttpClientHandler),
    (r"/coroutine/?", CoroutineHandler),

    # db oracle cx_Oracle
    (r'/db/oracle/position-conn/?$', OraclePositionConn),
    (r'/db/oracle/connecting-conn/?$', OracleConnectingConn),
    (r'/db/oracle/makedsn-conn/?$', OracleMakesnConn),
    (r'/db/oracle/insert/?$', OracleInsert),
    (r'/db/oracle/delete/?$', OracleDelete),
    (r'/db/oracle/update/?$', OracleUpdate),
    (r'/db/oracle/select/?$', OracleSelect),
    (r'/db/oracle/fetch-one/?$', OracleFetchOne),
    (r'/db/oracle/fetch-many/?$', OracleFetchMany),
    (r'/db/oracle/fetch-all/?$', OracleFetchAll),
    (r'/db/oracle/execute-many/?$', OracleExecuteMany),
    (r'/db/oracle/table-error/?$', OracleTableError),
    (r'/db/oracle/field-error/?$', OracleFieldError),
    (r'/db/oracle/syntax-error/?$', OracleSyntaxError),
    (r'/db/oracle/operates/?$', OracleOperates),
    (r'/db/oracle/connections/?$', OracleConnections),

    # db mysql mysqldb 16
    (r'/db/mysql/mysqldb-position-connect/?$', MysqldbPositionConnect),
    (r'/db/mysql/mysqldb-keyword-connect/?$', MysqldbKeyworkConnect),
    (r'/db/mysql/mysqldb-pool-connect/?$', MysqldbPoolConnect),
    (r'/db/mysql/mysqldb-insert/?$', MysqldbInsert),
    (r'/db/mysql/mysqldb-delete/?$', MysqldbDelete),
    (r'/db/mysql/mysqldb-update/?$', MysqldbUpdate),
    (r'/db/mysql/mysqldb-select/?$', MysqldbSelect),
    (r'/db/mysql/mysqldb-fetch-one/?$', MysqldbFetchOne),
    (r'/db/mysql/mysqldb-fetch-many/?$', MysqldbFetchMany),
    (r'/db/mysql/mysqldb-fetch-all/?$', MysqldbFetchAll),
    (r'/db/mysql/mysqldb-execute-many/?$', MysqldbExecuteMany),
    (r'/db/mysql/mysqldb-table-error/?$', MysqldbTableError),
    (r'/db/mysql/mysqldb-field-error/?$', MysqldbFieldError),
    (r'/db/mysql/mysqldb-syntax-error/?$', MysqldbSyntaxError),
    (r'/db/mysql/mysqldb-operates/?$', MysqldbOperates),
    (r'/db/mysql/mysqldb-connections/?$', MysqldbConnections),

    # db mysql pysqldb 17
    (r'/db/mysql/pymysql-no-port-connect/?$', PymysqlNoPortConnect),
    (r'/db/mysql/pymysql-dict-connect/?$', PymysqlDictConnect),
    (r'/db/mysql/pymysql-position-connect/?$', PymysqlPositionConnect),
    (r'/db/mysql/pymysql-keyword-connect/?$', PymysqlKeywordConnect),
    (r'/db/mysql/pymysql-insert/?$', PymysqlInsert),
    (r'/db/mysql/pymysql-delete/?$', PymysqlDelete),
    (r'/db/mysql/pymysql-update/?$', PymysqlUpdate),
    (r'/db/mysql/pymysql-select/?$', PymysqlSelect),
    (r'/db/mysql/pymysql-fetch-one/?$', PymysqlFetchOne),
    (r'/db/mysql/pymysql-fetch-many/?$', PymysqlFetchMany),
    (r'/db/mysql/pymysql-fetch-all/?$', PymysqlFetchAll),
    (r'/db/mysql/pymysql-execute-many/?$', PymysqlExecuteMany),
    (r'/db/mysql/pymysql-table-error/?$', PymysqlTableError),
    (r'/db/mysql/pymysql-field-error/?$', PymysqlFieldError),
    (r'/db/mysql/pymysql-syntax-error/?$', PymysqlSyntaxError),
    (r'/db/mysql/pymysql-operates/?$', PymysqlOperates),
    (r'/db/mysql/pymysql-connections/?$', PymysqlConnections),

    # db mysql oursql 12
    (r'/db/mysql/oursql-keyword-connect/?$', OursqlKeywordConnect),
    (r'/db/mysql/oursql-position-connect/?$', OursqlPositionConnect),
    (r'/db/mysql/oursql-no-port-connect/?$', OursqlNoPortConnect),
    (r'/db/mysql/oursql-insert/?$', OursqlInsert),
    (r'/db/mysql/oursql-delete/?$', OursqlDelete),
    (r'/db/mysql/oursql-update/?$', OursqlUpdate),
    (r'/db/mysql/oursql-select/?$', OursqlSelect),
    (r'/db/mysql/oursql-fetch-one/?$', OursqlFetchOne),
    (r'/db/mysql/oursql-fetch-many/?$', OursqlFetchMany),
    (r'/db/mysql/oursql-fetch-all/?$', OursqlFetchAll),
    (r'/db/mysql/oursql-operates/?$', OursqlOperates),
    (r'/db/mysql/oursql-connections/?$', OursqlConnections),

    # db mongodb pymongo 7
    (r'/db/mongodb/insert/?$', MongodbInsert),
    (r'/db/mongodb/delete/?$', MongodbDelete),
    (r'/db/mongodb/update/?$', MongodbUpdate),
    (r'/db/mongodb/select/?$', MongodbSelect),
    (r'/db/mongodb/conn/connection/?$', MongodbConnClass),
    (r'/db/mongodb/conn/mongoclient/params/?$', MongodbConnParams),
    (r'/db/mongodb/conn/mongoclient/str/?$', MongodbConnStr),

    # db postgresql psycopg2 20
    (r'/db/postgresql/psycopg2-parameters-connect/?$', Psycopg2ParametersConnect),
    (r'/db/postgresql/psycopg2-keyword-database-connect/?$', Psycopg2BaseDataConnect),
    (r'/db/postgresql/psycopg2-uri-connect/?$', Psycopg2UriConnect),
    (r'/db/postgresql/psycopg2-uri-no-port-connect/?$', Psycopg2UriNoPortConnect),
    (r'/db/postgresql/psycopg2-connectstring-no-port-connect/?$', Psycopg2ConnectStringNoPort),
    (r'/db/postgresql/psycopg2-connectstring-connect/?$', Psycopg2DBNameUserConnect),
    (r'/db/postgresql/psycopg2-keyword-dbname-connect/?$', Psycopg2DBNameConnect),
    (r'/db/postgresql/psycopg2-no-port-connect/?$', Psycopg2NoPortConnect),
    (r'/db/postgresql/psycopg2-insert/?$', Psycopg2Insert),
    (r'/db/postgresql/psycopg2-update/?$', Psycopg2Update),
    (r'/db/postgresql/psycopg2-select/?$', Psycopg2Select),
    (r'/db/postgresql/psycopg2-delete/?$', Psycopg2Delete),
    (r'/db/postgresql/psycopg2-connection-pool/?$', Psycopg2ConnectionPool),
    (r'/db/postgresql/psycopg2-timeout-error/?$', Psycopg2TimeoutError),
    (r'/db/postgresql/psycopg2-timeout-ok/?$', Psycopg2TimeoutOk),
    (r'/db/postgresql/psycopg2-table-error/?$', Psycopg2TableError),
    (r'/db/postgresql/psycopg2-field-error/?$', Psycopg2FieldError),
    (r'/db/postgresql/psycopg2-syntax-error/?$', Psycopg2SyntaxError),
    (r'/db/postgresql/psycopg2-operates/?$', Psycopg2Operates),
    (r'/db/postgresql/psycopg2-connections/?$', Psycopg2Connections),

    # db postgresql psycopg2ct 18
    (r'/db/postgresql/psycopg2ct-parameters-connect/?$', Psycopg2ctParametersConnect),
    (r'/db/postgresql/psycopg2ct-keyword-database-connect/?$', Psycopg2ctBaseDataConnect),
    (r'/db/postgresql/psycopg2ct-uri-connect/?$', Psycopg2ctUriConnect),
    (r'/db/postgresql/psycopg2ct-uri-no-port-connect/?$', Psycopg2ctUriNoPortConnect),
    (r'/db/postgresql/psycopg2ct-connectstring-no-port-connect/?$', Psycopg2ctConnectStringNoPort),
    (r'/db/postgresql/psycopg2ct-connectstring-connect/?$', Psycopg2ctDBNameUserConnect),
    (r'/db/postgresql/psycopg2ct-keyword-dbname-connect/?$', Psycopg2ctDBNameConnect),
    (r'/db/postgresql/psycopg2ct-no-port-connect/?$', Psycopg2ctNoPortConnect),
    (r'/db/postgresql/psycopg2ct-insert/?$', Psycopg2ctInsert),
    (r'/db/postgresql/psycopg2ct-update/?$', Psycopg2ctUpdate),
    (r'/db/postgresql/psycopg2ct-select/?$', Psycopg2ctSelect),
    (r'/db/postgresql/psycopg2ct-delete/?$', Psycopg2ctDelete),
    (r'/db/postgresql/psycopg2ct-connection-pool/?$', Psycopg2ctConnectionPool),
    (r'/db/postgresql/psycopg2ct-timeout-error/?$', Psycopg2ctTimeoutError),
    (r'/db/postgresql/psycopg2ct-timeout-ok/?$', Psycopg2ctTimeoutOk),
    (r'/db/postgresql/psycopg2ct-table-error/?$', Psycopg2ctTableError),
    (r'/db/postgresql/psycopg2ct-field-error/?$', Psycopg2ctFieldError),
    (r'/db/postgresql/psycopg2ct-syntax-error/?$', Psycopg2ctSyntaxError),

    # db postgresql psycopg2cffi 16
    (r'/db/postgresql/psycopg2cffi-parameters-connect/?$', Psycopg2cffiParametersConnect),
    (r'/db/postgresql/psycopg2cffi-keyword-database-connect/?$', Psycopg2cffiBaseDataConnect),
    (r'/db/postgresql/psycopg2cffi-uri-connect/?$', Psycopg2cffiUriConnect),
    (r'/db/postgresql/psycopg2cffi-uri-no-port-connect/?$', Psycopg2cffiUriNoPortConnect),
    (r'/db/postgresql/psycopg2cffi-connectstring-no-port-connect/?$', Psycopg2cffiConnecStringNoPort),
    (r'/db/postgresql/psycopg2cffi-connectstring-connect/?$', Psycopg2cffiDBNameUserConnect),
    (r'/db/postgresql/psycopg2cffi-keyword-dbname-connect/?$', Psycopg2cffiDBNameConnect),
    (r'/db/postgresql/psycopg2cffi-no-port-connect/?$', Psycopg2cffiNoPortConnect),
    (r'/db/postgresql/psycopg2cffi-insert/?$', Psycopg2cffiInsert),
    (r'/db/postgresql/psycopg2cffi-update/?$', Psycopg2cffiUpdate),
    (r'/db/postgresql/psycopg2cffi-select/?$', Psycopg2cffiSelect),
    (r'/db/postgresql/psycopg2cffi-delete/?$', Psycopg2cffiDelete),
    (r'/db/postgresql/psycopg2cffi-connection-pool/?$', Psycopg2cffiConnectionPool),
    (r'/db/postgresql/psycopg2cffi-table-error/?$', Psycopg2cffiTableError),
    (r'/db/postgresql/psycopg2cffi-field-error/?$', Psycopg2cffiFieldError),
    (r'/db/postgresql/psycopg2cffi-syntax-error/?$', Psycopg2cffiSyntaxError),

    # db redis 16
    (r'/db/redis/set/?$', RedisSet),
    (r'/db/redis/get/?$', RedisGet),
    (r'/db/redis/hset/?$', RedisHSet),
    (r'/db/redis/hget/?$', RedisHGet),
    (r'/db/redis/hgetall/?$', RedisHGetAll),
    (r'/db/redis/rpush/?$', RedisRPush),
    (r'/db/redis/lpop/?$', RedisLPop),
    (r'/db/redis/lrange/?$', RedisLRange),
    (r'/db/redis/sadd/?$', RedisSAdd),
    (r'/db/redis/srem/?$', RedisSRem),
    (r'/db/redis/smembers/?$', RedisSMembers),
    (r'/db/redis/zadd/?$', RedisZAdd),
    (r'/db/redis/zrange/?$', RedisZRange),
    (r'/db/redis/conn/default/?$', RedisConnByRedis),
    (r'/db/redis/conn/strictredis/?$', RedisConnByStrictredis),
    (r'/db/redis/conn/pool/?$', RedisConnPool),

    # db memcached 21
    (r'/db/memcache/memcache-set/?$', MemcacheSet),
    (r'/db/memcache/memcache-set-multi/?$', MemcacheSetMulti),
    (r'/db/memcache/memcache-get/?$', MemcacheGet),
    (r'/db/memcache/memcache-get-multi/?$', MemcacheGetMulti),
    (r'/db/memcache/memcache-delete/?$', MemcacheDelete),
    (r'/db/memcache/memcache-delete-multi/?$', MemcacheDeleteMulti),
    (r'/db/memcache/conn/default/?$', MemcacheConnDefault),

    (r'/db/memcache/pymemcache-set-multi/?$', PymemcacheSetMulti),
    (r'/db/memcache/pymemcache-get/?$', PymemcacheGet),
    (r'/db/memcache/pymemcache-get-multi/?$', PymemcacheGetMulti),
    (r'/db/memcache/pymemcache-delete/?$', PymemcacheDelete),
    (r'/db/memcache/pymemcache-delete-multi/?$', PymemcacheDeleteMulti),
    (r'/db/memcache/pymemcache/conn/client/?$', PymemcacheConnByClient),
    (r'/db/memcache/pymemcache/conn/hashclient/?$', PymemcacheConnByHashClient),

    (r'/db/memcache/bmemcached-set/?$', BMemcachedSet),
    (r'/db/memcache/bmemcached-set-multi/?$', BMemcachedSetMulti),
    (r'/db/memcache/bmemcached-get/?$', BMemcachedGet),
    (r'/db/memcache/bmemcached-get-multi/?$', BMemcachedGetMulti),
    (r'/db/memcache/bmemcached-delete/?$', BMemcachedDelete),
    (r'/db/memcache/bmemcached-delete-multi/?$', BMemcachedDeleteMulti),
    (r'/db/memcache/bmemcached/conn/default/?$', BMemcachedConnDefault),

    # external httplib2
    (r'/httplib2/get/?$', Httplib2Get),
    (r'/httplib2/post/?$', Httplib2Post),
    (r'/httplib2/error/(.*)/?$', Httplib2Error),

    # external requests
    (r'/requests/get/?$', RequestsGet),
    (r'/external/requests/get/?$', ExternalRequestsGet),
    (r'/requests/post/?$', RequestsPost),
    (r'/external/requests/post/?$', ExternalRequestsPost),
    (r'/requests/error/(.*)/?$', RequestsError),

    # external urllib
    (r'/urllib/get/?$', UrllibGet),
    (r'/urllib/post/?$', UrllibPost),
    (r'/urllib/urlencode/?$', UrllibUrlencode),

    # external urllib2
    (r'/urllib2/get/?$', Urllib2Get),
    (r'/urllib2/post/?$', Urllib2Post),
    (r'/urllib2/cookie/?$', Urllib2Cookie),

    # external urllib3
    (r'/urllib3/get/?$', Urllib3Get),
    (r'/urllib3/post/?$', Urllib3Post),
    (r'/urllib3/error/(.*)/?$', Urllib3Error),

    # block code
    (r"/resp_200/?$", Resp200),
    (r"/resp_500/?$", Resp500),
    (r"/resp_json/?$", RespJson),
    (r"/no_html_start/?$", NoHtmlStart),
    (r"/no_html_end/?$", NoHtmlEnd),
    (r"/no_head_start/?$", NoHeadStart),
    (r"/no_head_end/?$", NoHeadEnd),
    (r"/no_title_start/?$", NoTitleStart),
    (r"/no_title_end/?$", NoTitleEnd),
    (r"/no_head_start_title_start/?$", NoHeadStartTitleStart),
    (r"/no_head_start_title_end/?$", NoHeadStartTitleEnd),
    (r"/no_head/?$", NoHead),
    (r"/no_title/?$", NoTitle),
    (r"/no_head_end_title_start/?$", NoHeadEndTitleStart),
    (r"/no_head_end_title_end/?$", NoHeadEndTitleEnd),
    (r"/no_head_start_title/?$", NoHeadStartTitle),
    (r"/no_head_title_start/?$", NoHeadTitleStart),
    (r"/no_head_end_title/?$", NoHeadEndTitle),
    (r"/html_start_has_attr/?$", HtmlStartHasAttr),
    (r"/html_end_has_attr/?$", HtmlEndHasAttr),
    (r"/html_has_attr_lang_en/?$", HtmlHasAttrLangEN),
    (r"/html_has_attr_lang_zh/?$", HtmlHasAttrLangZH),
    (r"/head_start_has_attr/?$", HeadStartHasAttr),
    (r"/head_end_has_attr/?$", HeadEndHasAttr),
    (r"/title_start_has_attr/?$", TitleStartHasAttr),
    (r"/title_end_has_attr/?$", TitleEndHasAttr),
    (r"/head_start_title_start_has_attr/?$", HeadStartTitleStartHasAttr),
    (r"/head_start_title_end_has_attr/?$", HeadStartTitleEndHasAttr),
    (r"/head_end_title_start_has_attr/?$", HeadEndTitleStartHasAttr),
    (r"/head_end_title_end_has_attr/?$", HeadEndTitleEndHasAttr),
    (r"/befor_head_start_has_head_note/?$", BeforHeadStartHasHeadNote),
    (r"/befor_title_start_has_head_note/?$", BeforTitleStartHasHeadNote),
    (r"/befor_title_end_has_head_note/?$", BeforTitleEndHasHeadNote),
    (r"/befor_head_end_has_head_note/?$", BeforHeadEndHasHeadNote),
    (r"/after_head_end_has_head_note/?$", AfterHeadEndHasHeadNote),
    (r"/befor_head_start_has_title_note/?$", BeforHeadStartHasTitleNote),
    (r"/befor_title_start_has_title_note/?$", BeforTitleStartHasTitleNote),
    (r"/befor_title_end_has_title_note/?$", BeforTitleEndHasTitleNote),
    (r"/befor_head_end_has_title_note/?$", BeforHeadEndHasTitleNote),
    (r"/after_head_end_has_title_note/?$", AfterHeadEndHasTitleNote),
    (r"/title_has_special_char/?$", TitleHasSpecialChar),
    (r"/head_has_special_char/?$", HeadHasSpecialChar),
    (r"/html_has_special_char/?$", HtmlHasSpecialChar),
    (r"/size_gt_64k/?$", SizeGt64k),

    # mq
    (r"/rabbitmq/producer/select-connect/?", RabbitmqAsynConnection),
    (r"/rabbitmq/producer/asyn-connect/?", RabbitmqAsynConnection),
]