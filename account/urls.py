from django.urls import path, re_path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    re_path(r'^register/$', views.register, name='register'),
    re_path(r'^edit/$', views.edit, name='edit'),
]
