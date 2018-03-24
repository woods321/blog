# Generated by Django 2.0.1 on 2018-03-08 12:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('MyBlog', '0035_auto_20180130_1745'),
    ]

    operations = [
        migrations.AddField(
            model_name='superuser',
            name='user',
            field=models.OneToOneField(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
