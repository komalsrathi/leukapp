from django.test import TestCase

from ..models import Project


class ProjectModelTest(TestCase):

    """docstring for ProjectModelTest"""

    def test_saving_and_retrieving_projects(self):
        first_project = Project()
        first_project.description = "The first (ever) project"
        first_project.save()

        second_project = Project()
        second_project.description = "Project the second"
        second_project.save()

        saved_projects = Project.objects.all()
        self.assertEqual(saved_projects.count(), 2)

        first_saved_project = saved_projects[0]
        second_saved_project = saved_projects[1]
        self.assertEqual(first_saved_project.description,
                         "The first (ever) project")
        self.assertEqual(second_saved_project.description,
                         "Project the second")
