# -*- coding: utf-8 -*-
# python
from __future__ import unicode_literals, absolute_import

# djnago
from django.contrib.auth.models import AbstractUser
from django.core.urlresolvers import reverse
from django.utils.encoding import python_2_unicode_compatible
from django.db import models
from django.utils.translation import ugettext_lazy as _

# leukapp
from leukapp.apps.core.validators import phone_validator
from leukapp.apps.participants.factories import ParticipantFactory


@python_2_unicode_compatible
class User(AbstractUser):

    # First Name and Last Name do not cover name patterns
    # around the globe.

    phone = models.CharField(
        _("phone"),
        max_length=15,
        validators=[phone_validator],
        blank=True
        )

    def __str__(self):
        return self.username

    def save(self, *args, **kwargs):
        self.first_name = self.first_name.capitalize()
        self.last_name = self.last_name.capitalize()
        ParticipantFactory(
            first_name=self.first_name,
            last_name=self.last_name,
            email=self.email,
            phone=self.phone,
            )
        super(User, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('users:detail', kwargs={'username': self.username})
