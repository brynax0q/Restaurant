# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-05-30 11:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0008_auto_20180530_1121'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='date',
            field=models.CharField(choices=[('18:00', '18:00'), ('18:30', '18:30'), ('17:00', '19:00'), ('19:30', '19:30'), ('20:00', '20:00'), ('20:30', '20:30'), ('21:00', '21:00'), ('21:30', '21:30'), ('22:00', '22:00'), ('22:30', '22:30'), ('23:00', '23:00'), ('23:30', '23:30')], max_length=20, verbose_name='达到时间'),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='time',
            field=models.CharField(choices=[('0.5', '0.5'), ('1', '1'), ('1.5', '1.5'), ('2', '2'), ('2.5', '2.5'), ('3', '3'), ('3.5', '3.5'), ('4', '4')], default='0.5', max_length=10, verbose_name='用餐时长'),
        ),
        migrations.AlterField(
            model_name='walkin',
            name='date',
            field=models.CharField(choices=[('18:00', '18:00'), ('18:30', '18:30'), ('17:00', '19:00'), ('19:30', '19:30'), ('20:00', '20:00'), ('20:30', '20:30'), ('21:00', '21:00'), ('21:30', '21:30'), ('22:00', '22:00'), ('22:30', '22:30'), ('23:00', '23:00'), ('23:30', '23:30')], max_length=20, verbose_name='达到时间'),
        ),
        migrations.AlterField(
            model_name='walkin',
            name='time',
            field=models.CharField(choices=[('0.5', '0.5'), ('1', '1'), ('1.5', '1.5'), ('2', '2'), ('2.5', '2.5'), ('3', '3'), ('3.5', '3.5'), ('4', '4')], default='0.5', max_length=10, verbose_name='用餐时长'),
        ),
    ]
