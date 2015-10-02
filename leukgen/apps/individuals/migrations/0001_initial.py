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
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('institution', models.CharField(max_length=3, choices=[('MSK', 'Memorial Sloan-Kettering Cancer Center'), ('O', 'Other')], verbose_name='Source Institution')),
                ('species', models.CharField(max_length=1, choices=[('H', 'Human'), ('M', 'Mouse'), ('Y', 'Yeast'), ('Z', 'Zebrafish')], verbose_name="Individual's species")),
                ('ext_id', models.CharField(max_length=100, verbose_name='External ID')),
                ('int_id', models.CharField(max_length=7, blank=True, verbose_name='Internal ID')),
                ('leukid', models.CharField(max_length=100, blank=True, verbose_name='Individual Leukid')),
            ],
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
