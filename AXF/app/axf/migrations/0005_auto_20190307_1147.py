# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2019-03-07 11:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('axf', '0004_auto_20190307_1145'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goods',
            name='productlongname',
            field=models.CharField(max_length=100),
        ),
    ]
