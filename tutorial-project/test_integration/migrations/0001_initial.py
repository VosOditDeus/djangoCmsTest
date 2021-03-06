# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-27 11:53
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
            name='ContainerModel',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='test_integration_containermodel', serialize=False, to='cms.CMSPlugin')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.CreateModel(
            name='EventCardModel',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='test_integration_eventcardmodel', serialize=False, to='cms.CMSPlugin')),
                ('size', models.CharField(choices=[('150', '150x150'), ('300', '300x300'), ('450', '450x450')], default='150', max_length=255, verbose_name='Size')),
                ('title', models.CharField(max_length=2500, verbose_name='Title')),
                ('date', models.DateField(blank=True, null=True, verbose_name='Event Date')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
    ]
