# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cricket', '0003_auto_20180220_1150'),
    ]

    operations = [
        migrations.AlterField(
            model_name='venue',
            name='stadium_name',
            field=models.CharField(max_length=50, null=True, blank=True),
        ),
    ]
