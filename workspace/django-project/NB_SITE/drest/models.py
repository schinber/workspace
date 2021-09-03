# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

from django.db import models


# Create your models here.
class Test(models.Model):
    # 这些在创建数据表时是表字段，括号内为字段对应属性
    # 不过注意default属性，是说在实例化这个类时该字段默认是这个值，创建数据表时并不会当作一行括入数据表
    created = models.DateTimeField(auto_now_add=True)
    username = models.CharField(max_length=100, default='ls', )
    password = models.CharField(max_length=100, default='toor', )

    class Meta:
        # 这个表示数据表的内容按创建时间排序
        ordering = ('created',)
