from django.db import models
from django.utils.translation import ugettext_lazy as _
from django_mysql.models import QuerySet


class BaseModel(models.Model):
    created = models.DateTimeField(
        verbose_name=_('created'),
        help_text=_('object creation time'),
        auto_now_add=True,
    )

    modified = models.DateTimeField(
        verbose_name=_('modified'),
        help_text=_('object modification time'),
        auto_now=True,
    )

    objects = QuerySet.as_manager()

    class Meta:
        abstract = True
