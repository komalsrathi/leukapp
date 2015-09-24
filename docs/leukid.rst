.. This is a comment.
.. |date| date::

======
leukid
======

.. bibliographic fields (which also require a transform):
:author: Juan Medina,
:contact: medinaj@mskcc.org
:organization: Memorial Sloan-Kettering
:status: This is "work in progress"
:date: |date|
:Revision: 1

:abstract:
    This wiki describes the  **sample_form** and the **leukid** with it's generation script (*idscript.py*). The **leukid** is constructed based on data stored in **leukdb** and the information provided by the **sample_form**.

    Typographical conventions:

    * ``constant width`` for code fragments, commands or object attributes
    * *italic* for file names
    * **bold** important terms

.. meta::
   :keywords: leukid, sample_form
   :description lang=en: This wiki describes the **leukid**, it's generation script (*idscript.py*) and the  **sample_form**.

.. contents:: Table of Contents
.. section-numbering::


Introduction
------------

The **sample_form** is a submission template that include the minimum fields required to construct the **leukid**.

The **leukid** is designed to identify each single *data unit* living within the Leukemia Center infrastructure. The **leukid** provides a useful description of the nature of the data.

The **leukid** is composed by the following 2 sections:

1. *Sample*, describes:

   a) Individual
   b) Specimen
   c) Aliquot

2. *Sequencing Run* (maybe *Library* to match Sanger's naming), describes:

   a) Legacy
   b) Run ID
   c) Sequencing technology

sample_form
-----------

The minimum fields required to construct the **leukid** are submitted using the **sample_form**. Such fields are:

+------------------------+-------------+-----------+
| field name             | values      | data type |
+========================+=============+===========+
| ``individual_source``  | | Internal  | String    |
|                        | | External  |           |
+------------------------+-------------+-----------+
| ``individual_species`` | | Human     | String    |
|                        | | Mouse     |           |
|                        | | Yeast     |           |
|                        | | Zebrafish |           |
+------------------------+-------------+-----------+
| ``individual_ext_id``  | N/A         | String    |
+------------------------+-------------+-----------+
| ``specimen_type``      | | Tumor     | String    |
|                        | | Normal    |           |
+------------------------+-------------+-----------+
| ``specimen_ext_id``    | N/A         | String    |
+------------------------+-------------+-----------+
| ``aliquot_material``   | | DNA       | String    |
|                        | | RNA       |           |
|                        | | MIXED     |           |
+------------------------+-------------+-----------+
| ``aliquot_ext_id``     | N/A         | String    |
+------------------------+-------------+-----------+

leukid
------

This section describes the **leukid** and how to construct it based on the **sample_form**.

Sample
^^^^^^

A sample is an abstracted object that carries information about an Aliquot and it's respective Specimen and Individual.

Individual: ``I-H-100000``
""""""""""""""""""""""""""

An individual is the subject where the data was obtained from. The *idscript.py* assigns the following attributes:

1. ``individual_source``: indicates whether the sample comes from an MSK individual or not. This value is mapped from the **sample_form** according to the following table:

+-----------------------+------------+
| ``individual_source`` | form value |
+=======================+============+
| I                     | Internal   |
+-----------------------+------------+
| E                     | External   |
+-----------------------+------------+

2. ``individual_species``: indicates the species of the individual. This value is mapped from the **sample_form** according to the following table:

+------------------------+------------+
| ``individual_species`` | form value |
+========================+============+
| H                      | Human      |
+------------------------+------------+
| M                      | Mouse      |
+------------------------+------------+
| Y                      | Yeast      |
+------------------------+------------+
| Z                      | Zebrafish  |
+------------------------+------------+

3. ``individual_int_id``: For a given ``individual_ext_id`` (e.g. MRN), there is a unique ``individual_int_id``. This field is created by adding 1 to the previous unique record, starting from 100000. The ``individual_ext_id`` is recorded from **sample_form**.

Specimen: ``I-H-100000-T-2``
""""""""""""""""""""""""""""

This section describes to the Specimen extracted from the Individual. The *idscript.py* assigns the following attributes:

1. ``specimen_type``: this value is mapped from the **sample_form** according to the following table:

+-------------------+------------+
| ``specimen_type`` | form value |
+===================+============+
| T                 | Tumor      |
+-------------------+------------+
| N                 | Normal     |
+-------------------+------------+

2. ``specimen_int_id``: For a given ``specimen_ext_id``, there is a unique ``specimen_int_id``. This field is created by adding 1 to the previous unique record, starting from 1. The ``specimen_ext_id`` is recorded from **sample_form**.

Aliquot: ``I-H-100000-T-2-D-1-1``
"""""""""""""""""""""""""""""""""

This section describes to the physical aliquot extracted from the individual's specimen. The *idscript.py* assigns the following attributes:

1. ``aliquot_material``: this value corresponds to the biological material extracted from the specimen and is mapped from the **sample_form** according to the following table:

+----------------------+------------+
| ``aliquot_material`` | form value |
+======================+============+
| D                    | DNA        |
+----------------------+------------+
| R                    | RNA        |
+----------------------+------------+
| M                    | MIXED      |
+----------------------+------------+

2. ``aliquot_int_id``: For a given ``aliquot_ext_id``, there is a unique ``aliquot_int_id``. This field is created by adding 1 to the previous unique record, starting from 1. The ``aliquot_ext_id`` is recorded from **sample_form**. If the ``aliquot_ext_id`` is ``Null``, a new ``aliquot_int_id`` will be created.

3. ``aliquot_iteration_id``: the aliquot iteration corresponds to the subset of material extracted from the *Aliquot* tube that will be sent to the sequencing center.


Library
^^^^^^^
