# -*- coding: utf-8 -*-
# Generated by Django 1.9b1 on 2015-12-21 19:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('individuals', '0006_individual_queries_count'),
    ]

    operations = [
        migrations.AlterField(
            model_name='individual',
            name='institution',
            field=models.CharField(choices=[('MSK', 'MSK'), ('ICO', 'ICO'), ('PV', 'PV'), ('IHBT', 'IHBT'), ('OTHER', 'OTHER')], max_length=100, null=True, verbose_name='institution'),
        ),
    ]
