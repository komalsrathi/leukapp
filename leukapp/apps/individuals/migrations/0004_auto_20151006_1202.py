# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('individuals', '0003_auto_20151006_1200'),
    ]

    operations = [
        migrations.AlterField(
            model_name='individual',
            name='specimens_count',
            field=models.PositiveIntegerField(default=0, verbose_name='aliquot count'),
        ),
    ]
