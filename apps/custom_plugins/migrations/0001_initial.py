# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-09-04 11:17
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cms', '0020_old_tree_cleanup'),
    ]

    operations = [
        migrations.CreateModel(
            name='SocialNetwork',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='custom_plugins_socialnetwork', serialize=False, to='cms.CMSPlugin')),
                ('social_network', models.IntegerField(choices=[(0, 'Facebook'), (1, 'Instagram'), (2, 'LinkedIn'), (3, 'Twitter')], verbose_name='Social Network')),
                ('url', models.URLField(verbose_name='URL')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
    ]
