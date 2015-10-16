# -*- coding: utf-8 -*-

# django
from django.db import models
from django.utils.translation import ugettext_lazy as _

# leukapp
from leukapp.apps.core.models import LeukappModel
from leukapp.apps.core.validators import ext_id_validator
from leukapp.apps.aliquots.models import Aliquot
from leukapp.apps.projects.models import Project

# local
from .constants import APP_NAME, SAMPLE_CHOICES


class Sample(LeukappModel):

    """
    requirements: https://docs.google.com/spreadsheets/d/17TJ6zQ3OzwE-AZVZykFzzbHxtDM88aM7vvCPxJQ8-_M/edit#gid=2010180721
    """

    APP_NAME = APP_NAME
    CHOICES = SAMPLE_CHOICES

    # external fields
    aliquot = models.ForeignKey(
        Aliquot,
        verbose_name=_("aliquot"),
        )
    projects = models.ManyToManyField(
        Project,
        verbose_name=_("projects"),
        blank=True,
        )
    platform = models.CharField(
        _("platform"),
        max_length=30,
        choices=CHOICES["PLATFORM"]
        )
    technology = models.CharField(
        _("technology"),
        max_length=30,
        choices=CHOICES["TECHNOLOGY"]
        )
    center = models.CharField(
        _("sequencing center"),
        max_length=10,
        choices=CHOICES["CENTER"]
        )
    ext_id = models.CharField(
        _("sequencing center id"),
        max_length=100,
        validators=[ext_id_validator],  # test: test_ext_id_uses_validator
        help_text=_("The sequencing center id should be unique at the "
            "Institution and Species levels."),
        )

    # internal fields
    int_id = models.CharField(
        _("internal id"),
        max_length=8,
        null=True,
        )

    class Meta:
        verbose_name = _(APP_NAME[:-1])
        verbose_name_plural = _(APP_NAME)

        # test: test_unique_together_functionality
        unique_together = (("ext_id", "aliquot"))
        index_together = (("ext_id", "aliquot"))

    def __str__(self):
        return self.slug

    def if_new(self, **kwargs):
        """
        if_new is executed the first time the object is created
        tests:
            test_if_new_initializes_specimen_count_with_zero
            test_int_id_returns_expected_value
        """

        # alter parent count
        self.aliquot.samples_created += 1
        self.aliquot.save()

        # store int_id
        self.int_id = str(self.aliquot.samples_created)

    def if_save(self):
        """
        if_save() is executed everytime the object is saved
        test: test_str_returns_leukid
        """

        # update slug
        self.slug = '-'.join([
            self.aliquot.slug,
            self.int_id,
            ])
