# Generated by Django 2.0.1 on 2018-01-30 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyBlog', '0029_auto_20180130_1514'),
    ]

    operations = [
        migrations.AddField(
            model_name='diary',
            name='url_slug',
            field=models.SlugField(default=0),
        ),
    ]
