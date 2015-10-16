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
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('slug', models.SlugField(max_length=100, verbose_name='slug', unique=True)),
                ('first_name', models.CharField(max_length=100, verbose_name='first name')),
                ('last_name', models.CharField(max_length=100, verbose_name='last name')),
                ('email', models.EmailField(max_length=254, verbose_name='email', unique=True)),
                ('phone', models.CharField(validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'.Up to 15 digits allowed.", regex='^\\+?1?\\d{9,15}$')], blank=True, max_length=15, verbose_name='phone')),
            ],
            options={
                'verbose_name_plural': 'participants',
                'verbose_name': 'participant',
            },
        ),
    ]
