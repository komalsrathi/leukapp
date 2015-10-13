# -*- coding: utf-8 -*-

# django imports
from django.db import models
from django.utils.translation import ugettext_lazy as _

# apps imports
from leukapp.apps.core.models import LeukappModel
from leukapp.apps.core.validators import ext_id_validator
from leukapp.apps.specimens.models import Specimen

# local imports
from .constants import APP_NAME, ALIQUOT_CHOICES


class AliquotAbstractModel(LeukappModel):

    """
    This is an Abstract Model because its also used to create
    pseudo Aliquots.

    Pseudo Aliquots are used to validate new data whithout creating
    new objects. see the leukgen.apps.samples application

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
        validators=[ext_id_validator],  # test: test_ext_id_uses_validator
        help_text=_("The external id should be unique at the Specimen level."),
        )

    # internal fields
    int_id = models.CharField(
        _("internal id"),
        max_length=8,
        null=True,
        )

    class Meta:
        abstract = True

        verbose_name = _(APP_NAME[:-1])
        verbose_name_plural = _(APP_NAME)

        # test: test_unique_together_functionality
        unique_together = (("ext_id", "specimen"))
        index_together = (("ext_id", "specimen"))

    def __str__(self):
        return self.slug

    def if_new(self, **kwargs):
        """
        if_new is executed the first time the object is created
        tests:
            test_if_new_adds_one_to_specimen_aliquots_created
            test_if_specimens_created_keep_count_correctly

        """

        # alter parent count
        self.specimen.aliquots_created += 1
        self.specimen.save()

        # store int_id
        self.int_id = str(self.specimen.aliquots_created)

    def if_save(self):
        """
        if_save is always excecuted when saving
        test: test_str_returns_slug
        """

        self.slug = '-'.join([
            self.specimen.slug,
            self.bio_source,
            self.int_id
            ])


class Aliquot(AliquotAbstractModel):

    """
    Main Aliquot Model
    """
