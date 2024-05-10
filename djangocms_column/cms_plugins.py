from django.utils.translation import gettext_lazy as _

from cms.models import CMSPlugin
from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from cms import api
from .forms import MultiColumnForm
from .models import Column, MultiColumns


class MultiColumnPlugin(CMSPluginBase):
    model = MultiColumns
    module = _("Multi Columns")
    name = _("Multi Columns")
    render_template = "cms/plugins/multi_column.html"
    allow_children = True
    child_classes = ["ColumnPlugin"]
    form = MultiColumnForm

    def save_model(self, request, obj, form, change):
        response = super().save_model(
            request, obj, form, change
        )
        for _x in range(int(form.cleaned_data['create'])):
            col = api.add_plugin(
                placeholder=obj.placeholder,
                plugin_type=ColumnPlugin.__name__,
                language=obj.language,
                target=obj,
                width=form.cleaned_data['create_width'],
            )
            col.save()
        return response


class ColumnPlugin(CMSPluginBase):
    model = Column
    module = _("Multi Columns")
    name = _("Column")
    render_template = "cms/plugins/column.html"
    parent_classes = ["MultiColumnPlugin"]
    allow_children = True


plugin_pool.register_plugin(MultiColumnPlugin)
plugin_pool.register_plugin(ColumnPlugin)
