# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('asteroid', '0004_auto_20150219_1918'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vote',
            name='movie',
        ),
        migrations.DeleteModel(
            name='Vote',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='actor',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='character',
        ),
        migrations.AddField(
            model_name='movie',
            name='critics_consesus',
            field=models.CharField(default='NA', max_length=500),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='movie',
            name='movie_id',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='movie',
            name='votes',
            field=models.IntegerField(default=10),
            preserve_default=True,
        ),
    ]
