# Generated by Django 2.0.1 on 2018-01-26 14:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('MyBlog', '0021_auto_20180126_1258'),
    ]

    operations = [
        migrations.CreateModel(
            name='dairy1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('diary_txt1', models.CharField(default='hllo', max_length=100)),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MyBlog.superuser')),
            ],
        ),
        migrations.CreateModel(
            name='dairy2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('diary_txt2', models.CharField(default='hllo', max_length=100)),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MyBlog.superuser')),
            ],
        ),
        migrations.CreateModel(
            name='dairy3',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('diary_txt3', models.CharField(default='hllo', max_length=100)),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MyBlog.superuser')),
            ],
        ),
        migrations.CreateModel(
            name='dairy4',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('diary_txt4', models.CharField(default='hllo', max_length=100)),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MyBlog.superuser')),
            ],
        ),
    ]
