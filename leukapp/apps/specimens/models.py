# -*- coding: utf-8 -*-

# django imports
from django.db import models
from django.utils.translation import ugettext_lazy as _

# apps imports
from leukapp.apps.core.models import LeukappModel
from leukapp.apps.core.validators import ext_id_validator
from leukapp.apps.individuals.models import Individual

# local imports
from . import constants


class Specimen(LeukappModel):

    """
    requirements: https://docs.google.com/spreadsheets/d/17TJ6zQ3OzwE-AZVZykFzzbHxtDM88aM7vvCPxJQ8-_M/edit#gid=1125452971
    """

    APP_NAME = constants.APP_NAME
    CHOICES = constants.SPECIMEN_CHOICES

    # external fields
    individual = models.ForeignKey(
        Individual,
        verbose_name=_("individual"),
        )
    source = models.CharField(
        _("source"),
        max_length=100,
        blank=True,
        choices=CHOICES["SOURCE"]
        )
    source_type = models.CharField(
        _("source_type"),
        max_length=100,
        choices=CHOICES["SOURCE_TYPE"]
        )
    ext_id = models.CharField(
        _("external id"),
        max_length=100,
        validators=[ext_id_validator],
        help_text=_("The external id should be unique at the Individual "
            "and Source levels."),
        )

    # internal fields
    dna_count = models.PositiveSmallIntegerField(
        _("number of aliquots created"),
        default=0,
        editable=False,
        )
    rna_count = models.PositiveSmallIntegerField(
        _("number of aliquots created"),
        default=0,
        editable=False,
        )
    int_id = models.CharField(
        _("internal id"),
        max_length=8,
        null=True,
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
        unique_together = (constants.SPECIMEN_UNIQUE_TOGETHER)
        index_together = (constants.SPECIMEN_UNIQUE_TOGETHER)

    def __str__(self):
        return self.slug

    def if_new(self, **kwargs):
        """ if_new is executed the first time the object is created """
        self.dna_count = 0
        self.rna_count = 0
        self.get_int_id()

    def if_save(self):
        """ if_save is executed everytime the object is saved """
        self.slug = '-'.join([self.individual.slug, self.int_id])

    def get_int_id(self):
        """ return int_id based on count of tumors/normals per Individual """
        if self.source_type == constants.TUMOR:
            self.individual.tumors_count += 1
            self.int_id = self.source_type + str(self.individual.tumors_count)
        elif self.source_type == constants.NORMAL:
            self.individual.normals_count += 1
            self.int_id = self.source_type + str(self.individual.normals_count)
        self.individual.save()
        return self.int_id
