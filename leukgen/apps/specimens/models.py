# django imports
from django.db import models
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _

# apps imports
from core.models import TimeStampedModel
from individuals.models import Individual


class Specimen(TimeStampedModel):

    '''docstring for Specimen'''

    TUMOR = 'T'
    NORMAL = 'N'
    SOURCE_CHOICES = (
        (TUMOR, 'Tumor'),
        (NORMAL, 'Normal'),
    )

    individual = models.ForeignKey(Individual)
    source = models.CharField(
        _("Source Code"), max_length=1, choices=SOURCE_CHOICES)
    ext_id = models.CharField(max_length=100)

    # field candidates:
    # cell_type

    class Meta:
        index_together = (("ext_id", "source", "individual"))
        unique_together = (("ext_id", "source", "individual"))

    def __str__(self):
        return str(self.int_id())

    def save(self, *args, **kwargs):
        super(Specimen, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('specimens:detail', kwargs={'int_id': self.int_id()})

    def int_id(self):
        return self.pk
