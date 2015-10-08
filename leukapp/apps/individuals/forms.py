# -*- coding: utf-8 -*-

# django
from django import forms
from .models import Individual

# third party
from crispy_forms.helper import FormHelper

# local
from .constants import CREATE_FIELDS


class IndividualForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(IndividualForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)

    class Meta:
        model = Individual
        fields = CREATE_FIELDS
