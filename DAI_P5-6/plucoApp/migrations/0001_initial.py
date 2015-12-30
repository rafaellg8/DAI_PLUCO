# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('idComment', models.IntegerField()),
                ('title', models.CharField(help_text=b'T\xc3\xadtulo del comentario, asunto', unique=True, max_length=128)),
                ('commentText', models.TextField(help_text=b'Introduce aqu\xc3\xad tu comentario', max_length=500)),
                ('date', models.DateField()),
                ('likes', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Forum',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(help_text=b'T\xc3\xadtulo de la hebra o foro nuevo', unique=True, max_length=128)),
                ('theme', models.CharField(help_text=b'Tema', unique=True, max_length=50)),
                ('asignature', models.CharField(help_text=b'asignature', unique=True, max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('email', models.EmailField(help_text=b'direcci\xc3\xb3n email', max_length=30)),
                ('address', models.CharField(help_text=b'direcci\xc3\xb3n postal', max_length=30)),
                ('picture', models.ImageField(upload_to=b'media', blank=True)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='comment',
            name='theme',
            field=models.ForeignKey(to='plucoApp.Forum'),
        ),
        migrations.AddField(
            model_name='comment',
            name='username',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
    ]
