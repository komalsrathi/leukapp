# -*- coding: utf-8 -*-

"""
Custom forms not used so far
"""

"""
# django
from django import forms

# third party
from crispy_forms.helper import FormHelper
# from crispy_forms.layout import Layout, Field
# from crispy_forms.bootstrap import TabHolder, Tab

# local
from .constants import CREATE_FIELDS
from .models import Specimen


class SpecimenForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(SpecimenForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)

    class Meta:
        model = Specimen
        fields = CREATE_FIELDS
"""
