# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-12-08 14:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyBlog', '0018_auto_20171206_1458'),
    ]

    operations = [
        migrations.AlterField(
            model_name='img',
            name='img',
            field=models.FileField(default='touxiang/5.jpg', null=True, upload_to='upload/'),
        ),
    ]
