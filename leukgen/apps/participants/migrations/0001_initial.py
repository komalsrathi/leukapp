# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Participant',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('slug', models.SlugField(max_length=100, unique=True, verbose_name='slug')),
                ('first_name', models.CharField(max_length=100, verbose_name='first name')),
                ('last_name', models.CharField(max_length=100, verbose_name='last name')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='email')),
                ('phone', models.CharField(max_length=15, blank=True, validators=[django.core.validators.RegexValidator(regex='^\\+?1?\\d{9,15}$', message="Phone number must be entered in the format: '+999999999'.Up to 15 digits allowed.")], verbose_name='phone')),
            ],
            options={
                'verbose_name': 'participant',
                'verbose_name_plural': 'participants',
            },
        ),
    ]
