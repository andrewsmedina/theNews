# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-23 17:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0012_tag_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='promoted',
            field=models.BooleanField(default=False),
        ),
    ]
