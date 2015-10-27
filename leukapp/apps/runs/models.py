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
from . import constants


class Run(LeukappModel):

    """
    requirements: https://docs.google.com/spreadsheets/d/17TJ6zQ3OzwE-AZVZykFzzbHxtDM88aM7vvCPxJQ8-_M/edit#gid=2010180721
    """

    APP_NAME = constants.APP_NAME
    CHOICES = constants.RUN_CHOICES

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
        validators=[ext_id_validator],
        help_text=_("The sequencing center id should be unique at the "
            "Aliquot level."),
        )
    order = models.PositiveSmallIntegerField(
        _("desired order"),
        default=0,
        )

    # internal fields
    int_id = models.CharField(
        _("internal id"),
        max_length=8,
        null=True,
        )
    slug = models.SlugField(
        _("slug"),
        unique=True,
        editable=False,
        )

    class Meta:
        verbose_name = _(constants.APP_NAME[:-1])
        verbose_name_plural = _(constants.APP_NAME)
        unique_together = (constants.RUN_UNIQUE_TOGETHER)
        index_together = (constants.RUN_UNIQUE_TOGETHER)

    def __str__(self):
        return self.slug

    def if_new(self, **kwargs):
        """ if_new is executed the first time the object is created """
        self.aliquot.runs_count += 1
        self.aliquot.save()
        self.int_id = str(self.aliquot.runs_count)

    def if_save(self):
        """ if_save() is executed everytime the object is saved """
        self.slug = '-'.join([self.aliquot.slug, self.int_id])
