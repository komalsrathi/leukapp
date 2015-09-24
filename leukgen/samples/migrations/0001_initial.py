# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Aliquot',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Individual',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('source', models.CharField(max_length=1, choices=[('MSK', 'Memorial Sloan-Kettering Cancer Center'), ('O', 'O')])),
                ('species', models.CharField(max_length=1, choices=[('H', 'Human'), ('M', 'Mouse'), ('Y', 'Yeast'), ('Z', 'Zebrafish')])),
                ('ext_id', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Specimen',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AlterUniqueTogether(
            name='individual',
            unique_together=set([('ext_id', 'source')]),
        ),
        migrations.AlterIndexTogether(
            name='individual',
            index_together=set([('ext_id', 'source')]),
        ),
    ]
