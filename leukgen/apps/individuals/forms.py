from django import forms
from .models import Individual

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field
from crispy_forms.bootstrap import TabHolder, Tab


class IndividualForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(IndividualForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)

    class Meta:
        model = Individual
        fields = ['institution', 'ext_id', 'species']
