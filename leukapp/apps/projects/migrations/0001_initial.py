# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('participants', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('slug', models.SlugField(max_length=100, unique=True, verbose_name='slug')),
                ('name', models.CharField(max_length=100, verbose_name='name')),
                ('description', models.CharField(max_length=140, verbose_name='description')),
                ('cost_center_no', models.PositiveIntegerField(verbose_name='cost center number')),
                ('fund_no', models.PositiveIntegerField(verbose_name='fund number')),
                ('protocol_no', models.CharField(max_length=100, verbose_name='protocol number')),
                ('analyst', models.ForeignKey(related_name='projects_as_analyst', to='participants.Participant', verbose_name='data analyst')),
                ('participants', models.ManyToManyField(related_name='projects_participant', to='participants.Participant', verbose_name='participants')),
                ('pi', models.ForeignKey(related_name='projects_as_pi', to='participants.Participant', verbose_name='principal investigator')),
                ('requestor', models.ForeignKey(related_name='projects_as_requestor', to='participants.Participant', verbose_name='requestor')),
            ],
            options={
                'verbose_name': 'project',
                'verbose_name_plural': 'projects',
            },
        ),
    ]
