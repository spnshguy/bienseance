# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-10-02 02:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0008_blogimage_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='Is Active'),
        ),
    ]
