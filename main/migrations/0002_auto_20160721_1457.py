# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-07-21 07:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='device',
            name='stream_url',
            field=models.CharField(max_length=200, verbose_name='URL путь'),
        ),
    ]
