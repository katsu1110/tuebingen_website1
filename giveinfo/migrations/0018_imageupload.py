# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-09-04 13:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('giveinfo', '0017_remove_summary_main_text'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImageUpload',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('upload', models.ImageField(upload_to='uploads/%Y/%m/%d/')),
            ],
        ),
    ]