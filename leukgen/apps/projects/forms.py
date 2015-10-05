from django import forms
from .models import Project

from crispy_forms.helper import FormHelper
# from crispy_forms.layout import Layout, Field
# from crispy_forms.bootstrap import TabHolder, Tab


class ProjectForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(ProjectForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)

    class Meta:
        model = Project
        fields = [
            'name',
            'description',
            'pi',
            'analyst',
            'requestor',
            'participants',
            'cost_center_no',
            'fund_no',
            'protocol_no',
            ]
