# -*- coding: utf-8 -*-
# Generated by Django 1.9b1 on 2015-12-01 23:08
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('extractions', '0007_auto_20151130_1404'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='extraction',
            name='projects_string',
        ),
        migrations.AlterUniqueTogether(
            name='extraction',
            unique_together=set([('aliquot', 'ext_id')]),
        ),
        migrations.AlterIndexTogether(
            name='extraction',
            index_together=set([('aliquot', 'ext_id')]),
        ),
    ]