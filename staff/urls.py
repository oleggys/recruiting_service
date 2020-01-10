from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('sith_auth', views.sith_auth, name='sith_auth'),
    path('recruiter_auth', views.recruiter_auth, name='recruiter_auth'),
]
