# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20151023_1522'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='leukapptestmodel',
            name='slug',
        ),
    ]
