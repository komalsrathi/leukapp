# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('samples', '0002_auto_20150924_1904'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='individual',
            unique_together=set([('ext_id', 'source', 'species')]),
        ),
        migrations.AlterIndexTogether(
            name='individual',
            index_together=set([('ext_id', 'source', 'species')]),
        ),
    ]
