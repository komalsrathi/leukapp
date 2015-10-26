# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('specimens', '0005_auto_20151025_1650'),
    ]

    operations = [
        migrations.RenameField(
            model_name='specimen',
            old_name='aliquots_created',
            new_name='dna_count',
        ),
        migrations.AddField(
            model_name='specimen',
            name='rna_count',
            field=models.PositiveSmallIntegerField(default=0, verbose_name='number of aliquots created', editable=False),
        ),
        migrations.AlterField(
            model_name='specimen',
            name='source',
            field=models.CharField(choices=[('Blood', 'Blood'), ('Nails', 'Nails'), ('Buccal', 'Buccal'), ('Hair', 'Hair'), ('T-Cells', 'T-Cells')], verbose_name='source', max_length=100, blank=True),
        ),
    ]
