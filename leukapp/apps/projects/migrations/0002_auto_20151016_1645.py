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
            name='participants',
            field=models.ManyToManyField(verbose_name='participants', related_name='projects_as_participant', blank=True, null=True, to='participants.Participant'),
        ),
    ]
