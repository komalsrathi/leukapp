# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('individuals', '0010_auto_20151009_1704'),
    ]

    operations = [
        migrations.AlterField(
            model_name='individual',
            name='int_id',
            field=models.CharField(verbose_name='internal id', max_length=8, default=0),
            preserve_default=False,
        ),
    ]
