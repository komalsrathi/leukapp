# django imports
from django.db import models
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _

# apps imports
from leukgen.apps.core.models import TimeStampedModel


class Individual(TimeStampedModel):

    """docstring for Individual"""

    APP_NAME = 'individuals'

    MSK = 'MSK'
    OTHER = 'O'
    INSTITUTION_CHOICES = (
        (MSK, 'Memorial Sloan-Kettering Cancer Center'),
        (OTHER, 'Other'),
    )

    HUMAN = 'H'
    MOUSE = 'M'
    YEAST = 'Y'
    ZEBRAFISH = 'Z'
    SPECIES_CHOICES = (
        (HUMAN, 'Human'),
        (MOUSE, 'Mouse'),
        (YEAST, 'Yeast'),
        (ZEBRAFISH, 'Zebrafish'),
    )

    institution = models.CharField(
        _("Individual's Institution"),
        max_length=3,
        choices=INSTITUTION_CHOICES
        )
    species = models.CharField(
        _("Individual's Species"),
        max_length=1,
        choices=SPECIES_CHOICES)
    ext_id = models.CharField(
        _("Individual's External ID"),
        max_length=100
        )
    int_id = models.CharField(
        _("Individual's Internal ID"),
        max_length=7,
        blank=True
        )
    slug = models.CharField(
        _("Individual's Leukid"),
        max_length=100,
        blank=True
        )

    class Meta:
        index_together = (("ext_id", "institution", "species"))
        unique_together = (("ext_id", "institution", "species"))

    def __str__(self):
        return self.slug

    def save(self, *args, **kwargs):
        """
        slug and int_id requires pk for new objects,
        """

        new = not self.pk
        super(Individual, self).save(*args, **kwargs)

        # http://stackoverflow.com/questions/9940674/django-model-manager-objects-create-where-is-the-documentation
        if new:
            kwargs['force_insert'] = False  # set to avoid in error in create()
            self.int_id = self.get_int_id()
            self.slug = self.get_slug()
            super(Individual, self).save(*args, **kwargs)

    def check_institution(self):
        if self.institution == 'MSK':
            return 'I'
        else:
            return 'E'

    def get_absolute_url(self):
        return reverse(
            self.APP_NAME + ':detail', kwargs={'slug': self.slug}
        )

    def get_update_url(self):
        return reverse(
            self.APP_NAME + ':update', kwargs={'slug': self.slug}
        )

    def get_create_url(self):
        return reverse(
            self.APP_NAME + ':create', kwargs={'slug': self.slug}
        )

    def get_int_id(self):
        return str(self.pk + 100000)

    def get_slug(self):
        return '-'.join(
            [self.check_institution(), self.species, self.get_int_id()]
        )
