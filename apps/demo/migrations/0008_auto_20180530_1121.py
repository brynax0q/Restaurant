# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-05-30 11:21
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0007_auto_20180530_1121'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='day',
            field=models.CharField(default=datetime.datetime.now, max_length=100, verbose_name='到达日期'),
        ),
    ]