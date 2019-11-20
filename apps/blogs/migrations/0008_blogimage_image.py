# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-09-30 22:23
from __future__ import unicode_literals

import apps.custom_plugins.validation
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0007_auto_20180930_1803'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogimage',
            name='image',
            field=apps.custom_plugins.validation.ValidateImageFile(default='', upload_to=''),
            preserve_default=False,
        ),
    ]
