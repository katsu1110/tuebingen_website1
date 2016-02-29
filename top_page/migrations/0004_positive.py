# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-28 17:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('top_page', '0003_auto_20160227_1042'),
    ]

    operations = [
        migrations.CreateModel(
            name='Positive',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jp', models.CharField(default='きっといいことあるよ！', max_length=100)),
                ('de', models.CharField(default='Viel glückwünsche bei dir!', max_length=100)),
                ('en', models.CharField(default='May you have something wonderful!', max_length=100)),
                ('pub_date', models.DateTimeField(blank=True, null=True)),
            ],
        ),
    ]