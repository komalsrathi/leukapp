# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('specimens', '0003_auto_20151019_1547'),
    ]

    operations = [
        migrations.AlterField(
            model_name='specimen',
            name='aliquots_created',
            field=models.PositiveSmallIntegerField(editable=False, default=0, verbose_name='number of aliquots created'),
        ),
        migrations.AlterField(
            model_name='specimen',
            name='int_id',
            field=models.CharField(editable=False, max_length=8, verbose_name='internal id', null=True),
        ),
        migrations.AlterField(
            model_name='specimen',
            name='slug',
            field=models.SlugField(editable=False, unique=True, max_length=100, verbose_name='slug'),
        ),
    ]
