# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-12-06 14:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyBlog', '0017_auto_20171206_1454'),
    ]

    operations = [
        migrations.AlterField(
            model_name='superuser',
            name='touxiang',
            field=models.FileField(default='touxiang/5.jpg', upload_to='touxiang/'),
        ),
    ]