from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from .models import EventCardModel, ContainerModel
from django.utils.translation import ugettext as _


@plugin_pool.register_plugin  # register the plugin
class PollContainerPlugin(CMSPluginBase):
    model = ContainerModel  # model where plugin data are saved
    # module = _("Container")
    name = _("Poll_Container")  # name of the plugin in the interface
    render_template = "container.html"
    allow_children = True
    child_classes = ['EventCardPlugin']

    def render(self, context, instance, placeholder):
        context.update({'instance': instance})
        return context



@plugin_pool.register_plugin  # register the plugin
class EventCardPlugin(CMSPluginBase):
    model = EventCardModel  # model where plugin data are saved
    # module = _("Container")
    name = _("Event Card")  # name of the plugin in the interface
    render_template = "event.html"

    def render(self, context, instance, placeholder):
        context.update({'instance': instance})
        context['size'] = instance.size
        return context
