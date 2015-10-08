# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('individuals', '0002_auto_20151006_1159'),
    ]

    operations = [
        migrations.AlterField(
            model_name='individual',
            name='int_id',
            field=models.PositiveIntegerField(verbose_name='internal id', null=True),
        ),
    ]
