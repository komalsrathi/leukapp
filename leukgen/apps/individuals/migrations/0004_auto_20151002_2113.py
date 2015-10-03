# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('individuals', '0003_auto_20151002_2018'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='individual',
            name='int_id',
        ),
        migrations.AlterField(
            model_name='individual',
            name='ext_id',
            field=models.CharField(verbose_name='External ID', max_length=100),
        ),
        migrations.AlterField(
            model_name='individual',
            name='slug',
            field=models.CharField(max_length=100, verbose_name='Slug', blank=True),
        ),
    ]
