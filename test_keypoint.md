# 探针测试要点

## 基准功能
* 报表所需支持的所有数据展示（少部分不常见的不支持）
```
    基本应用性能数据
    慢过程追踪,以及相关
    吞吐率（主要看数据准确性),重要性： 低
    错误率（主要看数据准确性),重要性： 低
    CPU使用率（主要看数据准确性),重要性： 低
    内存使用量（主要看数据准确性),重要性： 低
```

* 服务器下发配置，以及探针配置
```
    本地配置与服务器冲突的，已服务器为准
    url过滤
    url参数采集
    各种采集阈值等
```


## 外部HTTP调用
* 用户文档里注明的所有外部插件
```
    HTTP调用错误追踪以及归类
    HTTP调用正常功能.
    相关配置
    thrift
```

## 数据库
```
    Oracle调用,增删改
    mysql调用,增删改.
    redis/memcached
    相关配置

    以xiguago为背景(代购网站)
```


## tornado
```
    自定义异步接口,Runner, gen coroutine, on_finish, prepare
    ioloop: _run_callback, handle_callback_exception, add_callback, add_handler
    concurrence
    http client: 异步/非异步
    uwsgi + tornadoApp
    gevent + tornadoApp
    tornadoServer + tornadoApp
    wsgiApp + tornadoServer
```

## 应用要求

```
    代码规范
    url统一, 每个应用,url要一致.
    一个测试点,一个url
```

