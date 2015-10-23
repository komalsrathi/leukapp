# -*- coding: utf-8 -*-

# django
from django.contrib import admin

# leukapp
from leukapp.apps.specimens.models import Specimen

# local
from .models import Individual


class SpecimenInline(admin.StackedInline):
    model = Specimen
    extra = 2


class IndividualAdmin(admin.ModelAdmin):
    inlines = [SpecimenInline]

admin.site.register(Individual, IndividualAdmin)
