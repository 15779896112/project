# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2019-03-09 07:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('axf', '0009_user_ss'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='img',
            field=models.CharField(default='1552114651.7579901QQ图片20180807200333.jpg', max_length=100),
        ),
    ]