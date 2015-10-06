# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('specimens', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='specimen',
            name='aliquots_count',
            field=models.PositiveIntegerField(default=0, verbose_name='aliquot count'),
        ),
        migrations.AlterField(
            model_name='specimen',
            name='int_id',
            field=models.PositiveIntegerField(null=True, verbose_name='internal id'),
        ),
    ]
