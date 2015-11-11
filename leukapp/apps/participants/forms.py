# -*- coding: utf-8 -*-

# django
from django import forms

# third party
from crispy_forms.helper import FormHelper

# local
from .models import Participant
from . import constants


class ParticipantForm(forms.ModelForm):

    """
    This form is mainly used in vies.ModalCreateForm, please dont get rid of it
    """

    def __init__(self, *args, **kwargs):
        super(ParticipantForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)

    class Meta:
        model = Participant
        fields = constants.PARTICIPANT_CREATE_FIELDS
