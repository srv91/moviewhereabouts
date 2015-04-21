# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('asteroid', '0007_auto_20150223_2142'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='critics_consensus',
        ),
    ]
