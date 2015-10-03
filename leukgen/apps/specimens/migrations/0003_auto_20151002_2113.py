# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('specimens', '0002_auto_20151002_1901'),
    ]

    operations = [
        migrations.RenameField(
            model_name='specimen',
            old_name='leukid',
            new_name='slug',
        ),
    ]
