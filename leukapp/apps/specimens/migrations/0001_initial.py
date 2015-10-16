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
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('slug', models.SlugField(max_length=100, verbose_name='slug', unique=True)),
                ('source', models.CharField(choices=[('Blood', 'Blood'), ('Nails', 'Nails'), ('Buccal', 'Buccal'), ('Hair', 'Hair'), ('T-Cells', 'T-Cells')], verbose_name='source_type', max_length=1)),
                ('ext_id', models.CharField(validators=[django.core.validators.RegexValidator(message="Enter a valid 'External id' consisting of letters, numbers, underscores or hyphens.", code='invalid', regex='^[-a-zA-Z0-9_]+\\Z')], max_length=100, verbose_name='external id', help_text='The external id should be unique at the Individual and Source levels.')),
                ('aliquots_created', models.PositiveSmallIntegerField(default=0, verbose_name='number of aliquots created')),
                ('int_id', models.CharField(null=True, max_length=8, verbose_name='internal id')),
                ('individual', models.ForeignKey(verbose_name='individual', to='individuals.Individual')),
            ],
            options={
                'verbose_name_plural': 'specimens',
                'verbose_name': 'specimen',
            },
        ),
        migrations.AlterUniqueTogether(
            name='specimen',
            unique_together=set([('ext_id', 'individual')]),
        ),
        migrations.AlterIndexTogether(
            name='specimen',
            index_together=set([('ext_id', 'individual')]),
        ),
    ]
