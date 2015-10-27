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
from .constants import APP_NAME


class Participant(LeukappModel):

    """docstring for Participant"""

    APP_NAME = APP_NAME

    # external
    first_name = models.CharField(
        _("first name"),
        max_length=100,
        )
    last_name = models.CharField(
        _("last name"),
        max_length=100,
        )
    email = models.EmailField(
        _("email"),
        max_length=254,
        unique=True,
        )
    phone = models.CharField(
        _("phone"),
        max_length=15,
        validators=[phone_validator],
        blank=True
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
        )

    class Meta:
        verbose_name = _(APP_NAME[:-1])
        verbose_name_plural = _(APP_NAME)

    def __str__(self):
        return self.slug

    def if_save(self):
        """ if_save is run everytime the object is saved"""

        # see if there is any user with the email registered
        try:
            self.user = EmailAddress.objects.get(email__iexact=self.email).user
            self.first_name = self.user.first_name
            self.last_name = self.user.last_name
        except EmailAddress.DoesNotExist:
            pass
        self.slug = self.email
