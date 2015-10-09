# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('individuals', '0006_auto_20151008_1916'),
    ]

    operations = [
        migrations.AlterField(
            model_name='individual',
            name='ext_id',
            field=models.CharField(help_text="Enter a 'External id' consisting of letters, numbers, underscores or hyphens.", validators=[django.core.validators.RegexValidator(code='invalid', message="Enter a valid 'External id' consisting of letters, numbers, underscores or hyphens.", regex='^[-a-zA-Z0-9_]+\\Z')], verbose_name='external id', max_length=100),
        ),
        migrations.AlterField(
            model_name='individual',
            name='int_id',
            field=models.PositiveIntegerField(verbose_name='internal id', default=10),
            preserve_default=False,
        ),
    ]
