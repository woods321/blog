# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-12-02 12:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyBlog', '0013_auto_20171202_0754'),
    ]

    operations = [
        migrations.AlterField(
            model_name='superuser',
            name='username',
            field=models.CharField(max_length=500),
        ),
    ]
