# -*- coding: utf-8 -*-
# Generated by Django 1.9b1 on 2015-12-02 16:01
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('extractions', '0008_auto_20151201_1808'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='extraction',
            name='center',
        ),
        migrations.RemoveField(
            model_name='extraction',
            name='platform',
        ),
        migrations.RemoveField(
            model_name='extraction',
            name='projects',
        ),
        migrations.RemoveField(
            model_name='extraction',
            name='technology',
        ),
    ]