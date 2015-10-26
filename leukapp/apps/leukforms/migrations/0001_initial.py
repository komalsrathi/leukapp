# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import leukapp.apps.leukforms.validators


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Leukform',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('description', models.CharField(help_text='This is for your future self.', verbose_name='description', max_length=140, blank=True)),
                ('submission', models.FileField(verbose_name='leukform', upload_to='leukform/submissions/%Y/%m', validators=[leukapp.apps.leukforms.validators.leukform_csv_validator])),
                ('result', models.FileField(verbose_name='sumbission result', upload_to='leukform/results/%Y/%m', blank=True)),
                ('summary', models.TextField(verbose_name='summary', blank=True)),
                ('slug', models.SlugField(verbose_name='slug', editable=False, unique=True)),
            ],
            options={
                'verbose_name': 'leukform',
                'verbose_name_plural': 'leukforms',
            },
        ),
    ]
