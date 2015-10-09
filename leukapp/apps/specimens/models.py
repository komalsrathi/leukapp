# django imports
from django.db import models
from django.utils.translation import ugettext_lazy as _

# apps imports
from leukapp.apps.core.models import LeukappModel
from leukapp.apps.core.validators import ext_id_validator
from leukapp.apps.individuals.models import Individual

# local imports
from .constants import APP_NAME, SPECIMEN_CHOICES


class Specimen(LeukappModel):

    """docstring for Specimen"""

    APP_NAME = APP_NAME
    CHOICES = SPECIMEN_CHOICES

    # external fields
    individual = models.ForeignKey(
        Individual,
        verbose_name=_("individual"),
        )
    source = models.CharField(
        _("source"),
        max_length=1,
        choices=CHOICES["SOURCE"]
        )
    ext_id = models.CharField(
        _("external id"),
        max_length=100,
        validators=[ext_id_validator],  # test: test_ext_id_uses_validator
        help_text=_("The external id should be unique at the Individual "
            "and Source levels."),
        )

    # internal fields
    aliquots_created = models.PositiveIntegerField(
        _("number of aliquots created"),
        default=0
        )
    int_id = models.CharField(
        _("internal id"),
        max_length=8,
        null=True,
        )

    class Meta:
        verbose_name = _(APP_NAME[:-1])
        verbose_name_plural = _(APP_NAME)

        # test: test_unique_together_functionality
        unique_together = (("ext_id", "source", "individual"))
        index_together = (("ext_id", "source", "individual"))

    def __str__(self):
        return self.slug

    def if_new(self, **kwargs):
        """
        if_new is executed the first time the object is created
        tests:
            test_individual_specimens_created_keep_count_correctly
            test_specimens_created_is_correct_after_delete_specimens
            test_int_id_returns_expected_value
        """

        # alter individual specimens_created count
        self.individual.specimens_created += 1
        self.individual.save()

        self.aliquots_created = 0
        self.int_id = str(self.individual.specimens_created)

    def if_save(self):
        """
        if_save is executed everytime the object is saved
        test: test_str_returns_slug
        """

        self.slug = '-'.join([
            self.individual.slug,
            self.source,
            self.int_id])
