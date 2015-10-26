# -*- coding: utf-8 -*-

# django imports
from django.db import models
from django.utils.translation import ugettext_lazy as _

# apps imports
from leukapp.apps.core.models import LeukappModel
from leukapp.apps.core.validators import ext_id_validator
from leukapp.apps.specimens.models import Specimen

# local imports
from .constants import APP_NAME, ALIQUOT_CHOICES, DNA, RNA


class Aliquot(LeukappModel):

    """
    requirements: https://docs.google.com/spreadsheets/d/17TJ6zQ3OzwE-AZVZykFzzbHxtDM88aM7vvCPxJQ8-_M/edit#gid=365039979
    """

    APP_NAME = APP_NAME
    CHOICES = ALIQUOT_CHOICES

    # external fields
    specimen = models.ForeignKey(
        Specimen,
        verbose_name=_("specimen"),
        )
    bio_source = models.CharField(
        _("biological material"),
        max_length=1,
        choices=CHOICES["BIO_SOURCE"]
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
        max_length=8,
        null=True,
        editable=False,
        )
    runs_count = models.PositiveSmallIntegerField(
        _("number of samples created"),
        default=0,
        editable=False,
        )
    slug = models.SlugField(
        _("slug"),
        unique=True,
        editable=False,
        )

    class Meta:
        verbose_name = _(APP_NAME[:-1])
        verbose_name_plural = _(APP_NAME)
        unique_together = (("ext_id", "specimen"))
        index_together = (("ext_id", "specimen"))

    def __str__(self):
        return self.slug

    def if_new(self, **kwargs):
        """ if_new is executed the first time the object is created """
        self.runs_count = 0
        self.get_int_id()

    def if_save(self):
        """ if_save is always excecuted when saving """
        self.slug = '-'.join([self.specimen.slug, self.int_id])

    def get_int_id(self):
        """ return int_id based on count of tumors/normals per Individual """
        if self.bio_source == DNA:
            self.specimen.dna_count += 1
            self.int_id = self.bio_source + str(self.specimen.dna_count)
        elif self.bio_source == RNA:
            self.specimen.rna_count += 1
            self.int_id = self.bio_source + str(self.specimen.rna_count)
        self.specimen.save()
        return self.int_id
