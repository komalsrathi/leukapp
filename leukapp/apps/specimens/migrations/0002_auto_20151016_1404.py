# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('specimens', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='specimen',
            name='source_type',
            field=models.CharField(max_length=1, verbose_name='source_type', choices=[('Blood', 'Blood'), ('Nails', 'Nails'), ('Buccal', 'Buccal'), ('Hair', 'Hair'), ('T-Cells', 'T-Cells')], default=''),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='specimen',
            name='source',
            field=models.CharField(verbose_name='source', max_length=15, choices=[('Blood', 'Blood'), ('Nails', 'Nails'), ('Buccal', 'Buccal'), ('Hair', 'Hair'), ('T-Cells', 'T-Cells')]),
        ),
    ]
