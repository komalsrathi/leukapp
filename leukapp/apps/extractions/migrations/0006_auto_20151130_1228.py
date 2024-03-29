# -*- coding: utf-8 -*-
# Generated by Django 1.9b1 on 2015-11-30 17:28
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models
import leukapp.apps.core.db


class Migration(migrations.Migration):

    dependencies = [
        ('extractions', '0005_auto_20151130_1202'),
    ]

    operations = [
        migrations.AlterField(
            model_name='extraction',
            name='ext_id',
            field=leukapp.apps.core.db.CharNullField(default='UNKNOWN', help_text='The sequencing center ID.', max_length=100, null=True, validators=[django.core.validators.RegexValidator(code='invalid', message="Enter a valid 'External id' consisting of letters, numbers, underscores or hyphens.", regex='^[-a-zA-Z0-9_.]+\\Z')], verbose_name='sequencing center ID'),
        ),
        migrations.AlterField(
            model_name='extraction',
            name='int_id',
            field=models.CharField(editable=False, max_length=100, null=True, verbose_name='internal ID'),
        ),
    ]
