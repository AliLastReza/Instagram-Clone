from django.db import models


class BaseModel(models.Model):
    created_time = models.DateField(verbose_name='created_time', auto_now=True)
    modified_time = models.DateField(verbose_name='modified_time', auto_now_add=True)

    class Meta:
        abstract = True