# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2018-02-06 21:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('osm_view', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='location',
            name='activity',
        ),
        migrations.AddField(
            model_name='location',
            name='activity',
            field=models.ManyToManyField(to='osm_view.Activity'),
        ),
    ]
