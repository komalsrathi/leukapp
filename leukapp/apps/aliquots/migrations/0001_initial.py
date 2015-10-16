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
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('slug', models.SlugField(max_length=100, verbose_name='slug', unique=True)),
                ('bio_source', models.CharField(choices=[('D', 'DNA'), ('R', 'RNA'), ('M', 'MIXED')], verbose_name='biological material', max_length=1)),
                ('ext_id', models.CharField(validators=[django.core.validators.RegexValidator(message="Enter a valid 'External id' consisting of letters, numbers, underscores or hyphens.", code='invalid', regex='^[-a-zA-Z0-9_]+\\Z')], max_length=100, verbose_name='external id', help_text='The external id should be unique at the Specimen level.')),
                ('int_id', models.CharField(null=True, max_length=8, verbose_name='internal id')),
                ('samples_created', models.PositiveSmallIntegerField(default=0, verbose_name='number of samples created')),
                ('specimen', models.ForeignKey(verbose_name='specimen', to='specimens.Specimen')),
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
