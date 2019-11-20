# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-09-18 03:15
from __future__ import unicode_literals

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='slug',
            field=autoslug.fields.AutoSlugField(default='test', editable=False, populate_from='title'),
            preserve_default=False,
        ),
    ]
