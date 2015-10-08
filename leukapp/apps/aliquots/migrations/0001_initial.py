# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('specimens', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Aliquot',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('slug', models.SlugField(max_length=100, unique=True, verbose_name='slug')),
                ('biological_material', models.CharField(max_length=1, verbose_name='biological material', choices=[('D', 'DNA'), ('R', 'RNA'), ('M', 'MIXED')])),
                ('ext_id', models.CharField(max_length=100, verbose_name='external id')),
                ('int_id', models.PositiveIntegerField(verbose_name='internal id')),
                ('specimen', models.ForeignKey(to='specimens.Specimen', verbose_name='specimen')),
            ],
            options={
                'verbose_name': 'aliquot',
                'verbose_name_plural': 'aliquots',
            },
        ),
        migrations.AlterUniqueTogether(
            name='aliquot',
            unique_together=set([('ext_id', 'biological_material', 'specimen')]),
        ),
        migrations.AlterIndexTogether(
            name='aliquot',
            index_together=set([('ext_id', 'biological_material', 'specimen')]),
        ),
    ]
