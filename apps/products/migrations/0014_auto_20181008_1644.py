# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-10-08 20:44
from __future__ import unicode_literals

import autoslug.fields
import ckeditor.fields
import ckeditor_uploader.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0013_auto_20181008_1640'),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Title')),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='title', unique=True)),
                ('short_description', ckeditor.fields.RichTextField()),
                ('description', ckeditor_uploader.fields.RichTextUploadingField()),
                ('price', models.FloatField(verbose_name='Price')),
                ('nb_purchase', models.PositiveIntegerField(default=0, verbose_name='Number of purchases')),
                ('product_images', models.ManyToManyField(to='products.Image')),
                ('tags', models.ManyToManyField(to='products.Tag', verbose_name='Tags')),
            ],
        ),
        migrations.RemoveField(
            model_name='magazine',
            name='description',
        ),
        migrations.RemoveField(
            model_name='magazine',
            name='id',
        ),
        migrations.RemoveField(
            model_name='magazine',
            name='nb_purchase',
        ),
        migrations.RemoveField(
            model_name='magazine',
            name='price',
        ),
        migrations.RemoveField(
            model_name='magazine',
            name='product_images',
        ),
        migrations.RemoveField(
            model_name='magazine',
            name='short_description',
        ),
        migrations.RemoveField(
            model_name='magazine',
            name='slug',
        ),
        migrations.RemoveField(
            model_name='magazine',
            name='tags',
        ),
        migrations.RemoveField(
            model_name='magazine',
            name='title',
        ),
        migrations.RemoveField(
            model_name='product',
            name='description',
        ),
        migrations.RemoveField(
            model_name='product',
            name='id',
        ),
        migrations.RemoveField(
            model_name='product',
            name='nb_views',
        ),
        migrations.RemoveField(
            model_name='product',
            name='price',
        ),
        migrations.RemoveField(
            model_name='product',
            name='product_images',
        ),
        migrations.RemoveField(
            model_name='product',
            name='short_description',
        ),
        migrations.RemoveField(
            model_name='product',
            name='slug',
        ),
        migrations.RemoveField(
            model_name='product',
            name='tags',
        ),
        migrations.RemoveField(
            model_name='product',
            name='title',
        ),
        migrations.AddField(
            model_name='magazine',
            name='item_ptr',
            field=models.OneToOneField(auto_created=True, default=1, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='products.Item'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='item_ptr',
            field=models.OneToOneField(auto_created=True, default=2, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='products.Item'),
            preserve_default=False,
        ),
    ]
