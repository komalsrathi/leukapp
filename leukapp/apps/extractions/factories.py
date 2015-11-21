# -*- coding: utf-8 -*-

# python
import string

# third party
import factory
from factory.fuzzy import FuzzyChoice, FuzzyText

# leukapp
from leukapp.apps.aliquots.factories import AliquotFactory

# local
from .models import Extraction
from . import constants


class ExtractionFactory(factory.django.DjangoModelFactory):

    """
    Creates :class:`~leukapp.apps.extractions.models.Extraction` object, mainly
    for testing purposes.

    If no keyword argument is provided, ``ExtractionFactory`` will generate the
    appropriate attributes.
    See :func:`~leukapp.apps.extractions.models.Extraction` for parameter
    details.

    .. warning:: blabla

    .. parameter description
    :param aliquot:
        :func:`~leukapp.apps.aliquots.models.Aliquot` object. If not provided,
        factory.SubFactory(AliquotFactory) will be used.
    :param analyte: :py:const:`~leukapp.apps.extractions.constants.ANALYTE`
    :param platform: juan
    :param technology: juan
    :param center: juan
    :param ext_id: juan
    :param projects_list: juan
    :param projects: juan

    .. parameter types
    :type aliquot: :func:`~leukapp.apps.aliquots.models.Aliquot`
    :type analyte: str
    :type platform: str
    :type technology: str
    :type center: str
    :type ext_id: str
    :type projects_list: str
    :type projects: list

    .. returns
    :return: :func:`~leukapp.apps.extractions.models.Extraction` object.

    Creates Many to Many relationships to `Project` instances passed
    through the `projects` keyword argument. for example::

            projects = [ProjectFactory() for i in range(3)]
            extraction = ExtractionFactory(analyte=DNA, projects=projects)

    Example::
        extraction = ExtractionFactory(aliquot=AliquotFactory(), analyte='DNA')

    .. seealso::
        :func:`~leukapp.apps.extractions.models.Extraction`
        :func:`~leukapp.apps.aliquots.models.Aliquot`
        :func:`~leukapp.apps.aliquots.factories.AliquotFactory`

    .. warnings also:: blabla
    .. note:: blabla
    .. todo:: blabla

    .. note::
        There are many other Info fields but they may be redundant:
            * param, parameter, arg, argument, key, keyword: Description of a
              parameter.
            * type: Type of a parameter.
            * raises, raise, except, exception: That (and when) a specific
              exception is raised.
            * var, ivar, cvar: Description of a variable.
            * returns, return: Description of the return value.
            * rtype: Return type.

    .. note::
        There are many other directives such as versionadded, versionchanged,
        rubric, centered, ... See the sphinx documentation for more details.


    Creates Many to Many relationships to `Project` instances passed
    through the `projects` keyword argument. for example::

            projects = [ProjectFactory() for i in range(3)]
            extraction = ExtractionFactory(analyte=DNA, projects=projects)
    """

    class Meta:
        model = Extraction

    aliquot = factory.SubFactory(AliquotFactory)
    analyte = FuzzyChoice(constants.ANALYTE_VALUE)
    platform = FuzzyChoice(constants.PLATFORM_VALUE)
    technology = FuzzyChoice(constants.TECHNOLOGY_VALUE)
    center = FuzzyChoice(constants.CENTER_VALUE)
    ext_id = FuzzyText(length=12, chars=string.hexdigits)
    projects_list = ''

    @factory.post_generation
    def projects(self, create, extracted, **kwargs):
        if not create:  # Simple build, do nothing.
            return
        if extracted:   # A list of project were passed in, use them
            [self.projects.add(p) for p in extracted]


# ROUTINE PROTECTION
# -----------------------------------------------------------------------------

if __name__ == '__main__':
    pass
