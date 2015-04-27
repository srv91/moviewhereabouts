# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('asteroid', '0019_remove_movie_release'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cast',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('actor', models.CharField(max_length=200)),
                ('character', models.CharField(max_length=200)),
                ('movie', models.ForeignKey(to='asteroid.Movie', unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fname', models.CharField(default=b'unknown', max_length=25)),
                ('fmail', models.EmailField(default=b'unknown@unknown.com', max_length=50)),
                ('msg', models.CharField(default=b'no msg', max_length=200)),
            ],
        ),
    ]
