from django import forms
from .models import Aliquot

from crispy_forms.helper import FormHelper
# from crispy_forms.layout import Layout, Field
# from crispy_forms.bootstrap import TabHolder, Tab

# local
from .constants import CREATE_FIELDS


class AliquotForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(AliquotForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)

    class Meta:
        model = Aliquot
        fields = CREATE_FIELDS
