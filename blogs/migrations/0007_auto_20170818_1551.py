# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-18 09:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0006_auto_20170818_1216'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='down_votes',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='blog',
            name='up_votes',
            field=models.IntegerField(default=0),
        ),
    ]