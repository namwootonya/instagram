# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-13 09:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0003_auto_20171013_0732'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='title',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
