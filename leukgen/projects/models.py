# django imports
from django.db import models
from django.conf import settings
from django.utils.translation import ugettext_lazy as _

# apps imports
from core.models import TimeStampedModel


class Project(TimeStampedModel):

    """docstring for Project"""

    # fields
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100, default='')
    pi = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name=_("principal investigator"),
        related_name='projects_as_pi',
    )
    scientist = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name=_("scientist"),
        related_name='projects_as_scientist',
        null=True,
        blank=True
    )
    data_analyst = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name=_("data analyst"),
        related_name='projects_as_data_analyst',
        null=True,
        blank=True
    )

    """ prospect fields
    sequencing_center_project_id
    biospecimen_protocol
    """
