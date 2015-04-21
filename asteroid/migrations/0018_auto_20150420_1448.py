# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('asteroid', '0017_auto_20150419_1849'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='movie_synopsis',
            field=models.CharField(max_length=1800),
            preserve_default=True,
        ),
    ]
