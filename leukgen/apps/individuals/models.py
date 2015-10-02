# django imports
from django.db import models
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _

# apps imports
from leukgen.apps.core.models import TimeStampedModel


class Individual(TimeStampedModel):

    """docstring for Individual"""

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
        _("Source Institution"),
        max_length=3,
        choices=INSTITUTION_CHOICES
        )
    species = models.CharField(
        _("Individual's species"),
        max_length=1,
        choices=SPECIES_CHOICES)
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
        _("Individual Leukid"),
        max_length=100,
        blank=True
        )

    class Meta:
        index_together = (("ext_id", "institution", "species"))
        unique_together = (("ext_id", "institution", "species"))

    def __str__(self):
        return self.get_leukid()

    def save(self, *args, **kwargs):
        """
        leukid and int_id requires pk for new objects,
        see: http://stackoverflow.com/questions/9940674/django-model-manager-objects-create-where-is-the-documentation
        """

        new = not self.pk
        super(Individual, self).save(*args, **kwargs)

        if new:
            # create() uses `force_insert`, which causes error.
            kwargs['force_insert'] = False

            self.int_id = self.get_int_id()
            self.leukid = self.get_leukid()
            super(Individual, self).save(*args, **kwargs)

    def check_institution(self):
        if self.institution == 'MSK':
            return 'I'
        else:
            return 'E'

    def get_absolute_url(self):
        return reverse('individuals:detail', kwargs={'leukid': self.leukid})

    def get_int_id(self):
        return str(self.pk + 100000)

    def get_leukid(self):
        return '-'.join(
            [self.check_institution(), self.species, self.get_int_id()]
        )
