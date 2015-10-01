# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('individuals', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Specimen',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('source', models.CharField(verbose_name='Source Code', choices=[('T', 'Tumor'), ('N', 'Normal')], max_length=1)),
                ('ext_id', models.CharField(max_length=100)),
                ('individual', models.ForeignKey(to='individuals.Individual')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='specimen',
            unique_together=set([('ext_id', 'source', 'individual')]),
        ),
        migrations.AlterIndexTogether(
            name='specimen',
            index_together=set([('ext_id', 'source', 'individual')]),
        ),
    ]
