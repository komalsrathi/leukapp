# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='data_analyst',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='project',
            name='description',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='project',
            name='name',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='project',
            name='principal_investigator',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='project',
            name='scientist',
            field=models.CharField(default='', max_length=100),
        ),
    ]
