from django.urls import path, include
from . import views


urlpatterns = [
    path('test_for_recruiters/<int:clan_id>', views.test_for_recruiters, name='test_for_recruiters'),
    path('thanks', views.thanks_view, name='thanks'),
]
