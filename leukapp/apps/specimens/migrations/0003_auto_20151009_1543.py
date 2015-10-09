# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('specimens', '0002_auto_20151006_1202'),
    ]

    operations = [
        migrations.RenameField(
            model_name='specimen',
            old_name='aliquots_count',
            new_name='aliquots_created',
        ),
        migrations.AlterField(
            model_name='specimen',
            name='ext_id',
            field=models.CharField(verbose_name='external id', help_text="Enter a 'External id' consisting of letters, numbers, underscores or hyphens.", validators=[django.core.validators.RegexValidator(message="Enter a valid 'External id' consisting of letters, numbers, underscores or hyphens.", regex='^[-a-zA-Z0-9_]+\\Z', code='invalid')], max_length=100),
        ),
        migrations.AlterField(
            model_name='specimen',
            name='int_id',
            field=models.CharField(verbose_name='internal id', null=True, max_length=8),
        ),
    ]
