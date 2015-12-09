# -*- coding: utf-8 -*-
# Generated by Django 1.9b1 on 2015-12-09 20:20
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('specimens', '0003_auto_20151130_1556'),
    ]

    operations = [
        migrations.AlterField(
            model_name='specimen',
            name='ext_id',
            field=models.CharField(blank=True, default='UNKNOWN', help_text='The external id should be unique at the Individual and Source type levels.', max_length=100, validators=[django.core.validators.RegexValidator(code='invalid', message="Enter a valid 'External id' consisting of letters, numbers, underscores or hyphens.", regex='^[-a-zA-Z0-9_.]+\\Z')], verbose_name='external id'),
        ),
        migrations.AlterField(
            model_name='specimen',
            name='individual',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='individuals.Individual', verbose_name='individual'),
            preserve_default=False,
        ),
    ]
