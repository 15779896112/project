# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2019-03-09 03:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('axf', '0008_auto_20190309_0226'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='ss',
            field=models.CharField(default='1', max_length=10),
        ),
    ]
