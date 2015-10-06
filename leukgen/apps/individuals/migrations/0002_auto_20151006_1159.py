# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('individuals', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='individual',
            name='specimens_count',
            field=models.PositiveIntegerField(null=True, verbose_name='aliquot count'),
        ),
    ]
