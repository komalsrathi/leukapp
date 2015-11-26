# -*- coding: utf-8 -*-

"""
This module contains the :mod:`~leukapp.apps.core` app constants.
Information that isn't likely to change and that is used across the
:mod:`~leukapp.apps.core` app and the :mod:`~leukapp` project
should be stored here.

.. important::
    **DO NOT** change any constant unless you know what you are doing.
"""

# APP INFO
# =============================================================================
APP_NAME = 'core'  #: Application's name.

# VARIABLES
# =============================================================================
UNKNOWN = 'UNKNOWN'
"""
Value used accross the :mod:`~leukapp` project to described **unknown**
information.
"""

# MESSAGES
# =============================================================================
SUCCESS_MESSAGE = "Looking good"
""" Success message used across the :mod:`~leukapp.apps` package. """

PERMISSION_DENIED_MESSAGE = \
    ''' You don't have permission to perform this action, please contact a
    Leukgen Administrator. '''
""" Permission denied message used across the :mod:`~leukapp.apps` package. """
