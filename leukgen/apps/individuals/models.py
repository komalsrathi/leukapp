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
        choices=INSTITUTION_CHOICES)
    species = models.CharField(
        _("Individual's species"),
        max_length=1,
        choices=SPECIES_CHOICES)
    ext_id = models.CharField(
        _("External ID"),
        max_length=100)

    class Meta:
        index_together = (("ext_id", "institution", "species"))
        unique_together = (("ext_id", "institution", "species"))

    def __str__(self):
        return '-'.join([self.species, self.int_id()])

    def save(self, *args, **kwargs):
        super(Individual, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('specimens:detail', kwargs={'int_id': self.int_id()})

    def check_institution(self):
        if self.institution == 'MSK':
            return 'I'
        else:
            return 'E'

    def int_id(self):
        return str(self.pk + 100000)
