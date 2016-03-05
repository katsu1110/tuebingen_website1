# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-03-05 18:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Imagepost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=20)),
                ('image', models.ImageField(default='', upload_to='uploads/')),
                ('pub_date', models.DateTimeField(blank=True, null=True)),
                ('writer', models.CharField(default='すずさん', max_length=20)),
            ],
        ),
    ]