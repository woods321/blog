# Generated by Django 2.0.1 on 2018-01-30 13:56

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('MyBlog', '0026_auto_20180130_1353'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment2',
            name='comment',
            field=tinymce.models.HTMLField(default='hllo', max_length=100),
        ),
        migrations.AlterField(
            model_name='diary1',
            name='diary_txt',
            field=tinymce.models.HTMLField(default='hllo', max_length=100),
        ),
        migrations.AlterField(
            model_name='diary2',
            name='diary_txt',
            field=tinymce.models.HTMLField(default='hllo', max_length=100),
        ),
        migrations.AlterField(
            model_name='diary4',
            name='diary_txt',
            field=tinymce.models.HTMLField(default='hllo', max_length=100),
        ),
    ]
