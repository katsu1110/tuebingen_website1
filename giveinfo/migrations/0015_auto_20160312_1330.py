# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-03-12 12:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('giveinfo', '0014_auto_20160312_1157'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='summary',
            name='img',
        ),
        migrations.AddField(
            model_name='summary',
            name='pic_name',
            field=models.CharField(default='suzu1.jpg', max_length=100),
        ),
    ]
