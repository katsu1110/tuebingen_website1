# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-12 12:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('giveinfo', '0019_delete_imageupload'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='tag',
            field=models.CharField(default='生活全般', max_length=100),
        ),
        migrations.AddField(
            model_name='articletext',
            name='tag',
            field=models.CharField(default='生活全般', max_length=100),
        ),
        migrations.AddField(
            model_name='experience',
            name='tag',
            field=models.CharField(default='管理人', max_length=100),
        ),
        migrations.AddField(
            model_name='experiencetext',
            name='tag',
            field=models.CharField(default='管理人', max_length=100),
        ),
    ]
