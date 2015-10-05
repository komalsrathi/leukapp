# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Individual',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('slug', models.SlugField(max_length=100, unique=True, verbose_name='slug')),
                ('institution', models.CharField(max_length=3, verbose_name="individual's institution", choices=[('MSK', 'Memorial Sloan-Kettering Cancer Center'), ('O', 'Other')])),
                ('species', models.CharField(max_length=1, verbose_name="individual's species", choices=[('H', 'Human'), ('M', 'Mouse'), ('Y', 'Yeast'), ('Z', 'Zebrafish')])),
                ('specimens_count', models.PositiveIntegerField(verbose_name='aliquot count')),
                ('ext_id', models.CharField(max_length=100, verbose_name='external id')),
                ('int_id', models.PositiveIntegerField(verbose_name='internal id')),
            ],
            options={
                'verbose_name': 'individual',
                'verbose_name_plural': 'individuals',
            },
        ),
        migrations.AlterUniqueTogether(
            name='individual',
            unique_together=set([('ext_id', 'institution', 'species')]),
        ),
        migrations.AlterIndexTogether(
            name='individual',
            index_together=set([('ext_id', 'institution', 'species')]),
        ),
    ]
