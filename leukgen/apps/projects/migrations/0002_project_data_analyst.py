# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='data_analyst',
            field=models.ForeignKey(blank=True, related_name='projects_as_data_analyst', to=settings.AUTH_USER_MODEL, verbose_name='data analyst', null=True),
        ),
    ]
