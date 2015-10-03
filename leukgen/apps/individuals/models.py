# django imports
from django.db import models
from django.utils.translation import ugettext_lazy as _

# apps imports
from leukgen.apps.core.models import LeukappModel

# local imports
from .constants import APP_NAME, CHOICES


class Individual(LeukappModel):

    """docstring for Individual"""

    APP_NAME = APP_NAME
    CHOICES = CHOICES

    institution = models.CharField(
        _("Individual's Institution"),
        max_length=3,
        choices=CHOICES["INSTITUTION"]
        )
    species = models.CharField(
        _("Individual's Species"),
        max_length=1,
        choices=CHOICES["SPECIES"]
        )

    class Meta:
        index_together = (("ext_id", "institution", "species"))
        unique_together = (("ext_id", "institution", "species"))

    def __str__(self):
        return self.slug

    def check_institution(self):
        if self.institution == 'MSK':
            return 'I'
        else:
            return 'E'

    def get_slug(self):
        return '-'.join(
            [self.check_institution(), self.species, self.get_int_id()]
        )

    def get_int_id(self):
        return str(self.pk + 100000)
