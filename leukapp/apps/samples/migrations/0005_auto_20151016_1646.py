# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('samples', '0004_sample_projects'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sample',
            name='projects',
            field=models.ManyToManyField(to='projects.Project', verbose_name='projects', blank=True),
        ),
    ]
