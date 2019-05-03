from django.urls import path, re_path
from . import views

urlpatterns = [
    re_path(r'^$', views.projects_list, name='projects_list'),
    re_path(r'^my/$', views.my_projects, name='my_projects'),
    re_path(r'^add/$', views.create_project, name='create_project'),
    re_path(r'^(?P<slug>[\w-]+)/$', views.single_project, name='single_project'),
    re_path(r'^(?P<slug>[\w-]+)/edit/$', views.edit_project, name='edit_project'),
    re_path(r'^(?P<slug>[\w-]+)/delete/$', views.delete_project, name='delete_project'),
]
