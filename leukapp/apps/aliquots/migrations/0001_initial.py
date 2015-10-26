# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('specimens', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Aliquot',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('bio_source', models.CharField(max_length=1, verbose_name='biological material', choices=[('D', 'DNA'), ('R', 'RNA')])),
                ('ext_id', models.CharField(help_text='The external id should be unique at the Specimen level.', verbose_name='external id', validators=[django.core.validators.RegexValidator(message="Enter a valid 'External id' consisting of letters, numbers, underscores or hyphens.", code='invalid', regex='^[-a-zA-Z0-9_]+\\Z')], max_length=100)),
                ('int_id', models.CharField(max_length=8, verbose_name='internal id', editable=False, null=True)),
                ('runs_count', models.PositiveSmallIntegerField(verbose_name='number of runs created', default=0, editable=False)),
                ('slug', models.SlugField(verbose_name='slug', editable=False, unique=True)),
                ('specimen', models.ForeignKey(verbose_name='specimen', to='specimens.Specimen')),
            ],
            options={
                'verbose_name': 'aliquot',
                'verbose_name_plural': 'aliquots',
            },
        ),
        migrations.AlterUniqueTogether(
            name='aliquot',
            unique_together=set([('ext_id', 'specimen', 'bio_source')]),
        ),
        migrations.AlterIndexTogether(
            name='aliquot',
            index_together=set([('ext_id', 'specimen', 'bio_source')]),
        ),
    ]
