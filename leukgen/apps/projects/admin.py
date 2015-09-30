from django.contrib import admin

from .models import Project


# class ProjectAdmin(admin.ModelAdmin):

#     """docstring for ProjectAdmin"""

#     fieldsets = [
#         (None, {'fields': ['name', 'description']}),
#         ('Users', {
#             'fields': ['principal_investigator', 'scientist', 'data_analyst'],
#             'classes': ['collapse']})
#     ]

#     list_display = ('name', 'principal_investigator')

# admin.site.register(Project, ProjectAdmin)
