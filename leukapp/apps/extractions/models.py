# -*- coding: utf-8 -*-

# django
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.conf import settings
from django.core.exceptions import ImproperlyConfigured

# leukapp
from leukapp.apps.core.models import LeukappModel
from leukapp.apps.core.validators import ext_id_validator
from leukapp.apps.core.utils import LeukConnect
from leukapp.apps.core.constants import UNKNOWN
from leukapp.apps.aliquots.models import Aliquot
from leukapp.apps.projects.models import Project

# local
from . import constants
from .validators import projects_string_validator


class Extraction(LeukappModel):

    """

    :param aliquot: Parent `~leukapp.apps.aliquots.models.Aliquot` object.
    :param analyte:
    :param platform:
    :param technology:
    :param center:
    :param ext_id:
    :param projects_string:
    :param projects:

    """

    APP_NAME = constants.APP_NAME
    CHOICES = constants.EXTRACTION_CHOICES

    # external fields
    aliquot = models.ForeignKey(
        Aliquot,
        verbose_name=_("aliquot"),
        null=True,
        )
    analyte = models.CharField(
        _("biological material"),
        max_length=100,
        choices=CHOICES["ANALYTE"],
        null=True,
        )
    projects = models.ManyToManyField(
        Project,
        verbose_name=_("projects"),
        blank=True,
        null=True,
        )
    projects_string = models.CharField(
        _("list of projetcs"),
        max_length=100,
        validators=[projects_string_validator],
        help_text=_("Include the projects pks separated by a '|' character"),
        blank=True,
        null=True,
        )
    platform = models.CharField(
        _("platform"),
        max_length=100,
        choices=CHOICES["PLATFORM"],
        null=True,
        )
    technology = models.CharField(
        _("technology"),
        max_length=100,
        choices=CHOICES["TECHNOLOGY"],
        null=True,
        )
    center = models.CharField(
        _("sequencing center"),
        max_length=100,
        choices=CHOICES["CENTER"],
        null=True,
        )
    ext_id = models.CharField(
        _("sequencing center id"),
        max_length=100,
        validators=[ext_id_validator],
        default=UNKNOWN,
        help_text=_("The sequencing center id."),
        null=True,
        )

    # internal fields
    int_id = models.CharField(
        _("internal id"),
        max_length=100,
        null=True,
        )
    slug = models.SlugField(
        _("slug"),
        unique=True,
        editable=False,
        null=True,
        )

    class Meta:
        verbose_name = _(constants.APP_NAME[:-1])
        verbose_name_plural = _(constants.APP_NAME)
        unique_together = (constants.EXTRACTION_UNIQUE_TOGETHER)
        index_together = (constants.EXTRACTION_UNIQUE_TOGETHER)

    def __str__(self):
        return self.slug

    def _if_new(self, **kwargs):
        """ _if_new is executed the first time the object is created """

        # This function can only be called from save()
        self._check_if_caller_is_save()

        # get internal id
        self.int_id = self._get_int_id()

    def _if_save(self):
        """ NOTTESTED _if_save() is executed everytime the object is saved """

        # This function can only be called from save()
        self._check_if_caller_is_save()

        # update object slug
        self.slug = '-'.join([self.aliquot.slug, self.int_id])

        # update projects
        self._get_projects_from_string()

        # update data center
        self._create_leukcd_run_dir()

    def _get_projects_from_string(self):
        """ NOTTESTED NOTDOCUMENTED """
        if self.projects_string:
            projects = [int(p) for p in self.projects_string.split("|")]
            [self.projects.add(p) for p in projects]

    def _get_int_id(self):
        """ return int_id based on count of tumors/normals per Individual """

        # This function can only be called from _if_new()
        self._check_if_caller_is_if_new()

        # get internal id
        analyte_id = constants.LEUKID_ANALYTE[self.analyte]
        if self.analyte == constants.DNA:
            self.aliquot.dna_extractions_count += 1
            self.int_id = analyte_id + str(self.aliquot.dna_extractions_count)
        elif self.analyte == constants.RNA:
            self.aliquot.rna_extractions_count += 1
            self.int_id = analyte_id + str(self.aliquot.rna_extractions_count)
        self.aliquot.save()
        return self.int_id

    def _create_leukcd_run_dir(self):
        """ This function ssh to leukdc and creates a run directory."""
        # NOTTESTED

        if settings.TESTING:
            return

        try:  # if LEUKCD_ACTIVE is TRUE, creates a dir at the Data Center
            leukcd = LeukConnect()
            projects = self.projects.all()

            # root directories
            projectsroot = leukcd.LEUKDC_PROJECTS_DIR
            samplesroot = leukcd.LEUKDC_SAMPLES_DIR

            # specific paths
            projectspathlist = [self.technology, self.slug]
            samplespathlist = [self.slug]
            pdirs = ['/'.join([p.int_id] + projectspathlist) for p in projects]
            pdirs = [projectsroot + pdir for pdir in pdirs]
            sdir = samplesroot + '/'.join(samplespathlist)

            # create sample directory
            leukcd.connect()
            command = 'mkdir -p %s' % sdir
            leukcd.exec_command(command)

            # create directories at projects
            command = 'mkdir -p {0}'
            [leukcd.exec_command(command.format(pdir)) for pdir in pdirs]

            # create symlinks from samples to projects
            command = 'ln -s {0} {1}'
            [leukcd.exec_command(command.format(sdir, pdir)) for pdir in pdirs]

            # close connection
            leukcd.close()
        except ImproperlyConfigured:
            print('LEUKCD_ACTIVE is FALSE')
