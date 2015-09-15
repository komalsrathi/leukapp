# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('principal_investigator', models.TextField(default='')),
                ('scientist', models.TextField(default='')),
                ('data_analyst', models.TextField(default='')),
                ('name', models.TextField(default='')),
                ('description', models.TextField(default='')),
            ],
        ),
    ]
