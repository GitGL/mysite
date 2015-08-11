# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ApplyInfos',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('apply_date', models.DateTimeField(verbose_name=b'date apply')),
                ('play_date', models.DateField(verbose_name=b'date play')),
                ('file_path', models.CharField(max_length=300)),
                ('apply_stage', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Areas',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('area_name', models.CharField(max_length=100)),
                ('area_desc', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Employees',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('employee_id', models.CharField(max_length=8)),
                ('employee_name', models.CharField(max_length=50)),
                ('employee_pwd', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='TimeList',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('list_name', models.CharField(max_length=10)),
            ],
        ),
        migrations.AddField(
            model_name='applyinfos',
            name='area_id',
            field=models.ForeignKey(to='broadcast.Areas'),
        ),
        migrations.AddField(
            model_name='applyinfos',
            name='employee_id',
            field=models.ForeignKey(to='broadcast.Employees'),
        ),
        migrations.AddField(
            model_name='applyinfos',
            name='play_time',
            field=models.ForeignKey(to='broadcast.TimeList'),
        ),
    ]
