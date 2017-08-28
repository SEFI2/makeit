# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-21 09:35
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0008_blogactivity_blogcommentactivity'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blogactivity',
            options={'verbose_name': 'Blog Activities', 'verbose_name_plural': 'Blog Activity'},
        ),
        migrations.AlterModelOptions(
            name='blogcommentactivity',
            options={'verbose_name': 'Blog Comment Activities', 'verbose_name_plural': 'Blog Comment Activity'},
        ),
        migrations.RenameField(
            model_name='blogcommentactivity',
            old_name='blog',
            new_name='blog_comment',
        ),
        migrations.RemoveField(
            model_name='blog',
            name='down_votes',
        ),
        migrations.RemoveField(
            model_name='blog',
            name='up_votes',
        ),
    ]