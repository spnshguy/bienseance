# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-10-06 17:50
from __future__ import unicode_literals

import ckeditor.fields
import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0010_remove_product_card_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='short_description',
            field=ckeditor.fields.RichTextField(default='Consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=ckeditor_uploader.fields.RichTextUploadingField(),
        ),
    ]
