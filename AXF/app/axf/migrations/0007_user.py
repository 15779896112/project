# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2019-03-09 01:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('axf', '0006_auto_20190307_1152'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20, unique=True)),
                ('password', models.CharField(max_length=256)),
                ('name', models.CharField(max_length=20)),
                ('tel', models.CharField(max_length=20)),
                ('add', models.CharField(max_length=100)),
                ('img', models.CharField(max_length=100)),
            ],
        ),
    ]
