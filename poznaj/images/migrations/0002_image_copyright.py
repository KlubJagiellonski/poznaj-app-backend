# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-14 12:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='copyright',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]