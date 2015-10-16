# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('participants', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('slug', models.SlugField(max_length=100, verbose_name='slug', unique=True)),
                ('name', models.CharField(validators=[django.core.validators.RegexValidator(message='Enter a valid name consisting of letters, numbers, white spaces, underscores or hyphens.', code='invalid', regex='^[-a-zA-Z0-9_\\s]+\\Z')], max_length=100, verbose_name='project name')),
                ('description', models.CharField(max_length=140, verbose_name='project description')),
                ('cost_center_no', models.PositiveIntegerField(verbose_name='cost center number')),
                ('fund_no', models.PositiveIntegerField(verbose_name='fund number')),
                ('protocol_no', models.CharField(max_length=100, verbose_name='protocol number')),
                ('analyst', models.ForeignKey(to='participants.Participant', verbose_name='data analyst', related_name='projects_as_analyst')),
                ('participants', models.ManyToManyField(to='participants.Participant', related_name='projects_participant', verbose_name='participants')),
                ('pi', models.ForeignKey(to='participants.Participant', verbose_name='principal investigator', related_name='projects_as_pi')),
                ('requestor', models.ForeignKey(to='participants.Participant', verbose_name='requestor', related_name='projects_as_requestor')),
            ],
            options={
                'verbose_name_plural': 'projects',
                'verbose_name': 'project',
            },
        ),
    ]
