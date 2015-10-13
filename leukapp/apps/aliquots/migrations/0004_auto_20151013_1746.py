# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aliquots', '0003_auto_20151009_1704'),
    ]

    operations = [
        migrations.RenameField(
            model_name='aliquot',
            old_name='biological_material',
            new_name='bio_source',
        ),
    ]
