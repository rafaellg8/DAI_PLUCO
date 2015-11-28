# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('idComment', models.IntegerField()),
                ('title', models.CharField(unique=True, max_length=128)),
                ('commentText', models.CharField(max_length=500)),
                ('url', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Forum',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(unique=True, max_length=128)),
                ('theme', models.CharField(unique=True, max_length=50)),
                ('asignature', models.CharField(unique=True, max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('userName', models.CharField(unique=True, max_length=25)),
                ('name', models.CharField(max_length=25)),
                ('firstName', models.CharField(max_length=25)),
                ('secondName', models.CharField(max_length=25)),
                ('birthday', models.DateField()),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=25)),
            ],
        ),
        migrations.AddField(
            model_name='comment',
            name='theme',
            field=models.ForeignKey(to='plucoApp.Forum'),
        ),
        migrations.AddField(
            model_name='comment',
            name='userName',
            field=models.ForeignKey(to='plucoApp.User'),
        ),
    ]
