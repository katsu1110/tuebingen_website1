# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-03-07 21:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('giveinfo', '0010_auto_20160307_2146'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='img',
            field=models.ImageField(default='', upload_to='images'),
        ),
        migrations.AlterField(
            model_name='summary',
            name='img',
            field=models.ImageField(default='', upload_to='images'),
        ),
    ]
