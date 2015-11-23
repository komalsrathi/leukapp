# django imports
from django.db import models
from django.conf import settings
from django.utils.translation import ugettext_lazy as _

# third party
from allauth.account.models import EmailAddress

# apps imports
from leukapp.apps.core.models import LeukappModel
from leukapp.apps.core.validators import phone_validator

# local imports
from . import constants


class Participant(LeukappModel):

    """docstring for Participant"""

    APP_NAME = constants.APP_NAME

    # external
    first_name = models.CharField(
        _("first name"),
        max_length=100,
        null=True,
        )
    last_name = models.CharField(
        _("last name"),
        max_length=100,
        null=True,
        )
    email = models.EmailField(
        _("email"),
        max_length=254,
        unique=True,
        null=True,
        )
    phone = models.CharField(
        _("phone"),
        max_length=15,
        validators=[phone_validator],
        blank=True,
        null=True,
        )

    # internal
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name=_("user"),
        null=True,
        blank=True
    )
    slug = models.SlugField(
        _("slug"),
        unique=True,
        editable=False,
        null=True,
        )

    class Meta:
        verbose_name = _(constants.APP_NAME[:-1])
        verbose_name_plural = _(constants.APP_NAME)

    def __str__(self):
        return self.slug

    def _if_save(self):
        """ _if_save is run everytime the object is saved"""

        # This function can only be called from save()
        self._check_if_caller_is_save()

        # see if there is any user with the email registered
        try:
            self.user = EmailAddress.objects.get(email__iexact=self.email).user
            self.first_name = self.user.first_name
            self.last_name = self.user.last_name
        except EmailAddress.DoesNotExist:
            pass

        # set slug
        self.slug = self.email
