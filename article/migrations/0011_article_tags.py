# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-23 15:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0010_remove_tag_articles'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='tags',
            field=models.ManyToManyField(to='article.Tag'),
        ),
    ]
