from django.contrib import admin
from django.utils.translation import ugettext_lazy as _


class CategoryFatherListFilter(admin.SimpleListFilter):
    # Human-readable title which will be displayed in the
    # right admin sidebar just above the filter options.
    title = _('所有分类')

    # Parameter for the filter that will be used in the URL query.
    parameter_name = 'father_id'

    def lookups(self, request, model_admin):
        """
        Returns a list of tuples. The first element in each
        tuple is the coded value for the option that will
        appear in the URL query. The second element is the
        human-readable name for the option that will appear
        in the right sidebar.
        """
        return (
            ('-1', _('一级分类')),
        )

    def queryset(self, request, queryset):
        """
        Returns the filtered queryset based on the value
        provided in the query string and retrievable via
        `self.value()`.
        """
        # Compare the requested value (either '80s' or '90s')
        # to decide how to filter the queryset.
        if self.value() == '-1':
            return queryset.filter(father_id=-1)

    def __init__(self, request, params, model, model_admin):
        super().__init__(request, params, model, model_admin)

