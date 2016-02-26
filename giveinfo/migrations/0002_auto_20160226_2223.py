# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-26 21:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('giveinfo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='main_text',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='article',
            name='pub_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='experience',
            name='main_text',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='experience',
            name='pub_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='summary',
            name='main_text',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='summary',
            name='pub_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
