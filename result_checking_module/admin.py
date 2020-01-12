from django.contrib import admin
from result_checking_module.models import Test, Question, RecruiterAnswer, EndTestRecruiter

# Register your models here.

admin.site.register(RecruiterAnswer)


class QuestionAdminModel(admin.TabularInline):
    model = Question


@admin.register(EndTestRecruiter)
class EndTestRecruiterAdminModel(admin.ModelAdmin):
    list_display = ('get_recruiter_name', 'get_test_name')

    def get_recruiter_name(self, obj):
        return obj.recruiter.name

    def get_test_name(self, obj):
        return obj.test.name

    get_recruiter_name.short_description = 'recruiter name'
    get_test_name.short_description = 'test name'


@admin.register(Test)
class TestAdminModel(admin.ModelAdmin):
    inlines = [
        QuestionAdminModel,
    ]

