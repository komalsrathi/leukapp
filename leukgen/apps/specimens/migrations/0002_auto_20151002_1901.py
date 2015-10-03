# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('specimens', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='specimen',
            name='int_id',
            field=models.CharField(max_length=7, blank=True, verbose_name='Internal ID'),
        ),
        migrations.AddField(
            model_name='specimen',
            name='leukid',
            field=models.CharField(max_length=100, blank=True, verbose_name="Specimen's Leukid"),
        ),
        migrations.AlterField(
            model_name='specimen',
            name='ext_id',
            field=models.CharField(max_length=100, verbose_name='External ID'),
        ),
    ]
