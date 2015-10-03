# django imports
from django.db import models
from django.utils.translation import ugettext_lazy as _

# apps imports
from leukgen.apps.core.models import LeukappModel
from leukgen.apps.individuals.models import Individual

# local imports
from .constants import APP_NAME, CHOICES


class Specimen(LeukappModel):

    """docstring for Specimen"""

    APP_NAME = APP_NAME

    individual = models.ForeignKey(
        Individual,
        )
    source = models.CharField(
        _("Source Code"),
        max_length=1,
        choices=CHOICES["SOURCE"]
        )

    # field candidates:
    # cell_type

    class Meta:
        index_together = (("ext_id", "source", "individual"))
        unique_together = (("ext_id", "source", "individual"))

    def __str__(self):
        return self.slug

    def get_slug(self):
        return '-'.join(
            [self.individual.slug, self.source, str(self.pk)]
        )
