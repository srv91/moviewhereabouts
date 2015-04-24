# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cast',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('actor', models.CharField(max_length=200)),
                ('character', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.IntegerField(default=0, serialize=False, primary_key=True)),
                ('imdb_id', models.CharField(default=b'', max_length=25)),
                ('tmdb_id', models.CharField(default=b'', max_length=25)),
                ('title', models.CharField(max_length=100)),
                ('movie_synopsis', models.CharField(max_length=1800)),
                ('critics_score', models.IntegerField(default=0)),
                ('votes', models.IntegerField(default=10)),
                ('img', models.CharField(default=b'Image unavailable', max_length=50)),
                ('s_img', models.CharField(default=b'', max_length=70)),
                ('l_img', models.CharField(default=b'', max_length=70)),
                ('category', models.CharField(max_length=20)),
                ('genre', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('username', models.CharField(max_length=40)),
                ('user_fav', models.CommaSeparatedIntegerField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='cast',
            name='movie',
            field=models.ForeignKey(to='asteroid.Movie', unique=True),
        ),
    ]
