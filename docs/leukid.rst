.. This is a comment.
.. |date| date::

======
leukid
======

.. bibliographic fields (which also require a transform):
:author: Juan Medina
:contact: medinaj@mskcc.org
:organization: Memorial Sloan-Kettering
:status: This is "work in progress"
:date: |date|
:Revision: 1

:abstract:
    This wiki describes the **leukid** and it's models. The **leukid** is constructed based on the information provided by the **sample_form**.

    Typographical conventions:

    * ``constant width`` for code fragments, commands or object attributes
    * *italic* for file names
    * **bold** important terms

.. meta::
   :keywords: leukid, sample_form, models, sample, data unit
   :description lang=en: This wiki describes the **leukid** and it's models. The **leukid** is constructed based on the information provided by the **sample_form**.

.. contents:: Table of Contents
.. .. section-numbering::


Introduction
------------

The **sample_form** is a submission template that includes the minimum fields required to construct the **leukid**. The **leukid** is constructed using the following Django ``Models`` (or database Schemas, or how Elli calls them: Databases):

a) ``Individual``
b) ``Specimen``
c) ``Aliquot``
d) ``Library``

The **leukid** is designed to identify each single **data unit** living within the Leukemia Center infrastructure. A **data unit** is an abstract concept that refers to a sequenced ``Library`` and its respective **sample**. A **sample** is an abstract concept that carries information about an ``Aliquot`` and it's respective ``Specimen`` and ``Individual``.

The **leukid** provides a useful description of the nature of the data. The **leukid** models are thoroughly explained in the `leukid construction`_ section.

sample_form
-----------

The minimum fields required to construct the **leukid** are submitted using the **sample_form**. Such fields are:

+------------------------+-----------+-----------+
| model field name       | form name | data type |
+========================+===========+===========+
| ``Individual.source``  | Internal  | String    |
+------------------------+-----------+-----------+
| ``Individual.species`` | Human     | String    |
+------------------------+-----------+-----------+
| ``Individual.ext_id``  | N/A       | String    |
+------------------------+-----------+-----------+
| ``Specimen.type``      | Tumor     | String    |
+------------------------+-----------+-----------+
| ``Specimen.ext_id``    | N/A       | String    |
+------------------------+-----------+-----------+
| ``Aliquot.material``   | DNA       | String    |
+------------------------+-----------+-----------+
| ``Aliquot.ext_id``     | N/A       | String    |
+------------------------+-----------+-----------+

leukid construction
-------------------

This section describes the construction of the **leukid** models based on the **sample_form** submission.

``Individual`` (leukid: I-H-100000 ...)
"""""""""""""""""""""""""""""""""""""""

The ``Individual`` is the subject where the ``Specimen`` was obtained from. The ``Individual`` model has the following fields and methods:

1. ``Individual.pk``: unique identifier at the database level. Its an integer starting from 1.

2. ``Individual.source``: indicates the source of the **sample**. This value is mapped from the **sample_form** according to the following table:

+-------------------------------+----------------------------------------+
| ``Individual.source`` choices | form value                             |
+===============================+========================================+
| MSK                           | Memorial Sloan-Kettering Cancer Center |
+-------------------------------+----------------------------------------+
| O                             | Other                                  |
+-------------------------------+----------------------------------------+

3. ``Individual.species``: indicates the ``Individual``'s species. This value is mapped from the **sample_form** according to the following table:

+--------------------------------+------------+
| ``Individual.species`` choices | form value |
+================================+============+
| H                              | Human      |
+--------------------------------+------------+
| M                              | Mouse      |
+--------------------------------+------------+
| Y                              | Yeast      |
+--------------------------------+------------+
| Z                              | Zebrafish  |
+--------------------------------+------------+

4. ``Individual.ext_id``: corresponds to the subject external ID, (e.g. for a human, the HOTB would provide **Subject ID**). The ``Individual.ext_id`` is recorded from **sample_form**.

5. ``Individual.int_id()``: This field is created by adding 100000 to the ``Individual.pk``.

6. ``Individual.check_source()``: This field is created by adding 100000 to the ``Individual.pk``.

``Specimen`` (leukid: I-H-100000-T-2 ...)
"""""""""""""""""""""""""""""""""""""""""

This section describes to the ``Specimen`` extracted from the ``Individual``. The ``Specimen`` model has the following fields and methods:

1. ``Specimen.Individual``: this field is a ``ForeingKey`` to an ``Individual`` instance.

1. ``Specimen.source``: this value is mapped from the **sample_form** according to the following table:

+-------------------+------------+
| ``Specimen.source`` | form value |
+===================+============+
| T                 | Tumor      |
+-------------------+------------+
| N                 | Normal     |
+-------------------+------------+

2. ``Specimen.int_id``: For a given ``Specimen.ext_id``, there is a unique ``Specimen.int_id``. This field is created by adding 1 to the previous unique record, starting from 1. The ``Specimen.ext_id`` is recorded from **sample_form**.

Aliquot: ``I-H-100000-T-2-D-1-1``
"""""""""""""""""""""""""""""""""

This section describes to the physical aliquot extracted from the ``Individual``'s specimen. The *idscript.py* assigns the following attributes:

1. ``Aliquot.material``: this value corresponds to the biological material extracted from the specimen and is mapped from the **sample_form** according to the following table:

+----------------------+------------+
| ``Aliquot.material`` | form value |
+======================+============+
| D                    | DNA        |
+----------------------+------------+
| R                    | RNA        |
+----------------------+------------+
| M                    | MIXED      |
+----------------------+------------+

2. ``Aliquot.int_id``: For a given ``Aliquot.ext_id``, there is a unique ``Aliquot.int_id``. This field is created by adding 1 to the previous unique record, starting from 1. The ``Aliquot.ext_id`` is recorded from **sample_form**. If the ``Aliquot.ext_id`` is ``Null``, a new ``Aliquot.int_id`` will be created.

3. ``Aliquot.iteration_id``: the aliquot iteration corresponds to the subset of material extracted from the *Aliquot* tube that will be sent to the sequencing center.


Library
^^^^^^^
