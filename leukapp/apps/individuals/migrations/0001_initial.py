# -*- coding: utf-8 -*-
# Generated by Django 1.9b1 on 2015-11-17 21:00
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Individual',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('institution', models.CharField(choices=[('MSK', 'Memorial Sloan-Kettering Cancer Center'), ('OTHER', 'Other')], max_length=100, verbose_name='institution')),
                ('species', models.CharField(choices=[('HUMAN', 'Human'), ('MOUSE', 'Mouse'), ('YEAST', 'Yeast'), ('ZEBRAFISH', 'Zebrafish'), ('XENOGRAFT', 'Xenograft')], max_length=100, verbose_name='species')),
                ('ext_id', models.CharField(help_text='The external id should be unique at the Institution and Species levels.', max_length=100, validators=[django.core.validators.RegexValidator(code='invalid', message="Enter a valid 'External id' consisting of letters, numbers, underscores or hyphens.", regex='^[-a-zA-Z0-9_.]+\\Z')], verbose_name='external id')),
                ('tumors_count', models.PositiveSmallIntegerField(default=0, editable=False, verbose_name='number of tumor specimens created')),
                ('normals_count', models.PositiveSmallIntegerField(default=0, editable=False, verbose_name='number of normal specimens created')),
                ('int_id', models.CharField(editable=False, max_length=100, verbose_name='internal id')),
                ('slug', models.SlugField(editable=False, unique=True, verbose_name='slug')),
            ],
            options={
                'verbose_name': 'individual',
                'verbose_name_plural': 'individuals',
            },
        ),
        migrations.AlterUniqueTogether(
            name='individual',
            unique_together=set([('institution', 'species', 'ext_id')]),
        ),
        migrations.AlterIndexTogether(
            name='individual',
            index_together=set([('institution', 'species', 'ext_id')]),
        ),
    ]
