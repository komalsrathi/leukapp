# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('individuals', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Specimen',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('slug', models.SlugField(max_length=100, unique=True, verbose_name='slug')),
                ('source', models.CharField(max_length=1, verbose_name='source', choices=[('T', 'Tumor'), ('N', 'Normal')])),
                ('aliquots_count', models.PositiveIntegerField(verbose_name='aliquot count')),
                ('ext_id', models.CharField(max_length=100, verbose_name='external id')),
                ('int_id', models.PositiveIntegerField(verbose_name='internal id')),
                ('individual', models.ForeignKey(to='individuals.Individual', verbose_name='individual')),
            ],
            options={
                'verbose_name': 'specimen',
                'verbose_name_plural': 'specimens',
            },
        ),
        migrations.AlterUniqueTogether(
            name='specimen',
            unique_together=set([('ext_id', 'source', 'individual')]),
        ),
        migrations.AlterIndexTogether(
            name='specimen',
            index_together=set([('ext_id', 'source', 'individual')]),
        ),
    ]
