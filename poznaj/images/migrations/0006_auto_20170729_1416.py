# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-29 14:16
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0005_auto_20170729_1348'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='point',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='point_images', to='points.Point'),
        ),
        migrations.AlterField(
            model_name='image',
            name='story',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='story_images', to='stories.Story'),
        ),
    ]
