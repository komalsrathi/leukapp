# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Individual',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('slug', models.SlugField(max_length=100, verbose_name='slug', unique=True)),
                ('institution', models.CharField(choices=[('MSK', 'Memorial Sloan-Kettering Cancer Center'), ('O', 'Other')], verbose_name='institution', max_length=3)),
                ('species', models.CharField(choices=[('H', 'Human'), ('M', 'Mouse'), ('Y', 'Yeast'), ('Z', 'Zebrafish')], verbose_name='species', max_length=1)),
                ('ext_id', models.CharField(validators=[django.core.validators.RegexValidator(message="Enter a valid 'External id' consisting of letters, numbers, underscores or hyphens.", code='invalid', regex='^[-a-zA-Z0-9_]+\\Z')], max_length=100, verbose_name='external id', help_text='The external id should be unique at the Institution and Species levels.')),
                ('specimens_created', models.PositiveSmallIntegerField(default=0, verbose_name='number of specimens created')),
                ('int_id', models.CharField(max_length=8, verbose_name='internal id')),
            ],
            options={
                'verbose_name_plural': 'individuals',
                'verbose_name': 'individual',
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
