# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('asteroid', '0008_remove_movie_critics_consensus'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='img',
            field=models.CharField(default='', max_length=20),
            preserve_default=False,
        ),
    ]
