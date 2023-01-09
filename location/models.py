from django.contrib.postgres.fields import JSONField
from django.db import models

from django.utils.translation import ugettext_lazy as _

from lib.common_models import BaseModel


class Location(BaseModel):
    title = models.CharField(_("title"), max_length=32)
    points = JSONField(_("points"))  # sample: {'lat': 32.093452354, 'long': 65.23452354234}

    class Meta:
        verbose_name = _("Location")
        verbose_name_plural = _("Locations")

    def __str__(self):
        return self.title
