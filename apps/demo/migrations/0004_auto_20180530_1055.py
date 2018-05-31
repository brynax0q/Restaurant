# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-05-30 10:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0003_auto_20180530_1050'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='date',
            field=models.CharField(choices=[('t_18', '18:00'), ('t_1830', '18:30'), ('t_17', '19:00'), ('t_1930', '19:30'), ('t_20', '20:00'), ('t_2030', '20:30'), ('t_21', '21:00'), ('t_2130', '21:30'), ('t_22', '22:00'), ('t_2230', '22:30'), ('t_23', '23:00'), ('t_2330', '23:30')], max_length=20, verbose_name='达到时间'),
        ),
        migrations.AlterField(
            model_name='walkin',
            name='date',
            field=models.CharField(choices=[('t_18', '18:00'), ('t_1830', '18:30'), ('t_17', '19:00'), ('t_1930', '19:30'), ('t_20', '20:00'), ('t_2030', '20:30'), ('t_21', '21:00'), ('t_2130', '21:30'), ('t_22', '22:00'), ('t_2230', '22:30'), ('t_23', '23:00'), ('t_2330', '23:30')], max_length=20, verbose_name='达到时间'),
        ),
    ]
