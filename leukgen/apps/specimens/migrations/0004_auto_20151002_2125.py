# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('specimens', '0003_auto_20151002_2113'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='specimen',
            name='int_id',
        ),
        migrations.AlterField(
            model_name='specimen',
            name='slug',
            field=models.CharField(max_length=100, blank=True, verbose_name='Slug'),
        ),
    ]
