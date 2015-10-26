# -*- coding: utf-8 -*-

# django
from django.db import models
from django.utils.translation import ugettext_lazy as _

# leukapp
from leukapp.apps.core.models import LeukappModel
from leukapp.apps.core.validators import ext_id_validator

# local
from .constants import APP_NAME, INDIVIDUAL_CHOICES


class Individual(LeukappModel):

    """
    This is an Abstract Model because its also used to create
    pseudo Individuals.

    Pseudo Individuals are used to validate new data whithout creating
    new objects. see the leukgen.apps.samples application

    requirements: https://docs.google.com/spreadsheets/d/17TJ6zQ3OzwE-AZVZykFzzbHxtDM88aM7vvCPxJQ8-_M/edit#gid=288765627
    """

    APP_NAME = APP_NAME
    CHOICES = INDIVIDUAL_CHOICES

    # external fields
    institution = models.CharField(
        _("institution"),
        max_length=3,
        choices=CHOICES["INSTITUTION"]
        )
    species = models.CharField(
        _("species"),
        max_length=1,
        choices=CHOICES["SPECIES"],
        )
    ext_id = models.CharField(
        _("external id"),
        max_length=100,
        validators=[ext_id_validator],  # test: test_ext_id_uses_validator
        help_text=_("The external id should be unique at the "
            "Institution and Species levels."),
        )

    # internal fields
    tumors_count = models.PositiveSmallIntegerField(
        _("number of tumor specimens created"),
        default=0,
        editable=False,
        )
    normals_count = models.PositiveSmallIntegerField(
        _("number of normal specimens created"),
        default=0,
        editable=False,
        )
    int_id = models.CharField(
        _("internal id"),
        max_length=8,
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

        # test: test_unique_together_functionality
        unique_together = (("ext_id", "institution", "species"))
        index_together = (("ext_id", "institution", "species"))

    def __str__(self):
        return self.slug

    def check_institution(self):
        """
        Determines whether or not the Individual comes from MSK or not.
        tests:
            test_check_institution_return_internal
            test_check_institution_return_external
        """

        if self.institution == 'MSK':
            return 'I'
        else:
            return 'E'

    def if_new(self, **kwargs):
        """
        if_new is executed the first time the object is created
        tests:
            test_if_new_initializes_specimen_count_with_zero
            test_int_id_returns_expected_value
        """

        # initializes count of normal and tumors
        self.tumors_count = 0
        self.normals_count = 0

        # gets internal id
        self.get_int_id()

    def if_save(self):
        """
        if_save() is executed everytime the object is saved
        test: test_str_returns_leukid
        """

        # update slug
        self.slug = '-'.join([
            self.check_institution(),
            self.int_id
            ])

    def get_int_id(self):
        """ returns Individual internal ID """
        self.int_id = self.species + str(self.pk + 100000)
        return self.int_id
