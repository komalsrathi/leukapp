from django import forms
from .models import Specimen

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field
from crispy_forms.bootstrap import TabHolder, Tab


class SpecimenForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(SpecimenForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)

    class Meta:
        model = Specimen
        fields = ['individual', 'source', 'ext_id']
