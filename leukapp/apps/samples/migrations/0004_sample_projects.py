# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_auto_20151016_1645'),
        ('samples', '0003_auto_20151016_1423'),
    ]

    operations = [
        migrations.AddField(
            model_name='sample',
            name='projects',
            field=models.ManyToManyField(verbose_name='projects', to='projects.Project', blank=True, null=True),
        ),
    ]
