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

    ext_id = models.CharField(
        _("External ID"),
        max_length=100
        )
    slug = models.CharField(
        _("Slug"),
        max_length=100,
        blank=True
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
            self.slug = self.get_slug()
            super(LeukappModel, self).save(*args, **kwargs)

        else:
            self.slug = self.get_slug()
            super(LeukappModel, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse(
            self.APP_NAME + ':detail', kwargs={'slug': self.slug}
        )

    def get_update_url(self):
        return reverse(
            self.APP_NAME + ':update', kwargs={'slug': self.slug}
        )

    def get_create_url(self):
        return reverse(
            self.APP_NAME + ':create', kwargs={'slug': self.slug}
        )

    def get_slug(self, **kwargs):
        raise NotImplementedError("Implement me")
