# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('individuals', '0004_auto_20151006_1202'),
    ]

    operations = [
        migrations.AlterField(
            model_name='individual',
            name='ext_id',
            field=models.CharField(validators=[django.core.validators.RegexValidator(message="Enter a valid 'slug' consisting of letters, numbers, underscores or hyphens.", code='invalid', regex='^[-a-zA-Z0-9_]+\\Z')], max_length=100, verbose_name='external id', editable=False),
        ),
        migrations.AlterField(
            model_name='individual',
            name='int_id',
            field=models.PositiveIntegerField(null=True, verbose_name='internal id', editable=False),
        ),
        migrations.AlterField(
            model_name='individual',
            name='specimens_count',
            field=models.PositiveSmallIntegerField(default=0, verbose_name='specimen count', editable=False),
        ),
    ]
