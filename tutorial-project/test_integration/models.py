from django.db import models
from django.utils.translation import ugettext_lazy as _
from cms.models.pluginmodel import CMSPlugin
# Create your models here.

SIZES_PLACEHOLDERS= (
    #   Example
    # ('150', _('150x150')),
    # ('300', _('300x300')),
    ('450', _('Small')),
    ('700', _('Big')),
)


class EventCardModel(CMSPlugin):
        size = models.CharField(_('Size'), max_length=255,
                                choices=SIZES_PLACEHOLDERS, default='150')
        title = models.CharField(_('Title'), max_length=2500)
        date = models.DateField(_('Event Date'), blank=True, null=True)


class ContainerModel(CMSPlugin):
    pass