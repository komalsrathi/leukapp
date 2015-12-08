.. |date| date::

**tldr**: This wiki describes the **leukid**.

******
Leukid
******

.. bibliographic fields (which also require a transform):
:author: Juan Medina
:contact: medinaj@mskcc.org
:organization: Memorial Sloan-Kettering
:status: This is "work in progress"
:date: |date|
:version: |version|
:abstract: This wiki describes the **leukid**.

.. meta::
   :keywords: leukid, leukform, models, sample, data unit
   :description lang=en: This wiki describes the **leukid**.

Example
=======

As of |date|, is is an example of the ID and its sections::

    # leukid example:
    E-M-944-T1-1-R1-1-9A-P100-IONTPGM-FNDTN

    # divided by sections
    Individual - Specimen - Aliquot - Extraction - Workflow
    E-M-944    - T1       - 1       - R1         - 1-9A-P100-IONTPGM-FNDTN

Description
===========

**Individual:**

* ``E``    - I if MSK's individual, E if not.
* ``M``    - Species, M for mouse, H for Human, etc.
* ``944``  - Internal ID for that individual

**Specimen:** tissue collected from Individual

* ``T1``   - T for tumor, N for normal. The number is an internal ID.

**Aliquot:** subset material of the Specimen

* ``1``    - Internal ID for aliquot tube.

**Extraction:** extracted DNA or RNA from the Aliquot

* ``R1``   - R if RNA, D if DNA. The number is an internal ID.

**Workflow:** sequencing data produced from the Extraction

* ``1``        - Internal ID.
* ``9A``       - Code for the :doc:`technology_codes`.
* ``P100``     - P for Pairend, E for Endpair, 100 is read length
* ``IONTPGM``  - Platform used.
* ``FNDTN``    - Sequencing center.
