# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('aliquots', '0002_auto_20151006_1457'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aliquot',
            name='ext_id',
            field=models.CharField(validators=[django.core.validators.RegexValidator(code='invalid', regex='^[-a-zA-Z0-9_]+\\Z', message="Enter a valid 'External id' consisting of letters, numbers, underscores or hyphens.")], help_text='The external id should be unique at the Specimen level.', max_length=100, verbose_name='external id'),
        ),
        migrations.AlterField(
            model_name='aliquot',
            name='int_id',
            field=models.CharField(max_length=8, null=True, verbose_name='internal id'),
        ),
        migrations.AlterUniqueTogether(
            name='aliquot',
            unique_together=set([('ext_id', 'specimen')]),
        ),
        migrations.AlterIndexTogether(
            name='aliquot',
            index_together=set([('ext_id', 'specimen')]),
        ),
    ]
