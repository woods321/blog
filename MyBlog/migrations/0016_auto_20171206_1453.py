# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-12-06 14:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyBlog', '0015_auto_20171206_1447'),
    ]

    operations = [
        migrations.AlterField(
            model_name='superuser',
            name='touxiang',
            field=models.FileField(blank=True, default='touxiang/5.jpg', null=True, upload_to='touxiang/'),
        ),
    ]
