.. |date| date::

***************************
Sequencing Technology Codes
***************************

.. bibliographic fields (which also require a transform):
:author: Juan Medina
:contact: medinaj@mskcc.org
:organization: Memorial Sloan-Kettering
:status: This is "work in progress"
:date: |date|
:version: |version|

:abstract:
    This dictionary is used to map the different **sequencing technologies** and **technology types** to the codes used in the **Leukgen** environment.

.. meta::
   :keywords: leukid, form, models, sample, code, sequencing technology
   :description lang=en: ``analyte/technology/technolgy_type`` codes.

.. _technology_codes:

.. exec::
    import json
    from leukapp.apps.workflows.constants import INT_ID_TECHNOLOGY
    json_obj = json.dumps(INT_ID_TECHNOLOGY, sort_keys=True, indent=8)
    json_obj = json_obj[:-1] + "    }"
    print('.. code-block:: JavaScript\n\n    %s' % json_obj)
