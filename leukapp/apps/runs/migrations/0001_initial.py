# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
        ('aliquots', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Run',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('platform', models.CharField(max_length=30, verbose_name='platform', choices=[('WHOLE-EXOME', 'WHOLE-EXOME'), ('WHOLE-GENOME', 'WHOLE-GENOME'), ('TARGETED-DNA', 'TARGETED-DNA'), ('RNA-SEQ-TARGETED', 'RNA-SEQ-TARGETED'), ('RNA-SEQ-WHOLE-TRANSCRIPTOME', 'RNA-SEQ-WHOLE-TRANSCRIPTOME'), ('RNA-SEQ-SINGLE-CELL', 'RNA-SEQ-SINGLE-CELL'), ('DNA-METHYLATION-SEQ', 'DNA-METHYLATION-SEQ'), ('CHIP-SEQ', 'CHIP-SEQ'), ('ATAC-SEQ', 'ATAC-SEQ')])),
                ('technology', models.CharField(max_length=30, verbose_name='technology', choices=[('AGILENTV4', 'AGILENTV4'), ('AGILENTV5', 'AGILENTV5'), ('WHOLEGENOMELIBRARYV1', 'WHOLEGENOMELIBRARYV1'), ('HEMEPACTV1', 'HEMEPACTV1'), ('HEMEPACTV2', 'HEMEPACTV2')])),
                ('center', models.CharField(max_length=10, verbose_name='sequencing center', choices=[('CMO', 'CMO'), ('NYGC', 'NYGC'), ('FOUNDATION', 'FOUNDATION')])),
                ('ext_id', models.CharField(help_text='The sequencing center id should be unique at the Institution and Species levels.', verbose_name='sequencing center id', validators=[django.core.validators.RegexValidator(message="Enter a valid 'External id' consisting of letters, numbers, underscores or hyphens.", code='invalid', regex='^[-a-zA-Z0-9_]+\\Z')], max_length=100)),
                ('int_id', models.CharField(max_length=8, verbose_name='internal id', null=True)),
                ('slug', models.SlugField(verbose_name='slug', editable=False, unique=True)),
                ('aliquot', models.ForeignKey(verbose_name='aliquot', to='aliquots.Aliquot')),
                ('projects', models.ManyToManyField(verbose_name='projects', blank=True, to='projects.Project')),
            ],
            options={
                'verbose_name': 'run',
                'verbose_name_plural': 'runs',
            },
        ),
        migrations.AlterUniqueTogether(
            name='run',
            unique_together=set([('ext_id', 'aliquot')]),
        ),
        migrations.AlterIndexTogether(
            name='run',
            index_together=set([('ext_id', 'aliquot')]),
        ),
    ]
