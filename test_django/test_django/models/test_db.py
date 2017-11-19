# -*- coding: utf-8 -*-

__all__ = ["MysqlOperate"]
from django.db import models


class DjangoOrmTest(models.Model):
    """
    MySQL
    """
    name = models.CharField(u"你的名字", max_length=50)
    address = models.CharField(u"你的地址", max_length=50, null=True)
    school = models.CharField(u"你的学校", max_length=50)
    grade = models.IntegerField(u"你的成绩", max_length=11)

    class Meta:
        db_table = "django_orm_test"
        verbose_name = u"测试Django框架的ORM"
        app_label = "mysql_mysqldb"

    # def __unicode__(self):
    #     return "%s" % self.name







