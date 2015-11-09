from django.db import models


class List(models.Model):

    """docstring for List"""

    pass


class Item(models.Model):

    """docstring for Item"""

    text = models.TextField(blank=True, default='list')
    list = models.ForeignKey(List, null=True, blank=True, default=None)
