from django.urls import path, re_path
from . import views

urlpatterns = [
    re_path(r'^$', views.categories_list, name='categories_list'),
    re_path(r'^(?P<slug>[\w-]+)/$', views.single_category, name='single_category'),
]
