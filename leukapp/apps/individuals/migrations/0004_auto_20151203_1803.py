# -*- coding: utf-8 -*-
# Generated by Django 1.9b1 on 2015-12-03 23:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('individuals', '0003_auto_20151130_1720'),
    ]

    operations = [
        migrations.AlterField(
            model_name='individual',
            name='species',
            field=models.CharField(choices=[('HUMAN', 'HUMAN'), ('MOUSE', 'MOUSE'), ('YEAST', 'YEAST'), ('ZEBRAFISH', 'ZEBRAFISH')], max_length=100, null=True, verbose_name='species'),
        ),
    ]
