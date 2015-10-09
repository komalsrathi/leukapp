# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='description',
            field=models.CharField(max_length=140, verbose_name='project description'),
        ),
        migrations.AlterField(
            model_name='project',
            name='name',
            field=models.CharField(validators=[django.core.validators.RegexValidator(message='Enter a valid name consisting of letters, numbers, white spaces, underscores or hyphens.', code='invalid', regex='^[-a-zA-Z0-9_\\s]+\\Z')], max_length=100, verbose_name='project name'),
        ),
    ]
