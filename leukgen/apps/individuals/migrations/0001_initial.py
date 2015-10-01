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
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('institution', models.CharField(verbose_name='Source Institution', choices=[('MSK', 'Memorial Sloan-Kettering Cancer Center'), ('O', 'Other')], max_length=3)),
                ('species', models.CharField(verbose_name='Individual Species', choices=[('H', 'Human'), ('M', 'Mouse'), ('Y', 'Yeast'), ('Z', 'Zebrafish')], max_length=1)),
                ('ext_id', models.CharField(verbose_name='External ID', max_length=100)),
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
