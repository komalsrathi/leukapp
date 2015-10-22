# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('leukforms', '0002_auto_20151020_1523'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='leukform',
            name='samples',
        ),
        migrations.AddField(
            model_name='leukform',
            name='summary',
            field=models.TextField(blank=True, verbose_name='summary'),
        ),
        migrations.AlterField(
            model_name='leukform',
            name='description',
            field=models.CharField(max_length=140, blank=True, help_text='This is for your future self.', verbose_name='description'),
        ),
    ]
