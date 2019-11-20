# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-10-09 12:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0015_product_published'),
        ('cart', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='item',
            options={'ordering': ('cart', 'object_id'), 'verbose_name': 'item', 'verbose_name_plural': 'items'},
        ),
        migrations.AddField(
            model_name='item',
            name='selected_color',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='products.Color'),
        ),
        migrations.AddField(
            model_name='item',
            name='selected_size',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='products.Size'),
        ),
    ]
