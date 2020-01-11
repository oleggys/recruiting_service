from django.urls import path, include
from . import views


urlpatterns = [
    path('test_for_recruiters/<int:clan_id>', views.test_for_recruiters, name='test_for_recruiters'),
    path('recruiters_for_sith', views.recruiters_for_sith, name='recruiters_for_sith'),
    path('answers/<int:recruiter_id>', views.check_user_answers, name='user_answers'),
    path('thanks', views.thanks_view, name='thanks'),
]
