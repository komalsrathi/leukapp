# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import leukapp.apps.leukforms.validators


class Migration(migrations.Migration):

    dependencies = [
        ('leukforms', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leukform',
            name='submission',
            field=models.FileField(upload_to='leukform/submissions/%Y/%m', verbose_name='leukform', validators=[leukapp.apps.leukforms.validators.leukform_csv_validator]),
        ),
    ]
