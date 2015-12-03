# -*- coding: utf-8 -*-

# django
from django import forms

# leukapp create fields
from leukapp.apps.individuals.constants import INDIVIDUAL_CREATE_FIELDS
from leukapp.apps.specimens.constants import SPECIMEN_CREATE_FIELDS
from leukapp.apps.aliquots.constants import ALIQUOT_CREATE_FIELDS
from leukapp.apps.extractions.constants import EXTRACTION_CREATE_FIELDS
from leukapp.apps.workflows.constants import WORKFLOW_CREATE_FIELDS

# leukapp models
from leukapp.apps.individuals.models import Individual
from leukapp.apps.specimens.models import Specimen
from leukapp.apps.aliquots.models import Aliquot
from leukapp.apps.extractions.models import Extraction
from leukapp.apps.workflows.models import Workflow


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


class ExtractionForm(forms.ModelForm):

    class Meta:
        model = Extraction
        fields = EXTRACTION_CREATE_FIELDS


class WorkflowForm(forms.ModelForm):

    class Meta:
        model = Workflow
        fields = WORKFLOW_CREATE_FIELDS
