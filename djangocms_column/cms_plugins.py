from cms.plugin_pool import plugin_pool
from cms.plugin_base import CMSPluginBase
from djangocms_column.models import MultiColumns, Column
from django.utils.translation import ugettext_lazy as _
from djangocms_column.forms import MultiColumnForm
from cms.models import CMSPlugin

class MultiColumnPlugin(CMSPluginBase):
    model = MultiColumns
    name = _("Multi Columns")
    render_template = "cms/plugins/multi_column.html"
    allow_children = True
    child_classes = ["ColumnPlugin"]
    form = MultiColumnForm

    def render(self, context, instance, placeholder):
        context.update({
            'instance': instance,
            'placeholder':placeholder,
        })
        return context

    def save_model(self, request, obj, form, change):
        response = super(MultiColumnPlugin, self).save_model(request, obj, form, change)
        for x in xrange(int(form.cleaned_data['create'])):
            col = Column(parent=obj, placeholder=obj.placeholder, language=obj.language, width=form.cleaned_data['create_width'], position=CMSPlugin.objects.filter(parent=obj).count(), plugin_type=ColumnPlugin.__name__)
            col.save()
        return response

class ColumnPlugin(CMSPluginBase):
    model = Column
    name = _("Column")
    render_template = "cms/plugins/column.html"
    frontend_edit_template = 'cms/plugins/column_edit.html'
    allow_children = True

    def render(self, context, instance, placeholder):
        context.update({
            'instance': instance,
            'placeholder':placeholder,
            })
        return context

plugin_pool.register_plugin(MultiColumnPlugin)
plugin_pool.register_plugin(ColumnPlugin)
