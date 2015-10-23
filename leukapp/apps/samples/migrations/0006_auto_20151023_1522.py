# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('samples', '0005_auto_20151016_1646'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sample',
            name='slug',
            field=models.SlugField(editable=False, unique=True, max_length=100, verbose_name='slug'),
        ),
    ]
