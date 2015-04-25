# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('asteroid', '0016_auto_20150419_1449'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='l_img',
            field=models.CharField(default=b'', max_length=70),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='movie',
            name='s_img',
            field=models.CharField(default=b'', max_length=70),
            preserve_default=True,
        ),
    ]
