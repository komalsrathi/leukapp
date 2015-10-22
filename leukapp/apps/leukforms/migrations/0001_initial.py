# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('samples', '0005_auto_20151016_1646'),
    ]

    operations = [
        migrations.CreateModel(
            name='Leukform',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('slug', models.SlugField(unique=True, max_length=100, verbose_name='slug')),
                ('description', models.CharField(max_length=8, verbose_name='description', blank=True, help_text='This is for your future self.')),
                ('submission', models.FileField(upload_to='leukform/submissions/%Y/%m', verbose_name='leukform csv')),
                ('result', models.FileField(upload_to='leukform/results/%Y/%m', verbose_name='sumbission result', blank=True)),
                ('samples', models.ManyToManyField(to='samples.Sample', verbose_name='samples', blank=True)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL, null=True, verbose_name='user', blank=True)),
            ],
            options={
                'verbose_name_plural': 'leukforms',
                'verbose_name': 'leukform',
            },
        ),
    ]
