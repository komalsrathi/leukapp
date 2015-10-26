# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('specimens', '0006_auto_20151026_1046'),
    ]

    operations = [
        migrations.CreateModel(
            name='Aliquot',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('bio_source', models.CharField(max_length=1, choices=[('D', 'DNA'), ('R', 'RNA')], verbose_name='biological material')),
                ('ext_id', models.CharField(help_text='The external id should be unique at the Specimen level.', max_length=100, validators=[django.core.validators.RegexValidator(code='invalid', message="Enter a valid 'External id' consisting of letters, numbers, underscores or hyphens.", regex='^[-a-zA-Z0-9_]+\\Z')], verbose_name='external id')),
                ('int_id', models.CharField(null=True, editable=False, max_length=8, verbose_name='internal id')),
                ('runs_count', models.PositiveSmallIntegerField(default=0, editable=False, verbose_name='number of samples created')),
                ('slug', models.SlugField(unique=True, verbose_name='slug', editable=False)),
                ('specimen', models.ForeignKey(to='specimens.Specimen', verbose_name='specimen')),
            ],
            options={
                'verbose_name_plural': 'aliquots',
                'verbose_name': 'aliquot',
            },
        ),
        migrations.AlterUniqueTogether(
            name='aliquot',
            unique_together=set([('ext_id', 'specimen')]),
        ),
        migrations.AlterIndexTogether(
            name='aliquot',
            index_together=set([('ext_id', 'specimen')]),
        ),
    ]
