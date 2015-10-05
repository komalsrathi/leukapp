# django imports
from django.db import models
from django.utils.translation import ugettext_lazy as _

# apps imports
from leukgen.apps.core.models import LeukappModel
from leukgen.apps.participants.models import Participant

# local imports
from .constants import APP_NAME


class Project(LeukappModel):

    """docstring for Project"""

    APP_NAME = APP_NAME

    name = models.CharField(
        _("name"),
        max_length=100
        )
    description = models.CharField(
        _("description"),
        max_length=140,
        )
    pi = models.ForeignKey(
        Participant,
        verbose_name=_("principal investigator"),
        related_name='projects_as_pi',
        )
    analyst = models.ForeignKey(
        Participant,
        verbose_name=_("data analyst"),
        related_name='projects_as_analyst',
        )
    requestor = models.ForeignKey(
        Participant,
        verbose_name=_("requestor"),
        related_name='projects_as_requestor',
        )
    participants = models.ManyToManyField(
        Participant,
        verbose_name=_("participants"),
        related_name='projects_participant',
        )
    cost_center_no = models.PositiveIntegerField(
        _("cost center number"),
        )
    fund_no = models.PositiveIntegerField(
        _("fund number"),
        )
    protocol_no = models.CharField(
        _("protocol number"),
        max_length=100,
        )

    class Meta:
        verbose_name = _(APP_NAME[:-1])
        verbose_name_plural = _(APP_NAME)

    def __str__(self):
        return self.slug

    def get_slug(self):
        """ get_slug is run everytime the object is saved"""

        # add pi, analyst and requestors as project participants
        self.participants.add(self.pi, self.analyst, self.requestor)

        # get_slug must return the slug
        return '-'.join(
            [self.pi.last_name, self.pk]
        )
