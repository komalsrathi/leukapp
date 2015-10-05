# django imports
from django.db import models
from django.utils.translation import ugettext_lazy as _

# apps imports
from leukgen.apps.core.models import LeukappModel
from leukgen.apps.specimens.models import Specimen

# local imports
from .constants import APP_NAME, CHOICES


class Aliquot(LeukappModel):

    """docstring for Aliquot"""

    APP_NAME = APP_NAME

    specimen = models.ForeignKey(
        Specimen,
        verbose_name=_("specimen"),
        )
    biological_material = models.CharField(
        _("biological material"),
        max_length=1,
        choices=CHOICES["BIOLOGICAL_MATERIAL"]
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

        index_together = (("ext_id", "biological_material", "specimen"))
        unique_together = (("ext_id", "biological_material", "specimen"))

    def __str__(self):
        return self.slug

    def if_new(self, **kwargs):
        """ if_new is executed the first time the object is created """

        # alter parent count
        self.specimen.aliquots_count += 1
        self.specimen.save()

        # store int_id
        self.int_id = self.specimen.aliquots_count

    def get_slug(self):
        """ get_slug is always excecuted when saving """

        return '-'.join([
            self.specimen.slug,
            self.biological_material,
            str(self.int_id)
            ])
