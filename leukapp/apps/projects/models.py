# django imports
from django.db import models
from django.utils.translation import ugettext_lazy as _

# apps imports
from leukapp.apps.core.models import LeukappModel
from leukapp.apps.core.validators import object_name_validator
from leukapp.apps.participants.models import Participant

# local imports
from .constants import APP_NAME


class Project(LeukappModel):

    """docstring for Project"""

    APP_NAME = APP_NAME

    name = models.CharField(
        _("project name"),
        max_length=100,
        validators=[object_name_validator]
        )
    description = models.CharField(
        _("project description"),
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
        related_name='projects_as_participant',
        blank=True,
        )
    cost_center_no = models.CharField(
        _("cost center number"),
        max_length=100,
        )
    fund_no = models.CharField(
        _("fund number"),
        max_length=100,
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

    def if_save(self):
        """ if_save() is run everytime the object is saved"""

        # add pi, analyst and requestors as project participants
        self.participants.add(self.pi, self.analyst, self.requestor)

        # if_save() must return the slug
        self.slug = str(self.pk)
