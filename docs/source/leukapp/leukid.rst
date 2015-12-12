.. |date| date::

**tldr**: This wiki describes the **leukid** and the projects file structure.

****************************************************
Projects File Structure, Leukid and Database Schemas
****************************************************

.. bibliographic fields (which also require a transform):

:author: Juan Medina
:contact: medinaj@mskcc.org
:organization: Memorial Sloan-Kettering
:status: This is "work in progress"
:date: |date|
:version: |version|
:abstract: This wiki describes the **leukid** and projects file structure.

.. meta::
   :keywords: leukid, leukform, models, sample, data unit
   :description lang=en: This wiki describes the **leukid**.

Projects File Structure
=======================

As of |date|, the file structure that will be presented to the **leukgen**
users is::

    PROJECTS_ROOT_DIR                           # projects root directory
    └── 100                                     # project 100 directory
        └── 1A-CMO-P100-HISQ25k                 # subproject directory
            └── I-H-100000-T1-1-R1-1            # sample directory
                └── I-H-100000-T1-1-R1-1.bam    # symbolic link to data

.. important::
    Please note that the **sample id** presented to the users corresponds to
    the system's **leukid** up to position ``[7]``. **Leukid's** positions
    ``[8-11]`` are used to define the subproject. Please see `leukid`_ for more
    information.


.. _leukid:

Leukid and Database Schemas
===========================

The **leukid** is used to track and represent different classes of objects that
are relevant to leukemia research. This classes are mapped to python **models**
which are further represented by database schemas. The **leukid** is composed
by ``11`` positions divided in 5 secions: Individual, Specimen, Aliquot, Extraction and Workflow.The following is a **leukid** example:

  ``E-M-944-T1-1-R1-1-9A-P100-IONTPGM-FNDTN``

.. code::

  Individual   Specimen  Aliquot  Extraction   Workflow
  [1] [2] [3]  [4]       [5]      [6]          [7]  [8]  [9]   [10]      [11]
  E - M - 100  T1        1        R1           1  - 9A - P100 - IONTPGM - FNDTN

.. note::
    position ``8`` of the leuk id is based on the
    :doc:`/leukapp/technology_codes` dictionary.

The next sections will describe each particular **model**, it's respective
**leukid** section and the database fields recorded.

Individual
^^^^^^^^^^
.. currentmodule:: leukapp.apps.individuals.models

This model is operated by the python class :class:`Individual` and it's data
is stored in the database schema ``individuals_individual``.
Each ``Individual`` instance is represented by leukid's positions ``[1-3]``.
This leukid section is saved in the :attr:`Individual.int_id` field:

.. autoinstanceattribute:: Individual.int_id
    :noindex:
    :annotation: = I-H-100000


Individual External Fields
""""""""""""""""""""""""""

.. autoinstanceattribute:: Individual.institution
    :noindex:
    :annotation: = MSK
.. autoinstanceattribute:: Individual.ext_id
    :noindex:
    :annotation: = 123456789
.. autoinstanceattribute:: Individual.species
    :noindex:
    :annotation: = HUMAN

Individual Internal Fields
""""""""""""""""""""""""""

.. autoinstanceattribute:: Individual.tumors_count
    :noindex:
    :annotation: = 3
.. autoinstanceattribute:: Individual.normals_count
    :noindex:
    :annotation: = 4
.. autoinstanceattribute:: Individual.slug
    :noindex:
    :annotation: = I-H-100000


Specimen
^^^^^^^^

.. currentmodule:: leukapp.apps.specimens.models

:class:`Individual's <leukapp.apps.aliquots.models.Aliquot>` tissue
collected on a particular day. This model is operated by the python class
:class:`Specimen` and it's data is stored in the database schema
``specimens_specimen``. Each ``Specimen`` instance is represented by leukid's
position ``[4]``. This leukid section is saved in the :attr:`Specimen.int_id` field:

.. autoinstanceattribute:: Specimen.int_id
    :noindex:
    :annotation: = T4

Specimen External Fields
""""""""""""""""""""""""

.. autoinstanceattribute:: Specimen.individual
    :noindex:
    :annotation: = 1
.. autoinstanceattribute:: Specimen.ext_id
    :noindex:
    :annotation: = 123456789
.. autoinstanceattribute:: Specimen.source
    :noindex:
    :annotation: = BLOOD
.. autoinstanceattribute:: Specimen.source_type
    :noindex:
    :annotation: = TUMOR
.. autoinstanceattribute:: Specimen.order
    :noindex:
    :annotation: = 1

Specimen Internal Fields
""""""""""""""""""""""""

.. autoinstanceattribute:: Specimen.aliquots_count
    :noindex:
    :annotation: = 3
.. autoinstanceattribute:: Specimen.slug
    :noindex:
    :annotation: = I-H-100000-T1


Aliquot
^^^^^^^

.. currentmodule:: leukapp.apps.aliquots.models

:class:`Specimen's <leukapp.apps.aliquots.models.Specimen>` sub-collections
stored in separated tubes. This model is operated by the python class
:class:`Aliquot` and it's data is stored in the database schema
``specimens_specimen``. Each ``Aliquot`` instance is represented by leukid's
position ``[5]``. This leukid section is saved in the :attr:`Aliquot.int_id` field:

.. autoinstanceattribute:: Aliquot.int_id
    :noindex:
    :annotation: = 1

Aliquot External Fields
"""""""""""""""""""""""
.. autoinstanceattribute:: Aliquot.specimen
    :noindex:
    :annotation: = 1
.. autoinstanceattribute:: Aliquot.ext_id
    :noindex:
    :annotation: = 123456789

Aliquot Internal Fields
"""""""""""""""""""""""
.. autoinstanceattribute:: Aliquot.dna_extractions_count
    :noindex:
    :annotation: = 2
.. autoinstanceattribute:: Aliquot.rna_extractions_count
    :noindex:
    :annotation: = 3
.. autoinstanceattribute:: Aliquot.slug
    :noindex:
    :annotation: = I-H-100000-T1-1


Extraction
^^^^^^^^^^

.. currentmodule:: leukapp.apps.extractions.models

:class:`Aliquot's <leukapp.apps.aliquots.models.Aliquot>` nucleic acid. This model is operated by the python class :class:`Extraction` and it's data is
stored in the database schema ``extractions_extraction``. Each ``Extraction``
instance is represented by leukid's position ``[6]``. This leukid section is saved in the :attr:`Extraction.int_id` field:

.. autoinstanceattribute:: Extraction.int_id
    :noindex:
    :annotation: = 1

Extraction External Fields
""""""""""""""""""""""""""
.. autoinstanceattribute:: Extraction.aliquot
    :noindex:
    :annotation: = 1
.. autoinstanceattribute:: Extraction.ext_id
    :noindex:
    :annotation: = 123456789
.. autoinstanceattribute:: Extraction.analyte
    :noindex:
    :annotation: = DNA

Extraction Internal Fields
""""""""""""""""""""""""""
.. autoinstanceattribute:: Extraction.workflows_count
    :noindex:
    :annotation: 3
.. autoinstanceattribute:: Extraction.slug
    :noindex:
    :annotation: I-H-100000-T1-1-D1


Workflow
^^^^^^^^

.. currentmodule:: leukapp.apps.workflows.models

:class:`Extraction's <leukapp.apps.extractions.models.Extraction>` sequence
workflow. This model is operated by the python class :class:`Workflow` and
it's data is stored in the database schema ``workflows_workflow``. Each
``Workflow`` instance is represented by leukid's positions ``[7-11]``.
This leukid section is saved in the :attr:`Workflow.int_id` field:

.. note::
    position ``8`` of the leuk id is based on the
    :doc:`/leukapp/technology_codes` dictionary.

.. autoinstanceattribute:: Workflow.int_id
    :noindex:
    :annotation: = 1

Workflow External Fields
""""""""""""""""""""""""""

.. autoinstanceattribute:: Workflow.extraction
    :noindex:
    :annotation: = 1
.. autoinstanceattribute:: Workflow.ext_id
    :noindex:
    :annotation: = 123456789
.. autoinstanceattribute:: Workflow.projects
    :noindex:
    :annotation: = [100, 101, 202]
.. autoinstanceattribute:: Workflow.projects_string
    :noindex:
    :annotation: = "101|102|103"
.. autoinstanceattribute:: Workflow.sequencing_center
    :noindex:
    :annotation: = CMO
.. autoinstanceattribute:: Workflow.sequencing_technology
    :noindex:
    :annotation: = "WHOLE-GENOME"
.. autoinstanceattribute:: Workflow.technology_type
    :noindex:
    :annotation: = "AGILENT-50MB"
.. autoinstanceattribute:: Workflow.sequencing_platform
    :noindex:
    :annotation: = "ILLUMINA-HISEQ-2000"
.. autoinstanceattribute:: Workflow.read_length
    :noindex:
    :annotation: = "100"
.. autoinstanceattribute:: Workflow.read_type
    :noindex:
    :annotation: = "SINGLE-END"

Workflow Internal Fields
""""""""""""""""""""""""""

.. autoinstanceattribute:: Workflow.slug
    :noindex:
    :annotation: I-H-100000-T1-1-D1-1-1A-S100-x10-CMO

