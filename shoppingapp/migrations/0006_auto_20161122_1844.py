# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-22 07:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shoppingapp', '0005_auto_20161122_1843'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='special',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=3),
        ),
    ]
