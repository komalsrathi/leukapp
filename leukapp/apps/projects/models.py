# django imports
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.conf import settings

# apps imports
from leukapp.apps.core.models import LeukappModel
from leukapp.apps.core.validators import object_name_validator
from leukapp.apps.core.utils import LeukConnect
from leukapp.apps.participants.models import Participant

# local imports
from . import constants


class Project(LeukappModel):

    """
    requirements= https://docs.google.com/spreadsheets/d/17TJ6zQ3OzwE-AZVZykFzzbHxtDM88aM7vvCPxJQ8-_M/edit#gid=0
    """

    APP_NAME = constants.APP_NAME

    # external
    title = models.CharField(
        _("project title"),
        max_length=100,
        validators=[object_name_validator],
        unique=True,
        )
    description = models.CharField(
        _("project description"),
        max_length=140,
        )
    pi = models.ForeignKey(
        Participant,
        verbose_name=_("principal investigator"),
        related_name='projects_as_pi',
        help_text='Laboratory head or principal investigator'
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

    # internal
    slug = models.SlugField(
        _("slug"),
        unique=True,
        editable=False,
        )
    int_id = models.SlugField(
        _("int_id"),
        unique=True,
        editable=False,
        )
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name=_("created by"),
        null=True,
        blank=True
        )

    class Meta:
        verbose_name = _(constants.APP_NAME[:-1])
        verbose_name_plural = _(constants.APP_NAME)

    def __str__(self):
        return self.slug

    def _if_new(self):
        """ ran when object is created """

        # This function can only be called from save()
        self._check_if_caller_is_save()

        # get internal id
        self.int_id = str(self.pk + 100)

        # create project folder at leukdc
        self._create_leukc_project_dir()

    def _if_save(self):
        """ _if_save() is run everytime the object is saved"""

        # This function can only be called from save()
        self._check_if_caller_is_save()

        # update object slug
        self.slug = self.int_id

        # update paticipants
        self.participants.add(self.pi, self.analyst, self.requestor)

    def _create_leukc_project_dir(self):
        """ This function ssh to leukdc and creates a project directory."""

        leukcd = LeukConnect()

        # set project directory
        if settings.TESTING:
            directory = leukcd.LEUKDC_PROJECTS_DIR + '/tests/' + self.int_id
        else:
            directory = leukcd.LEUKDC_PROJECTS_DIR + '/' + self.int_id

        try:
            leukcd.connect()
            command = 'mkdir -p %s' % directory
            leukcd.exec_command(command)
            leukcd.close()
        except Exception as e:
            print(e)
