# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('asteroid', '0002_auto_20150212_1459'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vote',
            name='movie',
            field=models.ForeignKey(to='asteroid.Movie', unique=True),
            preserve_default=True,
        ),
    ]
