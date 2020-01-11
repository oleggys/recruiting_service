from django.contrib import admin
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


@admin.register(Sith)
class SithAdminModel(admin.ModelAdmin):
    list_display = ('name', 'get_planet_name')
    search_fields = ('name', 'get_planet_name')
    inlines = [
        DarkHandAdminModel,
    ]

    def get_planet_name(self, obj):
        return obj.clan.planet.name