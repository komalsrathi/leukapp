# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('specimens', '0003_auto_20151009_1543'),
    ]

    operations = [
        migrations.AlterField(
            model_name='specimen',
            name='aliquots_created',
            field=models.PositiveSmallIntegerField(default=0, verbose_name='number of aliquots created'),
        ),
        migrations.AlterField(
            model_name='specimen',
            name='ext_id',
            field=models.CharField(validators=[django.core.validators.RegexValidator(code='invalid', regex='^[-a-zA-Z0-9_]+\\Z', message="Enter a valid 'External id' consisting of letters, numbers, underscores or hyphens.")], help_text='The external id should be unique at the Individual and Source levels.', max_length=100, verbose_name='external id'),
        ),
    ]
