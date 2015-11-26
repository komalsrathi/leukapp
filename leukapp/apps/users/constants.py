# -*- coding: utf-8 -*-

"""
This module contains the :mod:`~leukapp.apps.users` app constants.
Information that isn't likely to change and that is used across the
:mod:`~leukapp.apps.users` app and the :mod:`~leukapp` project
should be stored here.

.. important::
    **DO NOT** change any constant unless you know what you are doing.
"""

# APP INFO
# =============================================================================
APP_NAME = 'users' #: Application's name.

# FIELDS
# =============================================================================

USER_UNIQUE_TOGETHER = ('email', )
""" Fields that are required to be unique together. """
