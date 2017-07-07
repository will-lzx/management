from django.db import models

# Create your models here.


class Cabinet(models.Model):
    number = models.CharField(max_length=45, default='')
    spot_id = models.IntegerField()
    two_dimension_code = models.CharField(max_length=254)
    capacity = models.IntegerField()
    status = models.IntegerField()
    lat = models.FloatField(default=None)
    lon = models.FloatField(default=None)


class Pole(models.Model):
    number = models.CharField(max_length=20, default='')
    cabinet_id = models.IntegerField(default=0)
    update_time = models.DateTimeField()
    create_time = models.DateTimeField()


class Customer(models.Model):
    weixin_number = models.CharField(max_length=256)
    mobile_number = models.CharField(max_length=11)
    alipay = models.CharField(max_length=256)
    credit_score = models.FloatField()
    deposit = models.FloatField()
    deposit_status = models.IntegerField()


class Rule(models.Model):
    start_time_long = models.FloatField()
    unit_price = models.FloatField()
    # 0：否 1：是
    is_valid = models.IntegerField()
    create_time = models.DateTimeField()
    modify_time = models.DateTimeField()
    operator = models.CharField(max_length=20)


class Spot(models.Model):
    name = models.CharField(max_length=256)
    province = models.CharField(max_length=20)
    city = models.CharField(max_length=20)
    address = models.CharField(max_length=200)
    responsible_person = models.CharField(max_length=20)
    rule = models.ForeignKey(Rule)


class LendHistory(models.Model):
    pole = models.ForeignKey(Pole)
    mobile_number = models.CharField(max_length=11)
    start_time = models.DateTimeField()
    return_time = models.DateTimeField(default=None)
    rule = models.ForeignKey(Rule)
    money = models.FloatField(default=0)
    status = models.IntegerField(default=0)
