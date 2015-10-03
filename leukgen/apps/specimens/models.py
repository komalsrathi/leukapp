# django imports
from django.db import models
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _

# apps imports
from leukgen.apps.core.models import TimeStampedModel
from leukgen.apps.individuals.models import Individual


class Specimen(TimeStampedModel):

    """docstring for Specimen"""

    APP_NAME = 'specimens'

    TUMOR = 'T'
    NORMAL = 'N'
    SOURCE_CHOICES = (
        (TUMOR, 'Tumor'),
        (NORMAL, 'Normal'),
    )

    individual = models.ForeignKey(
        Individual,
        )
    source = models.CharField(
        _("Source Code"),
        max_length=1,
        choices=SOURCE_CHOICES
        )
    ext_id = models.CharField(
        _("External ID"),
        max_length=100
        )
    int_id = models.CharField(
        _("Internal ID"),
        max_length=7,
        blank=True
        )
    leukid = models.CharField(
        _("Specimen's Leukid"),
        max_length=100,
        blank=True
        )

    # field candidates:
    # cell_type

    class Meta:
        index_together = (("ext_id", "source", "individual"))
        unique_together = (("ext_id", "source", "individual"))

    def __str__(self):
        return str(self.int_id())

    def save(self, *args, **kwargs):
        """
        leukid and int_id requires pk for new objects,
        """

        new = not self.pk
        super(Specimen, self).save(*args, **kwargs)

        # http://stackoverflow.com/questions/9940674/django-model-manager-objects-create-where-is-the-documentation
        if new:
            kwargs['force_insert'] = False # set to avoid in error in create()
            self.int_id = self.get_int_id()
            self.leukid = self.get_leukid()
            super(Specimen, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse(
            self.APP_NAME + ':detail', kwargs={'slug': self.leukid}
        )

    def get_update_url(self):
        return reverse(
            self.APP_NAME + ':update', kwargs={'slug': self.leukid}
        )

    def get_int_id(self):
        return str(self.pk)

    def get_leukid(self):
        return '-'.join(
            [self.check_institution(), self.species, self.get_int_id()]
        )
