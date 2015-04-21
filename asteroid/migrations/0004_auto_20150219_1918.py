# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('asteroid', '0003_auto_20150216_1914'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='movie_synopsis',
            field=models.CharField(max_length=900),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='user',
            name='user_fav',
            field=models.CommaSeparatedIntegerField(max_length=50),
            preserve_default=True,
        ),
    ]
