# -*- coding: utf-8 -*-

# django
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.conf import settings
from django.core.files import File
from django.db.models.signals import post_delete
from django.dispatch.dispatcher import receiver

# leukapp
from leukapp.apps.core.models import LeukappModel
from leukapp.apps.individuals.models import Individual
from leukapp.apps.specimens.models import Specimen
from leukapp.apps.aliquots.models import Aliquot
from leukapp.apps.extractions.models import Extraction

# local
from .constants import APP_NAME
from .validators import leukform_csv_validator
from .utils import LeukformLoader


class Leukform(LeukappModel):

    """
    requirements: https://docs.google.com/spreadsheets/d/17TJ6zQ3OzwE-AZVZykFzzbHxtDM88aM7vvCPxJQ8-_M/edit#gid=2010180721
    """

    APP_NAME = APP_NAME

    # external fields
    description = models.CharField(
        _("description"),
        max_length=140,
        blank=True,
        help_text='This is for your future self.',
        null=True,
        )
    submission = models.FileField(
        upload_to='leukform/submissions/%Y/%m',
        verbose_name=_("leukform"),
        validators=[leukform_csv_validator],
        null=True,
        )
    result = models.FileField(
        upload_to='leukform/results/%Y/%m',
        verbose_name=_("sumbission result"),
        blank=True,
        null=True,
        )
    summary = models.TextField(
        _("summary"),
        blank=True,
        null=True,
        )
    mock = models.BooleanField(
        _("test leukform"),
        help_text='if True, records will not be saved.',
        default=False,
        null=True,
        )

    """ TENTATIVE
    created_individuals = models.ManyToManyField(
        Individual,
        verbose_name=_("created individuals"),
        blank=True,
        null=True,
        )
    created_specimens = models.ManyToManyField(
        Specimen,
        verbose_name=_("created specimens"),
        blank=True,
        null=True,
        )
    created_aliquots = models.ManyToManyField(
        Aliquot,
        verbose_name=_("created aliquots"),
        blank=True,
        null=True,
        )
    created_extractions = models.ManyToManyField(
        Extraction,
        verbose_name=_("created extractions"),
        blank=True,
        null=True,
        )
    """

    # internal
    slug = models.SlugField(
        _("slug"),
        unique=True,
        editable=False,
        null=True,
        )
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name=_("created by"),
        blank=True,
        null=True,
        )

    class Meta:
        verbose_name = _(APP_NAME[:-1])
        verbose_name_plural = _(APP_NAME)

    def __str__(self):
        return self.slug

    def _if_new(self, **kwargs):
        """ _if_new is executed the first time the object is created """

        # This function can only be called from save()
        self._check_if_caller_is_save()

        # validate is  False because it has already been validated
        loader = LeukformLoader()
        filepath = self.submission.file.name
        out = loader.submit(filepath=filepath, validate=False, mock=self.mock)

        # create result
        if self.mock:
            result_name = 'result-leukform-test-%s.csv' % self.pk
        else:
            result_name = 'result-leukform-%s.csv' % self.pk
        self.summary = out['summary']
        self.result = File(name=result_name, file=out['result'])

        # update slug
        self.slug = '-'.join(['leukform', str(self.pk)])

    def _if_save(self):
        """ _if_save() is executed everytime the object is saved """
        pass


@receiver(post_delete, sender=Leukform)
def leukform_delete(sender, instance, **kwargs):
    # Pass false so FileField doesn't save the model.
    instance.submission.delete(False)
    instance.result.delete(False)
