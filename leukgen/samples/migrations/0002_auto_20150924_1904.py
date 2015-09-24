# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('samples', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='individual',
            name='source',
            field=models.CharField(choices=[('MSK', 'Memorial Sloan-Kettering Cancer Center'), ('O', 'Other')], max_length=3),
        ),
    ]
