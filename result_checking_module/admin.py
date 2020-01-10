from django.contrib import admin
from result_checking_module.models import Test, Question


# Register your models here.

class QuestionAdminModel(admin.TabularInline):
    model = Question


@admin.register(Test)
class TestAdminModel(admin.ModelAdmin):
    inlines = [
        QuestionAdminModel,
    ]

