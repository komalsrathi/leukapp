# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('participants', '0002_participant_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='participant',
            name='slug',
            field=models.SlugField(editable=False, unique=True, max_length=100, verbose_name='slug'),
        ),
    ]
