# -*- coding: utf-8 -*-

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
    Leukapp Base Model
    """

    class Meta:
        abstract = True

    @transaction.atomic
    def save(self, *args, **kwargs):
        """
        slug requires pk for new objects
        """

        new = not self.pk

        # http://stackoverflow.com/questions/9940674/django-model-manager-objects-create-where-is-the-documentation

        if new:
            super(LeukappModel, self).save(*args, **kwargs)  # get pk
            kwargs['force_insert'] = False  # set to avoid error in create()
            self._if_new()
            self._if_save()

        else:
            self._if_save()

        super(LeukappModel, self).save(*args, **kwargs)

    def get_absolute_url(self):
        """ Returns the object detail url. """
        return reverse(self.APP_NAME + ':detail', kwargs={'slug': self.slug})

    def get_update_url(self):
        """ Returns the object's update url. """
        return reverse(self.APP_NAME + ':update', kwargs={'slug': self.slug})

    def _if_new(self, **kwargs):
        """ _if_new is executed the first time the object is created. """
        pass

    def _if_save(self, **kwargs):
        """ _if_save is executed everytime the object is saved. """
        pass

    def _check_if_caller_is_if_new(self):
        """ Checks if current function is been called from _if_new(). """

        # NOTTESTED
        msg = "This function can only be called from _if_new()."
        try:
            if inspect.stack()[2][3] != '_if_new':
                raise(Exception(msg))
        except IndexError:
            raise(Exception(msg))

    def _check_if_caller_is_save(self):
        """ Checks if current function is been called from save(). """

        # NOTTESTED
        msg = "This function can only be called from save()."
        try:
            if inspect.stack()[2][3] != 'save':
                raise(Exception(msg))
        except IndexError:
            raise(Exception(msg))


class LeukappTestModel(LeukappModel):

    """
    this model only serves the purpose of testing the abstract models above
    """

    def _if_save(self):
        """
        _if_save is executed everytime the object is saved
        test: test_str_returns_slug
        """

        self.slug = self.pk
