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
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('institution', models.CharField(max_length=3, verbose_name='institution', choices=[('MSK', 'Memorial Sloan-Kettering Cancer Center'), ('O', 'Other')])),
                ('species', models.CharField(max_length=1, verbose_name='species', choices=[('H', 'Human'), ('M', 'Mouse'), ('Y', 'Yeast'), ('Z', 'Zebrafish')])),
                ('ext_id', models.CharField(help_text='The external id should be unique at the Institution and Species levels.', verbose_name='external id', validators=[django.core.validators.RegexValidator(message="Enter a valid 'External id' consisting of letters, numbers, underscores or hyphens.", code='invalid', regex='^[-a-zA-Z0-9_]+\\Z')], max_length=100)),
                ('tumors_count', models.PositiveSmallIntegerField(verbose_name='number of tumor specimens created', default=0, editable=False)),
                ('normals_count', models.PositiveSmallIntegerField(verbose_name='number of normal specimens created', default=0, editable=False)),
                ('int_id', models.CharField(max_length=8, verbose_name='internal id', editable=False)),
                ('slug', models.SlugField(verbose_name='slug', editable=False, unique=True)),
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
