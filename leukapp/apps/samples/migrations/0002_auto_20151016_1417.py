# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('samples', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sample',
            name='center',
            field=models.CharField(max_length=10, choices=[('CMO', 'CMO'), ('NYGC', 'NYGC'), ('FOUNDATION', 'FOUNDATION')], verbose_name='sequencing center'),
        ),
        migrations.AlterField(
            model_name='sample',
            name='platform',
            field=models.CharField(max_length=20, choices=[('WHOLE-EXOME', 'WHOLE-EXOME'), ('WHOLE-GENOME', 'WHOLE-GENOME'), ('TARGETED-DNA', 'TARGETED-DNA'), ('RNA-SEQ-TARGETED', 'RNA-SEQ-TARGETED'), ('RNA-SEQ-WHOLE-TRANSCRIPTOME', 'RNA-SEQ-WHOLE-TRANSCRIPTOME'), ('RNA-SEQ-SINGLE-CELL', 'RNA-SEQ-SINGLE-CELL'), ('DNA-METHYLATION-SEQ', 'DNA-METHYLATION-SEQ'), ('CHIP-SEQ', 'CHIP-SEQ'), ('ATAC-SEQ', 'ATAC-SEQ')], verbose_name='platform'),
        ),
        migrations.AlterField(
            model_name='sample',
            name='technology',
            field=models.CharField(max_length=20, choices=[('AGILENTV4', 'AGILENTV4'), ('AGILENTV5', 'AGILENTV5'), ('WHOLEGENOMELIBRARYV1', 'WHOLEGENOMELIBRARYV1'), ('HEMEPACTV1', 'HEMEPACTV1'), ('HEMEPACTV2', 'HEMEPACTV2')], verbose_name='technology'),
        ),
    ]
