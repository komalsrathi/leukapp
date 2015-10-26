# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('specimens', '0004_auto_20151023_1522'),
    ]

    operations = [
        migrations.AlterField(
            model_name='specimen',
            name='slug',
            field=models.SlugField(editable=False, unique=True, verbose_name='slug'),
        ),
    ]
