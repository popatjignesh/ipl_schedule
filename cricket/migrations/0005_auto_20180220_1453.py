# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cricket', '0004_auto_20180220_1412'),
    ]

    operations = [
        migrations.AlterField(
            model_name='match',
            name='time',
            field=models.CharField(max_length=10, choices=[(b'4', b'4 PM'), (b'8', b'8 PM')]),
        ),
    ]
