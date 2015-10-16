# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('aliquots', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sample',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('slug', models.SlugField(max_length=100, verbose_name='slug', unique=True)),
                ('platform', models.CharField(choices=[('WHOLE-EXOME', 'WHOLE-EXOME'), ('WHOLE-GENOME', 'WHOLE-GENOME'), ('TARGETED-DNA', 'TARGETED-DNA'), ('RNA-SEQ-TARGETED', 'RNA-SEQ-TARGETED'), ('RNA-SEQ-WHOLE-TRANSCRIPTOME', 'RNA-SEQ-WHOLE-TRANSCRIPTOME'), ('RNA-SEQ-SINGLE-CELL', 'RNA-SEQ-SINGLE-CELL'), ('DNA-METHYLATION-SEQ', 'DNA-METHYLATION-SEQ'), ('CHIP-SEQ', 'CHIP-SEQ'), ('ATAC-SEQ', 'ATAC-SEQ')], verbose_name='platform', max_length=3)),
                ('technology', models.CharField(choices=[('AGILENTV4', 'AGILENTV4'), ('AGILENTV5', 'AGILENTV5'), ('WHOLEGENOMELIBRARYV1', 'WHOLEGENOMELIBRARYV1'), ('HEMEPACTV1', 'HEMEPACTV1'), ('HEMEPACTV2', 'HEMEPACTV2')], verbose_name='technology', max_length=3)),
                ('center', models.CharField(choices=[('CMO', 'CMO'), ('NYGC', 'NYGC'), ('FOUNDATION', 'FOUNDATION')], verbose_name='sequencing center', max_length=3)),
                ('ext_id', models.CharField(validators=[django.core.validators.RegexValidator(message="Enter a valid 'External id' consisting of letters, numbers, underscores or hyphens.", code='invalid', regex='^[-a-zA-Z0-9_]+\\Z')], max_length=100, verbose_name='sequencing center id', help_text='The sequencing center id should be unique at the Institution and Species levels.')),
                ('int_id', models.CharField(null=True, max_length=8, verbose_name='internal id')),
                ('aliquot', models.ForeignKey(verbose_name='aliquot', to='aliquots.Aliquot')),
            ],
            options={
                'verbose_name_plural': 'samples',
                'verbose_name': 'sample',
            },
        ),
        migrations.AlterUniqueTogether(
            name='sample',
            unique_together=set([('ext_id', 'aliquot')]),
        ),
        migrations.AlterIndexTogether(
            name='sample',
            index_together=set([('ext_id', 'aliquot')]),
        ),
    ]
