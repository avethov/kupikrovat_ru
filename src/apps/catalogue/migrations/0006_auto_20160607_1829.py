# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-07 15:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0005_auto_20160607_1737'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='product',
            managers=[
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='price',
            field=models.IntegerField(default=0, verbose_name='Цена'),
        ),
    ]
