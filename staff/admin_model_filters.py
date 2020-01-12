from django.contrib import admin
from django.db.models import QuerySet

from staff.models import Sith


class CountDarkHandsFilter(admin.SimpleListFilter):
    title = 'Count of dark hand'
    parameter_name = 'count'

    def lookups(self, request, model_admin):
        return (('>1', 'count > 1 dark hand'),)

    def queryset(self, request, queryset):
        if self.value() == '>1':
            need_objects_id = []
            for obj in queryset:
                if obj.count_of_dark_hand() > 1:
                    need_objects_id.append(obj.id)
            return queryset.filter(id__in=need_objects_id)
