# -*- coding: utf-8 -*-
# Generated by Django 1.9b1 on 2015-11-25 23:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('extractions', '0002_extraction_projects'),
    ]

    operations = [
        migrations.AlterField(
            model_name='extraction',
            name='platform',
            field=models.CharField(choices=[('HISEQ', 'HISEQ'), ('ILLUMINA-XTEN', 'ILLUMINA-XTEN'), ('AGILENT-50MB', 'AGILENT-50MB'), ('AGILENT-51MB', 'AGILENT-51MB'), ('PAIRED-END-50BP', 'PAIRED-END-50BP'), ('SINGLE-END-150BP', 'SINGLE-END-150BP'), ('HEMEPACT-V1', 'HEMEPACT-V1'), ('HEMEPACT-V2', 'HEMEPACT-V2'), ('HEMEPACT-V3', 'HEMEPACT-V3'), ('IMPACT-HEME', 'IMPACT-HEME'), ('IMPACT-300', 'IMPACT-300'), ('IMPACT-340', 'IMPACT-340'), ('IMPACT-CLINICAL', 'IMPACT-CLINICAL'), ('H3K4ME1', 'H3K4ME1'), ('H3K4ME3', 'H3K4ME3'), ('H3K4ME2', 'H3K4ME2'), ('H3K27AC', 'H3K27AC'), ('FOUNDATIONONE-HEME-PANEL', 'FOUNDATIONONE-HEME-PANEL'), ('FOUNDATIONONE-PANEL', 'FOUNDATIONONE-PANEL')], max_length=100, null=True, verbose_name='platform'),
        ),
        migrations.AlterField(
            model_name='extraction',
            name='technology',
            field=models.CharField(choices=[('WHOLE-EXOME', 'WHOLE-EXOME'), ('WHOLE-GENOME', 'WHOLE-GENOME'), ('TARGETED-DNA', 'TARGETED-DNA'), ('RNA-SEQ', 'RNA-SEQ'), ('RNA-SEQ-CUSTOM', 'RNA-SEQ-CUSTOM'), ('RNA-SEQ-SINGLE-CELL', 'RNA-SEQ-SINGLE-CELL'), ('CHIP-SEQ', 'CHIP-SEQ'), ('ATAC-SEQ', 'ATAC-SEQ'), ('FOUNDATION', 'FOUNDATION'), ('RLP', 'RLP')], max_length=100, null=True, verbose_name='technology'),
        ),
    ]