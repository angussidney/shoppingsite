# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-27 07:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shoppingapp', '0009_auto_20161123_2153'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='ingredients',
            field=models.TextField(default=b'Insert ingredients here'),
        ),
    ]
