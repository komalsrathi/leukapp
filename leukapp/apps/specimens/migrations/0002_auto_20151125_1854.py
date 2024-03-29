# -*- coding: utf-8 -*-
# Generated by Django 1.9b1 on 2015-11-25 23:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('specimens', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='specimen',
            name='source',
            field=models.CharField(blank=True, choices=[('BLOOD', 'BLOOD'), ('NAILS', 'NAILS'), ('BUCCAL', 'BUCCAL'), ('HAIR', 'HAIR'), ('TCELLS', 'TCELLS')], max_length=100, null=True, verbose_name='source'),
        ),
        migrations.AlterField(
            model_name='specimen',
            name='source_type',
            field=models.CharField(choices=[('TUMOR', 'TUMOR'), ('NORMAL', 'NORMAL')], max_length=100, null=True, verbose_name='source_type'),
        ),
    ]
