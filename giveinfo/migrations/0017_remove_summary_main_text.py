# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-03-27 16:22
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('giveinfo', '0016_auto_20160312_1638'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='summary',
            name='main_text',
        ),
    ]
