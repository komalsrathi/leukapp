# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('individuals', '0009_auto_20151009_1543'),
    ]

    operations = [
        migrations.AlterField(
            model_name='individual',
            name='specimens_created',
            field=models.PositiveSmallIntegerField(default=0, verbose_name='number of specimens created'),
        ),
    ]
