# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_auto_20151016_1645'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='participants',
            field=models.ManyToManyField(related_name='projects_as_participant', to='participants.Participant', verbose_name='participants', blank=True),
        ),
    ]
