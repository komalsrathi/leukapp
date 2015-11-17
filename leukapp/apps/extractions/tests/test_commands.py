# -*- coding: utf-8 -*-
"""
# python
import csv
import os

# django imports
from django.test import TestCase

# apps imports
from leukapp.apps.individuals.models import Individual
from leukapp.apps.specimens.models import Specimen
from leukapp.apps.aliquots.models import Aliquot
from leukapp.apps.projects.models import Project

from leukapp.apps.individuals.utils import IndividualFactory
from leukapp.apps.specimens.utils import SpecimenFactory
from leukapp.apps.aliquots.utils import AliquotFactory

# local imports
from ..management.commands import submit_extractions_from_csv
from ..utils import LeukformSamplesFactory
"""
