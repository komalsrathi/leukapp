# -*- coding: utf-8 -*-

"""
.. py:currentmodule:: leukapp.apps.individuals

Application used to track and edit :class:`Individuals <models.Indiviual>`.

The main model of this application is the
:py:class:`~models.Indiviual`. This model represents the top class in
the **Leukgen** ecosystem, it usually refers to patients, mice and other kind
of organisms.

It's child model is the :class:`~leukapp.apps.specimens.models.Specimen`
which is managed by the :mod:`~leukapp.apps.specimens` application.

"""
