# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2019-03-11 08:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('axf', '0010_auto_20190309_0700'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='tel',
            field=models.CharField(default='', max_length=20),
        ),
    ]
