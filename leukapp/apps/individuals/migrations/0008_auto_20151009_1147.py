# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('individuals', '0007_auto_20151009_1143'),
    ]

    operations = [
        migrations.AlterField(
            model_name='individual',
            name='int_id',
            field=models.CharField(null=True, verbose_name='internal id', max_length=8),
        ),
    ]
