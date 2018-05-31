from django.db import models
from datetime import datetime


class Table(models.Model):
    table_size = models.CharField(verbose_name=u"桌子尺寸", choices=(('S', '小桌'), ('M', '中桌'), ('L', '大桌')), max_length=2)
    seat_num = models.IntegerField(verbose_name=u"座位数", default=0)

    class Meta:
        verbose_name = u"餐桌"
        verbose_name_plural = verbose_name

    def __str__(self):
        return str(self.id)

class Customer(models.Model):
    name = models.CharField(verbose_name=u"顾客姓名", max_length=30)
    phone = models.CharField(max_length=11, null=True, blank=True)

    class Meta:
        verbose_name = u"顾客"
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.name

class WalkIn(models.Model):
    name = models.CharField(verbose_name=u"顾客姓名", max_length=30)
    phone = models.CharField(max_length=11, null=True, blank=True)
    people_num = models.IntegerField(verbose_name=u"就餐人数", default=1)
    table = models.ForeignKey(Table, verbose_name=u"桌号")
    day = models.CharField(verbose_name=u"到达日期", default=datetime.now, max_length=100)
    date = models.CharField(verbose_name=u"达到时间", max_length=20,
                            choices=(("0", "18:00"), ("1", "18:30"),
                                     ("2", "19:00"), ("3", "19:30"),
                                     ("4", "20:00"), ("5", "20:30"),
                                     ("6", "21:00"), ("7", "21:30"),
                                     ("8", "22:00"), ("9", "22:30"),
                                     ("10", "23:00"), ("11", "23:30")))
    time = models.CharField(verbose_name=u"用餐时长", max_length=10,
                            choices=(("1", "0.5"), ("2", "1"),
                                     ("3", "1.5"), ("4", "2"),
                                     ("5", "2.5"), ("6", "3"),
                                     ("7", "3.5"), ("8", "4")), default="1")
    class Meta:
        verbose_name = u"就餐"
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.name

class Reservation(models.Model):
    name = models.ForeignKey(Customer, verbose_name=u"顾客")
    people_num = models.IntegerField(verbose_name=u"就餐人数", default=1)
    table = models.ForeignKey(Table, verbose_name=u"桌号")
    day = models.CharField(verbose_name=u"到达日期", default=datetime.now, max_length=100)
    date = models.CharField(verbose_name=u"达到时间", max_length=20,
                            choices=(("0", "18:00"), ("1", "18:30"),
                                     ("2", "19:00"), ("3", "19:30"),
                                     ("4", "20:00"), ("5", "20:30"),
                                     ("6", "21:00"), ("7", "21:30"),
                                     ("8", "22:00"), ("9", "22:30"),
                                     ("10", "23:00"), ("11", "23:30")))
    time = models.CharField(verbose_name=u"用餐时长", max_length=10,
                            choices=(("1", "0.5"), ("2", "1"),
                                     ("3", "1.5"), ("4", "2"),
                                     ("5", "2.5"), ("6", "3"),
                                     ("7", "3.5"), ("8", "4")), default="1")

    class Meta:
        verbose_name = u"预约"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name.name

