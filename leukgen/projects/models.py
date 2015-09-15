from django.db import models


class Project(models.Model):

    """docstring for Project"""

    principal_investigator = models.CharField(default='', max_length=100)
    scientist = models.CharField(default='', max_length=100)
    data_analyst = models.CharField(default='', max_length=100)
    name = models.CharField(default='', max_length=100)
    description = models.CharField(default='', max_length=100)
