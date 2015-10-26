# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0006_auto_20151025_1650'),
        ('aliquots', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sample',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('platform', models.CharField(max_length=30, choices=[('WHOLE-EXOME', 'WHOLE-EXOME'), ('WHOLE-GENOME', 'WHOLE-GENOME'), ('TARGETED-DNA', 'TARGETED-DNA'), ('RNA-SEQ-TARGETED', 'RNA-SEQ-TARGETED'), ('RNA-SEQ-WHOLE-TRANSCRIPTOME', 'RNA-SEQ-WHOLE-TRANSCRIPTOME'), ('RNA-SEQ-SINGLE-CELL', 'RNA-SEQ-SINGLE-CELL'), ('DNA-METHYLATION-SEQ', 'DNA-METHYLATION-SEQ'), ('CHIP-SEQ', 'CHIP-SEQ'), ('ATAC-SEQ', 'ATAC-SEQ')], verbose_name='platform')),
                ('technology', models.CharField(max_length=30, choices=[('AGILENTV4', 'AGILENTV4'), ('AGILENTV5', 'AGILENTV5'), ('WHOLEGENOMELIBRARYV1', 'WHOLEGENOMELIBRARYV1'), ('HEMEPACTV1', 'HEMEPACTV1'), ('HEMEPACTV2', 'HEMEPACTV2')], verbose_name='technology')),
                ('center', models.CharField(max_length=10, choices=[('CMO', 'CMO'), ('NYGC', 'NYGC'), ('FOUNDATION', 'FOUNDATION')], verbose_name='sequencing center')),
                ('ext_id', models.CharField(help_text='The sequencing center id should be unique at the Institution and Species levels.', max_length=100, validators=[django.core.validators.RegexValidator(code='invalid', message="Enter a valid 'External id' consisting of letters, numbers, underscores or hyphens.", regex='^[-a-zA-Z0-9_]+\\Z')], verbose_name='sequencing center id')),
                ('int_id', models.CharField(null=True, max_length=8, verbose_name='internal id')),
                ('slug', models.SlugField(unique=True, verbose_name='slug', editable=False)),
                ('aliquot', models.ForeignKey(to='aliquots.Aliquot', verbose_name='aliquot')),
                ('projects', models.ManyToManyField(to='projects.Project', verbose_name='projects', blank=True)),
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
