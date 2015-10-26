# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import leukapp.apps.leukforms.validators


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Leukform',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('description', models.CharField(help_text='This is for your future self.', max_length=140, verbose_name='description', blank=True)),
                ('submission', models.FileField(upload_to='leukform/submissions/%Y/%m', validators=[leukapp.apps.leukforms.validators.leukform_csv_validator], verbose_name='leukform')),
                ('result', models.FileField(verbose_name='sumbission result', blank=True, upload_to='leukform/results/%Y/%m')),
                ('summary', models.TextField(verbose_name='summary', blank=True)),
                ('slug', models.SlugField(unique=True, verbose_name='slug', editable=False)),
                ('user', models.ForeignKey(null=True, to=settings.AUTH_USER_MODEL, verbose_name='user', blank=True)),
            ],
            options={
                'verbose_name_plural': 'leukforms',
                'verbose_name': 'leukform',
            },
        ),
    ]
