# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-23 00:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0002_auto_20160922_1643'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'ordering': ['-pub_date']},
        ),
        migrations.AlterField(
            model_name='article',
            name='pub_date',
            field=models.DateField(auto_now_add=True),
        ),
    ]
