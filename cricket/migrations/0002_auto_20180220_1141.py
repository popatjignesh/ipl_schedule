# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cricket', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='favourite',
            name='teams',
            field=models.ManyToManyField(to=b'cricket.Team', null=True, blank=True),
        ),
    ]
