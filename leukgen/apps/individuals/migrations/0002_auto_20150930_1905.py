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
            name='institution',
            field=models.CharField(max_length=3, choices=[('MSK', 'Memorial Sloan-Kettering Cancer Center'), ('O', 'Other')], verbose_name='Institution'),
        ),
        migrations.AlterField(
            model_name='individual',
            name='species',
            field=models.CharField(max_length=1, choices=[('H', 'Human'), ('M', 'Mouse'), ('Y', 'Yeast'), ('Z', 'Zebrafish')], verbose_name="Individual's species"),
        ),
    ]
