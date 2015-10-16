# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('samples', '0002_auto_20151016_1417'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sample',
            name='platform',
            field=models.CharField(choices=[('WHOLE-EXOME', 'WHOLE-EXOME'), ('WHOLE-GENOME', 'WHOLE-GENOME'), ('TARGETED-DNA', 'TARGETED-DNA'), ('RNA-SEQ-TARGETED', 'RNA-SEQ-TARGETED'), ('RNA-SEQ-WHOLE-TRANSCRIPTOME', 'RNA-SEQ-WHOLE-TRANSCRIPTOME'), ('RNA-SEQ-SINGLE-CELL', 'RNA-SEQ-SINGLE-CELL'), ('DNA-METHYLATION-SEQ', 'DNA-METHYLATION-SEQ'), ('CHIP-SEQ', 'CHIP-SEQ'), ('ATAC-SEQ', 'ATAC-SEQ')], verbose_name='platform', max_length=30),
        ),
        migrations.AlterField(
            model_name='sample',
            name='technology',
            field=models.CharField(choices=[('AGILENTV4', 'AGILENTV4'), ('AGILENTV5', 'AGILENTV5'), ('WHOLEGENOMELIBRARYV1', 'WHOLEGENOMELIBRARYV1'), ('HEMEPACTV1', 'HEMEPACTV1'), ('HEMEPACTV2', 'HEMEPACTV2')], verbose_name='technology', max_length=30),
        ),
    ]
