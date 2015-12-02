# -*- coding: utf-8 -*-
# Generated by Django 1.9b1 on 2015-11-23 17:52
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('aliquots', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Extraction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('analyte', models.CharField(choices=[('DNA', 'DNA'), ('RNA', 'RNA')], max_length=100, null=True, verbose_name='biological material')),
                ('projects_string', models.CharField(blank=True, help_text="Include the projects pks separated by a '|' character", max_length=100, null=True, verbose_name='list of projetcs')),
                ('platform', models.CharField(choices=[('AGILENTV4', 'AGILENTV4'), ('AGILENTV5', 'AGILENTV5'), ('WHOLEGENOMELIBRARYV1', 'WHOLEGENOMELIBRARYV1'), ('HEMEPACTV1', 'HEMEPACTV1'), ('HEMEPACTV2', 'HEMEPACTV2')], max_length=100, null=True, verbose_name='platform')),
                ('technology', models.CharField(choices=[('WHOLE-EXOME', 'WHOLE-EXOME'), ('WHOLE-GENOME', 'WHOLE-GENOME'), ('TARGETED-DNA', 'TARGETED-DNA'), ('RNA-SEQ-TARGETED', 'RNA-SEQ-TARGETED'), ('RNA-SEQ-WHOLE-TRANSCRIPTOME', 'RNA-SEQ-WHOLE-TRANSCRIPTOME'), ('RNA-SEQ-SINGLE-CELL', 'RNA-SEQ-SINGLE-CELL'), ('DNA-METHYLATION-SEQ', 'DNA-METHYLATION-SEQ'), ('CHIP-SEQ', 'CHIP-SEQ'), ('ATAC-SEQ', 'ATAC-SEQ')], max_length=100, null=True, verbose_name='technology')),
                ('center', models.CharField(choices=[('CMO', 'CMO'), ('NYGC', 'NYGC'), ('FOUNDATION', 'FOUNDATION')], max_length=100, null=True, verbose_name='sequencing center')),
                ('ext_id', models.CharField(default='UNKNOWN', help_text='The sequencing center id.', max_length=100, null=True, validators=[django.core.validators.RegexValidator(code='invalid', message="Enter a valid 'External id' consisting of letters, numbers, underscores or hyphens.", regex='^[-a-zA-Z0-9_.]+\\Z')], verbose_name='sequencing center id')),
                ('int_id', models.CharField(max_length=100, null=True, verbose_name='internal id')),
                ('slug', models.SlugField(editable=False, null=True, unique=True, verbose_name='slug')),
                ('aliquot', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='aliquots.Aliquot', verbose_name='aliquot')),
            ],
            options={
                'verbose_name_plural': 'extractions',
                'verbose_name': 'extraction',
            },
        ),
    ]
