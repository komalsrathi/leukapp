from django import forms

from crispy_forms.helper import FormHelper
# from crispy_forms.layout import Layout, Field
# from crispy_forms.bootstrap import TabHolder, Tab

from .models import Participant
from .constants import PARTICIPANT_CREATE_FIELDS


class ParticipantForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(ParticipantForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)

    class Meta:
        model = Participant
        fields = PARTICIPANT_CREATE_FIELDS
