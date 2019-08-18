# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Favourite',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
            options={
                'verbose_name': 'Favourite',
                'verbose_name_plural': 'Favourite',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Match',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateField()),
                ('time', models.TimeField()),
            ],
            options={
                'verbose_name': 'Match',
                'verbose_name_plural': 'Match',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'Team',
                'verbose_name_plural': 'Team',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Venue',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('stadium_name', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=70)),
                ('capacity', models.IntegerField()),
                ('image', models.ImageField(null=True, upload_to=b'venue_images/', blank=True)),
            ],
            options={
                'verbose_name': 'Stadium Name',
                'verbose_name_plural': 'Stadium Name',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='match',
            name='away_team',
            field=models.ForeignKey(related_name=b'awayteams', to='cricket.Team'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='match',
            name='home_team',
            field=models.ForeignKey(related_name=b'hometeams', to='cricket.Team'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='match',
            name='venue',
            field=models.ForeignKey(related_name=b'venues', to='cricket.Venue'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='favourite',
            name='teams',
            field=models.ManyToManyField(to='cricket.Team'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='favourite',
            name='user',
            field=models.ForeignKey(related_name=b'users', to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]
