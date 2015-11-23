# -*- coding: utf-8 -*-
# Generated by Django 1.9b1 on 2015-11-23 17:52
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('participants', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=100, null=True, unique=True, validators=[django.core.validators.RegexValidator(code='invalid', message='Enter a valid name consisting of letters, numbers, white spaces, underscores or hyphens.', regex='^[-a-zA-Z0-9_\\s]+\\Z')], verbose_name='project title')),
                ('description', models.CharField(max_length=140, null=True, verbose_name='project description')),
                ('cost_center_no', models.CharField(max_length=100, null=True, verbose_name='cost center number')),
                ('fund_no', models.CharField(max_length=100, null=True, verbose_name='fund number')),
                ('protocol_no', models.CharField(max_length=100, null=True, verbose_name='protocol number')),
                ('slug', models.SlugField(editable=False, null=True, unique=True, verbose_name='slug')),
                ('int_id', models.SlugField(editable=False, null=True, unique=True, verbose_name='int_id')),
                ('analyst', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='projects_as_analyst', to='participants.Participant', verbose_name='data analyst')),
            ],
            options={
                'verbose_name_plural': 'projects',
                'verbose_name': 'project',
            },
        ),
    ]
