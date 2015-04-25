# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('asteroid', '0018_auto_20150420_1448'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='release',
        ),
    ]
