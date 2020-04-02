from django.db import models

# Create your models here.
'''
定义模型对象
python2 要用pymysql
python3 要用mysqlclient  

创建模型对象
Python manage.py makemigrations
创建表
Python  manage.py migrate
'''


class UserInfo(models.Model):
    # 定义字段
    # 主键
    userId = models.BigAutoField(primary_key=True)
    userAccount = models.CharField(
        max_length=50, unique=True)  # unique=True是唯一的
    userPass = models.CharField(max_length=30)
    userBirth = models.DateTimeField(
        auto_now=True)  # 时间
    userSex = models.CharField(max_length=4)

    class Meta:
        db_table = 'userInfoTable'


class OrderInfo(models.Model):
    orderId = models.CharField(primary_key=True, max_length=100)
    orderDate = models.DateTimeField(
        auto_now=True)  # auto_now=True  添加数据时是默认系统时间
    orderMon = models.DecimalField(max_digits=11, decimal_places=2)
    userInfo = models.ForeignKey(UserInfo, on_delete=models.CASCADE)  # 设置外键关联

    class Meta:
        db_table = 'order_Table'

# 商品模型表


class Product(models.Model):
    productId = models.BigAutoField(primary_key=True)
    productName = models.CharField(max_length=200)
    productPrice = models.DecimalField(max_digits=11, decimal_places=2)
    productImg = models.CharField(max_length=200, null=True)

    class Meta:
        db_table = 'product'

# 用户购物车  多对多关系


class UserGoods(models.Model):
    user = models.ForeignKey(UserInfo, on_delete=models.DO_NOTHING)
    product = models.ForeignKey(Product, on_delete=models.DO_NOTHING)

    class Meta:
        db_table = 'userGoods'
