# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-29 18:02
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0004_auto_20170326_1334'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='casa',
            options={'ordering': ['nome']},
        ),
        migrations.AlterModelOptions(
            name='prodotto',
            options={'ordering': ['nome']},
        ),
        migrations.RemoveField(
            model_name='prodotto',
            name='data_rilascio',
        ),
        migrations.AddField(
            model_name='casa',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='casa',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='prodotto',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='prodotto',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='casa',
            name='about',
            field=models.TextField(blank=True, max_length=400, null=True),
        ),
        migrations.AlterField(
            model_name='prodotto',
            name='dettagli',
            field=models.TextField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='prodotto',
            name='immagine',
            field=models.FileField(blank=True, null=True, upload_to=b''),
        ),
    ]
