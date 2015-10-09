# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('individuals', '0005_auto_20151008_1834'),
    ]

    operations = [
        migrations.AlterField(
            model_name='individual',
            name='ext_id',
            field=models.CharField(max_length=100, verbose_name='external id', validators=[django.core.validators.RegexValidator(code='invalid', message="Enter a valid 'slug' consisting of letters, numbers, underscores or hyphens.", regex='^[-a-zA-Z0-9_]+\\Z')]),
        ),
        migrations.AlterField(
            model_name='individual',
            name='int_id',
            field=models.PositiveIntegerField(null=True, verbose_name='internal id'),
        ),
        migrations.AlterField(
            model_name='individual',
            name='specimens_count',
            field=models.PositiveSmallIntegerField(verbose_name='specimen count', default=0),
        ),
    ]
