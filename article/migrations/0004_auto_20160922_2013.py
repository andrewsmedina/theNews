# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-23 00:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0003_auto_20160922_2008'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='slug',
            field=models.CharField(blank=True, max_length=255, null=True, unique_for_date='pub_date'),
        ),
    ]
