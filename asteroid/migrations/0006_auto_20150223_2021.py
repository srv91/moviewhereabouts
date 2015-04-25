# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('asteroid', '0005_auto_20150223_1423'),
    ]

    operations = [
        migrations.RenameField(
            model_name='movie',
            old_name='critics_consesus',
            new_name='critics_consensus',
        ),
    ]
