# -*- coding: utf-8 -*-
# Generated by Django 1.9b1 on 2015-12-10 15:52
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations
import leukapp.apps.core.db


class Migration(migrations.Migration):

    dependencies = [
        ('workflows', '0003_auto_20151203_1803'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workflow',
            name='ext_id',
            field=leukapp.apps.core.db.CharNullField(blank=True, default='UNKNOWN', max_length=100, null=True, validators=[django.core.validators.RegexValidator(code='invalid', message="Enter a valid 'External id' consisting of letters, numbers, underscores or hyphens.", regex='^[-a-zA-Z0-9_.]+\\Z')], verbose_name='Extraction ID provided by sequencing center.'),
        ),
    ]
