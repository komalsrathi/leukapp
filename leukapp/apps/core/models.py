# -*- coding: utf-8 -*-

# django
from django.db import models
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _
from django.db import transaction


class TimeStampedModel(models.Model):

    """
    An abstract base class model that provides self-updating
    ``created`` and ``modified`` fields.
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
            self.if_new()
            self.if_save()

        else:
            self.if_save()

        super(LeukappModel, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse(self.APP_NAME + ':detail', kwargs={'slug': self.slug})

    def get_update_url(self):
        return reverse(self.APP_NAME + ':update', kwargs={'slug': self.slug})

    def if_new(self, **kwargs):
        pass

    def if_save(self, **kwargs):
        pass


class LeukappTestModel(LeukappModel):

    """
    this model only serves the purpose of testing the abstract models above
    """

    def if_save(self):
        """
        if_save is executed everytime the object is saved
        test: test_str_returns_slug
        """

        self.slug = self.pk
