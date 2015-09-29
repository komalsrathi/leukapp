# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('samples', '0003_auto_20150925_1716'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Aliquot',
        ),
        migrations.DeleteModel(
            name='Specimen',
        ),
    ]
