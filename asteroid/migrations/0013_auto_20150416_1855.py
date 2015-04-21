# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('asteroid', '0012_auto_20150415_1959'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='imdb_id',
            field=models.CharField(default=0, max_length=25),
            preserve_default=True,
        ),
    ]
