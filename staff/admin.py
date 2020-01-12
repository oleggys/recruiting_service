from django.contrib import admin

from staff.admin_model_filters import CountDarkHandsFilter
from staff.models import Planet, Recruiter, Sith, Clan, DarkHand

# Register your models here.

admin.site.register(Planet)
admin.site.register(Clan)


class DarkHandAdminModel(admin.TabularInline):
    model = DarkHand


@admin.register(Recruiter)
class RecruiterAdminModel(admin.ModelAdmin):
    list_display = ('name', 'email', 'get_planet_name', 'get_age')
    search_fields = ('name', 'email')

    def get_planet_name(self, obj):
        return obj.planet.name

    get_planet_name.short_description = 'planet name'


@admin.register(Sith)
class SithAdminModel(admin.ModelAdmin):
    list_display = ('name', 'get_planet_name', 'count_of_dark_hand')
    search_fields = ('name', 'get_planet_name')
    inlines = [
        DarkHandAdminModel,
    ]
    list_filter = [CountDarkHandsFilter]

    def get_planet_name(self, obj):
        return obj.clan.planet.name

    # def get_count_of_dark_hand(self, obj):
    #     return len(DarkHand.objects.filter(sith=obj))

    # get_count_of_dark_hand.short_description = 'count of dark hand'
    get_planet_name.short_description = 'planet name'