# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-03-09 20:31
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('giveinfo', '0011_auto_20160307_2223'),
    ]

    operations = [
        migrations.CreateModel(
            name='ArticleText',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('main_text', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='ExperienceText',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('main_text', models.TextField()),
            ],
        ),
        migrations.RemoveField(
            model_name='article',
            name='img',
        ),
        migrations.RemoveField(
            model_name='article',
            name='main_text',
        ),
        migrations.RemoveField(
            model_name='experience',
            name='main_text',
        ),
        migrations.AlterField(
            model_name='article',
            name='text_title',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='article',
            name='writer',
            field=models.CharField(default='管理人', max_length=50),
        ),
        migrations.AlterField(
            model_name='experience',
            name='text_title',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='experience',
            name='writer',
            field=models.CharField(default='管理人', max_length=50),
        ),
        migrations.AlterField(
            model_name='link',
            name='link_text',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='link',
            name='link_title',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='link',
            name='urllink',
            field=models.URLField(),
        ),
        migrations.AlterField(
            model_name='summary',
            name='head',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='summary',
            name='main_text',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='summary',
            name='sub_head',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='experiencetext',
            name='experience',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='giveinfo.Experience'),
        ),
        migrations.AddField(
            model_name='articletext',
            name='article',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='giveinfo.Article'),
        ),
    ]
