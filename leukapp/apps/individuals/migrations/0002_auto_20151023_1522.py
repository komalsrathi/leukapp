# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('individuals', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='individual',
            name='int_id',
            field=models.CharField(editable=False, max_length=8, verbose_name='internal id'),
        ),
        migrations.AlterField(
            model_name='individual',
            name='slug',
            field=models.SlugField(editable=False, unique=True, max_length=100, verbose_name='slug'),
        ),
        migrations.AlterField(
            model_name='individual',
            name='specimens_created',
            field=models.PositiveSmallIntegerField(editable=False, default=0, verbose_name='number of specimens created'),
        ),
    ]
