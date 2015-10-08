# -*- coding: utf-8 -*-

# django
from django.db import models
from django.utils.translation import ugettext_lazy as _

# leukapp
from leukapp.apps.core.models import LeukappModel

# local
from .constants import APP_NAME, INDIVIDUAL_CHOICES


class Individual(LeukappModel):

    """docstring for Individual"""

    APP_NAME = APP_NAME
    CHOICES = INDIVIDUAL_CHOICES

    # external fields
    institution = models.CharField(
        _("individual's institution"),
        max_length=3,
        choices=CHOICES["INSTITUTION"]
        )
    species = models.CharField(
        _("individual's species"),
        max_length=1,
        choices=CHOICES["SPECIES"]
        )
    ext_id = models.CharField(
        _("external id"),
        max_length=100,
        )

    # internal fields
    specimens_count = models.PositiveIntegerField(
        _("aliquot count"),
        default=0,
        )
    int_id = models.PositiveIntegerField(
        _("internal id"),
        null=True,
        )

    class Meta:
        verbose_name = _(APP_NAME[:-1])
        verbose_name_plural = _(APP_NAME)

        index_together = (("ext_id", "institution", "species"))
        unique_together = (("ext_id", "institution", "species"))

    def __str__(self):
        return self.slug

    def check_institution(self):
        if self.institution == 'MSK':
            return 'I'
        else:
            return 'E'

    def get_int_id(self):
        int_id = self.pk + 100000
        return int_id

    def if_new(self, **kwargs):
        """ if_new is executed the first time the object is created """

        # initialize child count
        self.specimens_count = 0

        # get internal id
        self.int_id = self.get_int_id()

    def get_slug(self):
        """ get_slug is executed everytime the object is saved """

        return '-'.join([
            self.check_institution(),
            self.species,
            str(self.int_id)]
        )
