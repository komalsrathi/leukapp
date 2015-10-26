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
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=100, verbose_name='project name', validators=[django.core.validators.RegexValidator(message='Enter a valid name consisting of letters, numbers, white spaces, underscores or hyphens.', code='invalid', regex='^[-a-zA-Z0-9_\\s]+\\Z')])),
                ('description', models.CharField(max_length=140, verbose_name='project description')),
                ('cost_center_no', models.CharField(max_length=100, verbose_name='cost center number')),
                ('fund_no', models.CharField(max_length=100, verbose_name='fund number')),
                ('protocol_no', models.CharField(max_length=100, verbose_name='protocol number')),
                ('slug', models.SlugField(verbose_name='slug', editable=False, unique=True)),
                ('analyst', models.ForeignKey(related_name='projects_as_analyst', verbose_name='data analyst', to='participants.Participant')),
                ('participants', models.ManyToManyField(verbose_name='participants', to='participants.Participant', blank=True, related_name='projects_as_participant')),
                ('pi', models.ForeignKey(related_name='projects_as_pi', verbose_name='principal investigator', to='participants.Participant')),
                ('requestor', models.ForeignKey(related_name='projects_as_requestor', verbose_name='requestor', to='participants.Participant')),
            ],
            options={
                'verbose_name': 'project',
                'verbose_name_plural': 'projects',
            },
        ),
    ]
