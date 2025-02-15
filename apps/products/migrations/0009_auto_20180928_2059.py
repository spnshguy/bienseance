# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-09-29 00:59
from __future__ import unicode_literals

import autoslug.fields
import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_auto_20180924_1915'),
    ]

    operations = [
        migrations.AddField(
            model_name='magazine',
            name='card_image',
            field=models.ImageField(default='', upload_to='', verbose_name='Card Image'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='magazine',
            name='description',
            field=ckeditor.fields.RichTextField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='magazine',
            name='nb_purchase',
            field=models.PositiveIntegerField(default=0, verbose_name='Number of views'),
        ),
        migrations.AddField(
            model_name='magazine',
            name='price',
            field=models.FloatField(default=0, verbose_name='Price'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='magazine',
            name='product_images',
            field=models.ManyToManyField(to='products.Image'),
        ),
        migrations.AddField(
            model_name='magazine',
            name='slug',
            field=autoslug.fields.AutoSlugField(default='', editable=False, populate_from='title', unique=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='magazine',
            name='tags',
            field=models.ManyToManyField(to='products.Tag', verbose_name='Tags'),
        ),
        migrations.AddField(
            model_name='magazine',
            name='title',
            field=models.CharField(default='', max_length=100, verbose_name='Title'),
            preserve_default=False,
        ),
    ]
