# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=100, default='')),
                ('pi', models.ForeignKey(verbose_name='principal investigator', to=settings.AUTH_USER_MODEL, related_name='projects_as_pi')),
                ('scientist', models.ForeignKey(verbose_name='scientist', to=settings.AUTH_USER_MODEL, blank=True, null=True, related_name='projects_as_scientist')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
