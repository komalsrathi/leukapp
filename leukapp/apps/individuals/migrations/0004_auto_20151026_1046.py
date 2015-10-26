# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('individuals', '0003_auto_20151025_1650'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='individual',
            name='specimens_created',
        ),
        migrations.AddField(
            model_name='individual',
            name='normals_count',
            field=models.PositiveSmallIntegerField(default=0, verbose_name='number of normal specimens created', editable=False),
        ),
        migrations.AddField(
            model_name='individual',
            name='tumors_count',
            field=models.PositiveSmallIntegerField(default=0, verbose_name='number of tumor specimens created', editable=False),
        ),
    ]
