# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aliquots', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aliquot',
            name='int_id',
            field=models.PositiveIntegerField(verbose_name='internal id', null=True),
        ),
    ]
