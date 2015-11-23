# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.contrib.sites.models


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0004_auto_20151027_1901'),
    ]

    operations = [
        migrations.AlterField(
            model_name='site',
            name='domain',
            field=models.CharField(verbose_name='domain name', validators=[django.contrib.sites.models._simple_domain_name_validator], max_length=100),
        ),
    ]
