# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-03-12 09:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('giveinfo', '0012_auto_20160309_2131'),
    ]

    operations = [
        migrations.AddField(
            model_name='articletext',
            name='sub_text',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='experiencetext',
            name='sub_text',
            field=models.CharField(default='', max_length=200),
        ),
    ]
