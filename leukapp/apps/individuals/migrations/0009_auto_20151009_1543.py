# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('individuals', '0008_auto_20151009_1147'),
    ]

    operations = [
        migrations.RenameField(
            model_name='individual',
            old_name='specimens_count',
            new_name='specimens_created',
        ),
        migrations.AlterField(
            model_name='individual',
            name='ext_id',
            field=models.CharField(verbose_name='external id', help_text='The external id should be unique at the Institution and Species levels.', validators=[django.core.validators.RegexValidator(message="Enter a valid 'External id' consisting of letters, numbers, underscores or hyphens.", regex='^[-a-zA-Z0-9_]+\\Z', code='invalid')], max_length=100),
        ),
        migrations.AlterField(
            model_name='individual',
            name='institution',
            field=models.CharField(verbose_name='institution', choices=[('MSK', 'Memorial Sloan-Kettering Cancer Center'), ('O', 'Other')], max_length=3),
        ),
        migrations.AlterField(
            model_name='individual',
            name='species',
            field=models.CharField(verbose_name='species', choices=[('H', 'Human'), ('M', 'Mouse'), ('Y', 'Yeast'), ('Z', 'Zebrafish')], max_length=1),
        ),
    ]
