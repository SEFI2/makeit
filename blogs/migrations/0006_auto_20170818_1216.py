# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-18 06:16
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0005_blogcomment'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blogcomment',
            options={'ordering': ('-date',), 'verbose_name': 'Blog Comment', 'verbose_name_plural': 'Blog Comments'},
        ),
    ]