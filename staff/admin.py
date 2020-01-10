from django.contrib import admin
from staff.models import Planet, Recruiter, Sith, Clan

# Register your models here.

admin.site.register(Planet)
admin.site.register(Clan)


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

    def get_planet_name(self, obj):
        return obj.planet.name