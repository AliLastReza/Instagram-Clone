from django.contrib.postgres.fields import JSONField
from django.db import models


from lib.common_models import BaseModel
from django.utils.translation import ugettext_lazy as _


class Location(BaseModel):
    title = models.CharField(_('title'), max_length=32)
    points = JSONField(_('points'), blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _("Location")
        verbose_name_plural = _("Locations")