leukid
==========

This wiki describes the **leukid** and it's generation script (*idscript.py*). The **leukid** is constructed based on data stored in **leukdb** and the information provided by the **sample_form**.

We use the following typographical conventions:

    * ``constant width`` for code fragments, commands or object attributes
    * *italic* for file names
    * **bold** important terms

Introduction
------------

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


Sample
------

Individual: ``I-H-100000``
^^^^^^^^^^^^^^^^^^^^^^^^^^

Corresponds to the real or virtual subject where the data was obtained from. The *idscript.py* assigns the following attributes:

1. ``individual_source``: indicates whether the sample comes from an MSK individual or not. This value is mapped from the **sample_form**'s field ``sf_individual_source`` according to the following table:

+-----------------------+--------------------------+
| ``individual_source`` | ``sf_individual_source`` |
+=======================+==========================+
| I                     | Internal                 |
+-----------------------+--------------------------+
| E                     | External                 |
+-----------------------+--------------------------+

2. ``individual_species``: indicates the species of the individual. This value is mapped from the **sample_form**'s field ``sf_individual_species`` according to the following table:

+------------------------+---------------------------+
| ``individual_species`` | ``sf_individual_species`` |
+========================+===========================+
| H                      | Human                     |
+------------------------+---------------------------+
| M                      | Mouse                     |
+------------------------+---------------------------+
| Y                      | Yeast                     |
+------------------------+---------------------------+
| Z                      | Zebra Fish                |
+------------------------+---------------------------+

3. ``individual_int_id``: There is a unique ``individual_int_id`` for any unique ``individual_ext_id`` (e.g. MRN). This field is created by adding 1 to the previous record, starting from 100000. The ``individual_ext_id`` is recorded from **sample_form**'s field ``sf_individual_ext_id``.

Specimen: ``I-H-100000-T-2``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This section describes to the physical specimen extracted from the individual. The *idscript.py* assigns the following attributes:

1. ``specimen_type``: this value is mapped from the **sample_form**'s field ``sf_specimen_type`` according to the following table:

+-------------------+----------------------+
| ``specimen_type`` | ``sf_specimen_type`` |
+===================+======================+
| T                 | Tumor                |
+-------------------+----------------------+
| N                 | Normal               |
+-------------------+----------------------+

2. ``specimen_int_id``: There is a unique ``specimen_int_id`` for any unique ``specimen_ext_id``. This field is created by adding 1 to the previous record, starting from 1. The ``specimen_ext_id`` is recorded from **sample_form**'s field ``sf_specimen_ext_id``.

Aliquot: ``I-H-100000-T-2-D-1-1``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This section describes to the physical aliquot extracted from the individual's specimen. The *idscript.py* assigns the following attributes:

1. ``aliquot_material``: this value corresponds to the biological material extracted from the specimen and is mapped from the **sample_form**'s field ``sf_aliquot_material`` according to the following table:

+----------------------+-------------------------+
| ``aliquot_material`` | ``sf_aliquot_material`` |
+======================+=========================+
| D                    | DNA                     |
+----------------------+-------------------------+
| R                    | RNA                     |
+----------------------+-------------------------+
| M                    | Mixed                   |
+----------------------+-------------------------+

2. ``aliquot_int_id``: There is a unique ``aliquot_int_id`` for any unique ``aliquot_ext_id``. This field is created by adding 1 to the previous record, starting from 1. The ``aliquot_ext_id`` is recorded from **sample_form**'s field ``sf_aliquot_ext_id``. If the ``sf_aliquot_ext_id`` is ``Null``, a new ``aliquot_int_id`` will be created.

3. ``aliquot_iteration_id``: the aliquot iteration corresponds to the subset of material extracted from the *Aliquot* tube that will be sent to the sequencing center.


Library
-------
