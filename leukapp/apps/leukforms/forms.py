# -*- coding: utf-8 -*-

# django
from django import forms

# leukapp
from leukapp.apps.individuals.constants import INDIVIDUAL_CREATE_FIELDS
from leukapp.apps.specimens.constants import SPECIMEN_CREATE_FIELDS
from leukapp.apps.aliquots.constants import ALIQUOT_CREATE_FIELDS
from leukapp.apps.runs.constants import RUN_CREATE_FIELDS
from leukapp.apps.individuals.models import Individual
from leukapp.apps.specimens.models import Specimen
from leukapp.apps.aliquots.models import Aliquot
from leukapp.apps.runs.models import Run


class IndividualForm(forms.ModelForm):

    class Meta:
        model = Individual
        fields = INDIVIDUAL_CREATE_FIELDS


class SpecimenForm(forms.ModelForm):

    class Meta:
        model = Specimen
        fields = SPECIMEN_CREATE_FIELDS


class AliquotForm(forms.ModelForm):

    class Meta:
        model = Aliquot
        fields = ALIQUOT_CREATE_FIELDS


class RunForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
            super(RunForm, self).__init__(*args, **kwargs)
            self.fields['projects_list'].required = True

    class Meta:
        model = Run
        fields = RUN_CREATE_FIELDS + ('projects_list', )
