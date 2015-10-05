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
        verbose_name=_("individual"),
        )
    source = models.CharField(
        _("source"),
        max_length=1,
        choices=CHOICES["SOURCE"]
        )
    aliquots_count = models.PositiveIntegerField(
        _("aliquot count"),
        )
    ext_id = models.CharField(
        _("external id"),
        max_length=100
        )
    int_id = models.PositiveIntegerField(
        _("internal id"),
        )

    class Meta:
        verbose_name = _(APP_NAME[:-1])
        verbose_name_plural = _(APP_NAME)

        index_together = (("ext_id", "source", "individual"))
        unique_together = (("ext_id", "source", "individual"))

    def __str__(self):
        return self.slug

    def if_new(self, **kwargs):
        """ if_new is executed the first time the object is created """

        # initialize child count
        self.aliquots_count = 0

        # alter parent count
        self.individual.specimens_count += 1
        self.individual.save()

        # store int_id
        self.int_id = self.individual.specimens_count

    def get_slug(self):
        """ get_slug is executed everytime the object is saved """

        return '-'.join([
            self.individual.slug,
            self.source,
            str(self.int_id)
            ])
