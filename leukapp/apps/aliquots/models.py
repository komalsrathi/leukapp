# -*- coding: utf-8 -*-

# django imports
from django.db import models
from django.utils.translation import ugettext_lazy as _

# apps imports
from leukapp.apps.core.models import LeukappModel
from leukapp.apps.core.validators import ext_id_validator
from leukapp.apps.specimens.models import Specimen

# local imports
from . import constants


class Aliquot(LeukappModel):

    """
    requirements: https://docs.google.com/spreadsheets/d/17TJ6zQ3OzwE-AZVZykFzzbHxtDM88aM7vvCPxJQ8-_M/edit#gid=288765627
    """

    APP_NAME = constants.APP_NAME
    CHOICES = constants.ALIQUOT_CHOICES

    # external fields
    specimen = models.ForeignKey(
        Specimen,
        verbose_name=_("specimen"),
        )
    ext_id = models.CharField(
        _("external id"),
        max_length=100,
        validators=[ext_id_validator],
        help_text=_("The external id should be unique at the Specimen level."),
        )

    # internal fields
    int_id = models.CharField(
        _("internal id"),
        max_length=100,
        null=True,
        editable=False,
        )
    dna_runs_count = models.PositiveSmallIntegerField(
        _("number of runs created"),
        default=0,
        editable=False,
        )
    rna_runs_count = models.PositiveSmallIntegerField(
        _("number of runs created"),
        default=0,
        editable=False,
        )
    slug = models.SlugField(
        _("slug"),
        unique=True,
        editable=False,
        )

    class Meta:
        verbose_name = _(constants.APP_NAME[:-1])
        verbose_name_plural = _(constants.APP_NAME)
        unique_together = (constants.ALIQUOT_UNIQUE_TOGETHER)
        index_together = (constants.ALIQUOT_UNIQUE_TOGETHER)

    def __str__(self):
        return self.slug

    def _if_new(self, **kwargs):
        """ _if_new is executed the first time the object is created """
        self._get_int_id()

    def _if_save(self):
        """ _if_save is always excecuted when saving """
        self.slug = '-'.join([self.specimen.slug, self.int_id])

    def _get_int_id(self):
        """ return int_id based on count of Aliquots per Specimen """
        self.specimen.aliquots_count += 1
        self.int_id = self.specimen.aliquots_count
        self.specimen.save()
        return self.int_id
