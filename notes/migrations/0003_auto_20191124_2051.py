# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-11-24 15:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0002_auto_20191124_2013'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='content',
            field=models.TextField(),
        ),
    ]
