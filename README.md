# Usage of projects（markdown语法)

## 内网Server信息
* host
```
    192.168.2.110   dc1dev.networkbench.com
    192.168.2.110   dc2dev.networkbench.com
    192.168.2.110   dc3dev.networkbench.com
    192.168.2.110   dc1.networkbench.com
    192.168.2.110   dc2.networkbench.com
    192.168.2.110   redirect.networkbench.com
    192.168.2.110   dcs1dev.networkbench.com
    192.168.2.110   dcs2dev.networkbench.com
    192.168.2.110   dcs1.networkbench.com
```

* 内网报表地址：http://reportlocal.tingyun.com/server/overview/application
* 用户名/密码：sina/1
* 内网测试license-key： 999-999-999

## 数据库
```
    mysql 地址：192.168.2.43，端口默认：3306， 用户：tingyun ， 密码： tingyun，
    redis 地址： 192.168.2.43，端口默认：6379
    memcached：192.168.2.43，端口默认：11211
```

## 测试机器
```
    192.168.2.43 nb/nb, 主要使用docker运行了一些服务，比如thrift、mysql、redis等
    192.168.2.201 nb/nb, 主要用于运行测试应用。包括nginx/apache/等。
```

## 推荐
* <代码整洁之道>
