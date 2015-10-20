# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('specimens', '0002_auto_20151016_1404'),
    ]

    operations = [
        migrations.AlterField(
            model_name='specimen',
            name='source',
            field=models.CharField(max_length=100, choices=[('Blood', 'Blood'), ('Nails', 'Nails'), ('Buccal', 'Buccal'), ('Hair', 'Hair'), ('T-Cells', 'T-Cells')], verbose_name='source'),
        ),
        migrations.AlterField(
            model_name='specimen',
            name='source_type',
            field=models.CharField(max_length=100, choices=[('T', 'Tumor'), ('N', 'Normal')], verbose_name='source_type'),
        ),
    ]
