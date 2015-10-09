from django.db import models
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _


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

    slug = models.SlugField(
        _("slug"),
        max_length=100,
        unique=True,
        )

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        """
        slug requires pk for new objects
        """

        new = not self.pk
        super(LeukappModel, self).save(*args, **kwargs)

        # http://stackoverflow.com/questions/9940674/django-model-manager-objects-create-where-is-the-documentation

        if new:
            kwargs['force_insert'] = False  # set to avoid in error in create()
            self.if_new()
            self.if_save()
            super(LeukappModel, self).save(*args, **kwargs)

        else:
            self.if_save()
            super(LeukappModel, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse(
            self.APP_NAME + ':detail', kwargs={'slug': self.slug}
        )

    def get_update_url(self):
        return reverse(
            self.APP_NAME + ':update', kwargs={'slug': self.slug}
        )

    def if_new(self, **kwargs):
        pass

    def if_save(self, **kwargs):
        pass
