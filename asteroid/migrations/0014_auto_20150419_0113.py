# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('asteroid', '0013_auto_20150416_1855'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='tmdb_id',
            field=models.CharField(default=b'', max_length=25),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='movie',
            name='imdb_id',
            field=models.CharField(default=b'', max_length=25),
            preserve_default=True,
        ),
    ]
