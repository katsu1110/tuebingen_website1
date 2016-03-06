# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-03-06 18:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('giveinfo', '0007_auto_20160302_2054'),
    ]

    operations = [
        migrations.AddField(
            model_name='summary',
            name='pub_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='article',
            name='correspond_img',
            field=models.ImageField(default='', upload_to='static/images/'),
        ),
        migrations.AlterField(
            model_name='summary',
            name='correspond_img',
            field=models.ImageField(default='', upload_to='static/images/'),
        ),
    ]
