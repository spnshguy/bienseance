# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-09-18 01:34
from __future__ import unicode_literals

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Name')),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Title')),
                ('description', ckeditor.fields.RichTextField()),
                ('price', models.FloatField(verbose_name='Price')),
                ('current_stock', models.PositiveIntegerField(default=0, verbose_name='Current Stock')),
                ('card_image', models.ImageField(upload_to='', verbose_name='Card Image')),
            ],
        ),
        migrations.CreateModel(
            name='Size',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Name')),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='available_colors',
            field=models.ManyToManyField(related_name='color_products', to='products.Size', verbose_name='Available colors'),
        ),
        migrations.AddField(
            model_name='product',
            name='available_sizes',
            field=models.ManyToManyField(related_name='size_products', to='products.Size', verbose_name='Available sizes'),
        ),
        migrations.AddField(
            model_name='product',
            name='product_images',
            field=models.ManyToManyField(to='products.Image'),
        ),
    ]
