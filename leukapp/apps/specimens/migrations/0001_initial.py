# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('individuals', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Specimen',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('source', models.CharField(max_length=100, verbose_name='source', choices=[('Blood', 'Blood'), ('Nails', 'Nails'), ('Buccal', 'Buccal'), ('Hair', 'Hair'), ('T-Cells', 'T-Cells')], blank=True)),
                ('source_type', models.CharField(max_length=100, verbose_name='source_type', choices=[('T', 'Tumor'), ('N', 'Normal')])),
                ('ext_id', models.CharField(help_text='The external id should be unique at the Individual and Source levels.', verbose_name='external id', validators=[django.core.validators.RegexValidator(message="Enter a valid 'External id' consisting of letters, numbers, underscores or hyphens.", code='invalid', regex='^[-a-zA-Z0-9_]+\\Z')], max_length=100)),
                ('dna_count', models.PositiveSmallIntegerField(verbose_name='number of aliquots created', default=0, editable=False)),
                ('rna_count', models.PositiveSmallIntegerField(verbose_name='number of aliquots created', default=0, editable=False)),
                ('int_id', models.CharField(max_length=8, verbose_name='internal id', editable=False, null=True)),
                ('slug', models.SlugField(verbose_name='slug', editable=False, unique=True)),
                ('individual', models.ForeignKey(verbose_name='individual', to='individuals.Individual')),
            ],
            options={
                'verbose_name': 'specimen',
                'verbose_name_plural': 'specimens',
            },
        ),
        migrations.AlterUniqueTogether(
            name='specimen',
            unique_together=set([('ext_id', 'individual', 'source_type')]),
        ),
        migrations.AlterIndexTogether(
            name='specimen',
            index_together=set([('ext_id', 'individual', 'source_type')]),
        ),
    ]
