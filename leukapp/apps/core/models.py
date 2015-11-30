# -*- coding: utf-8 -*-

"""
Abstract models used across the :mod:`leukapp` project.
"""

# python
import inspect

# django
from django.db import models
from django.core.urlresolvers import reverse
from django.db import transaction


class TimeStampedModel(models.Model):

    """
    An abstract base class model that provides self-updating
    ``created`` and ``modified`` fields.

    See: http://blog.kevinastone.com/django-model-behaviors.html
    """

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class LeukappModel(TimeStampedModel):

    """
    **Leukapp** abstract base model.

    This model has several methods that are shared across the **Leukapp**
    project. This implementation is mainly motivated by the DRY concept.
    """

    # META CLASS
    # =========================================================================
    class Meta:
        abstract = True

    # PUBLIC METHODS
    # =========================================================================
    @transaction.atomic
    def save(self, *args, **kwargs):
        """
        `Atomic`_ method to save the :class:`LeukappModel`.

        While executed, calls two methods:

            * :meth:`_if_new`: only called at creation, used to generate IDs.
            * :meth:`_if_save`: called every time the object is saved.

        The ``slug`` identification system is based on the use of primary keys.
        As such, the :class:`LeukappModel` must be saved before generating the
        ``slug``.

        The keyword argument ``force_insert`` is set to ``False`` in order to
        avoid error while using :meth:`create` (see `this question`_).

        .. _this question: http://stackoverflow.com/questions/9940674/django-model-manager-objects-create-where-is-the-documentation
        .. _Atomic: https://docs.djangoproject.com/en/1.8/topics/db/transactions/#controlling-transactions-explicitly
        """

        if not self.pk:
            super(LeukappModel, self).save(*args, **kwargs)  # get pk
            kwargs['force_insert'] = False  # set to avoid error in create()
            self._if_new()
            self._if_save()
        else:
            self._if_save()

        super(LeukappModel, self).save(*args, **kwargs)

    def get_absolute_url(self):
        """
        Returns the object detail url.
        """
        return reverse(self.APP_NAME + ':detail', kwargs={'slug': self.slug})

    def get_update_url(self):
        """
        Returns the object's update url.
        """
        return reverse(self.APP_NAME + ':update', kwargs={'slug': self.slug})

    # PRIVATE METHODS
    # =========================================================================

    def _if_new(self, **kwargs):
        """
        :meth:`_if_new` is executed the first time the object is created.
        """
        pass

    def _if_save(self, **kwargs):
        """
        :meth:`_if_save` is executed everytime the object is saved.
        """
        pass

    def _check_if_caller_is_if_new(self):
        """
        Checks if current function is been called from :meth:`_if_new`.
        This ensures the atomicity of the IDs generation.
        """

        # NOTTESTED
        msg = "This function can only be called from _if_new()."
        try:
            if inspect.stack()[2][3] != '_if_new':
                raise(Exception(msg))
        except IndexError:
            raise(Exception(msg))

    def _check_if_caller_is_save(self):
        """
        Checks if current method is been called from :meth:`save`.
        This ensures the atomicity of the IDs generation.
        """

        msg = "This function can only be called from save()."
        try:
            if inspect.stack()[2][3] != 'save':
                raise(Exception(msg))
        except IndexError:
            raise(Exception(msg))


class LeukappTestModel(LeukappModel):

    """
    This class only serves the purpose of testing the core's abstract models.
    """

    def _if_save(self):
        self._check_if_caller_is_save()
        self.slug = self.pk

    def _if_new(self):
        self._check_if_caller_is_save()
        self._test()

    def _test(self):
        self._check_if_caller_is_if_new()
