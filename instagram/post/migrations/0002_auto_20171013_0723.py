# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-13 07:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postcomment',
            name='content',
            field=models.TextField(),
        ),
    ]