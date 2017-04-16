# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-26 13:32
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='prodotto',
            name='data_rilascio',
            field=models.DateField(default=datetime.date(2017, 3, 26)),
        ),
        migrations.AddField(
            model_name='prodotto',
            name='spedizione_gratuita',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='casa',
            name='about',
            field=models.TextField(max_length=400),
        ),
    ]
