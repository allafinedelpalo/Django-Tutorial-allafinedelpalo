# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-26 13:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0003_auto_20170326_1333'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prodotto',
            name='data_rilascio',
            field=models.DateField(auto_now=True),
        ),
    ]
