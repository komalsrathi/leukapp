# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('individuals', '0002_auto_20151002_1859'),
    ]

    operations = [
        migrations.RenameField(
            model_name='individual',
            old_name='leukid',
            new_name='slug',
        ),
    ]
