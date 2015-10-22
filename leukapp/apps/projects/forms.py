from django import forms
from .models import Project

from crispy_forms.helper import FormHelper
# from crispy_forms.layout import Layout, Field
# from crispy_forms.bootstrap import TabHolder, Tab
from . import constants


class ProjectCreateForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(ProjectCreateForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)

    def is_valid(self, *args, **kwargs):
        try:
            participants = self.data['participants'].split(',')
            self.data['participants'] = [int(p) for p in participants]
        except Exception:
            self.data['participants'] = []
        return super(ProjectCreateForm, self).is_valid(*args, **kwargs)

    class Meta:
        model = Project
        fields = constants.PROJECT_CREATE_FIELDS


class ProjectUpdateForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(ProjectUpdateForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        # self.fields['participants'].required = True

    def is_valid(self, *args, **kwargs):
        try:
            participants = self.data['participants'].split(',')
            self.data['participants'] = [int(p) for p in participants]
        except Exception:
            self.data['participants'] = []
        return super(ProjectUpdateForm, self).is_valid(*args, **kwargs)

    class Meta:
        model = Project
        fields = constants.PROJECT_UPDATE_FIELDS
