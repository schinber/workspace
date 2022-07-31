from django.db import models


# Create your models here.


# 图书表
class Book(models.Model):
    title = models.CharField(max_length=255)
    # 书名
    price = models.DecimalField(max_digits=8, decimal_places=2)
    # 价格
    publish_date = models.DateField(auto_now_add=True)
    # 出版时间

    stock = models.IntegerField()
    # 库存
    sales = models.IntegerField()
    # 销售
    publish = models.ForeignKey(to='Publish')  # 默认外键连接出版社的主键ID
    # 出版社
    author = models.ManyToManyField(to="Author")  # 多连接多， 创建一张虚拟字段，自动创建一张虚拟表， 可以帮助orm跨表查询

    # 作者

    def __str__(self):
        return self.title


# 出版社表
class Publish(models.Model):
    # 出版社名字
    name = models.CharField(max_length=32)
    # 出版社地址
    addr = models.CharField(max_length=64)

    def __str__(self):
        return self.name


# 作者
class Author(models.Model):
    # 名字
    name = models.CharField(max_length=32)
    # 年龄
    age = models.IntegerField()
    # 作者详情
    author_detail = models.OneToOneField(to='AuthorDetail')

    def __str__(self):
        return self.name


# 作者详情
class AuthorDetail(models.Model):
    phone = models.BigIntegerField()
    address = models.CharField(max_length=255)

    def __str__(self):
        return self.address


# ps：设计完所有表进行命令行：
# 1：记录python3 manage.py makemigrations
# 2: 同步数据库： python_study manage.py migrate
# 这样才能创建表
