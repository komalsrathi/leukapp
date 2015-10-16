# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0003_auto_20151016_1646'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='cost_center_no',
            field=models.CharField(max_length=100, verbose_name='cost center number'),
        ),
        migrations.AlterField(
            model_name='project',
            name='fund_no',
            field=models.CharField(max_length=100, verbose_name='fund number'),
        ),
    ]
