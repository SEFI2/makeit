# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-21 03:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0006_auto_20170821_0947'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=models.FileField(default='/no_image.png', upload_to=''),
        ),
    ]