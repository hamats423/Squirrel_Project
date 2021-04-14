from django.urls import path, re_path
from . import views
from django.conf.urls import url

urlpatterns = [
        path('', views.index, name='index'),
        path('add/', views.AddSquirrel, name ='add'),
        re_path(r'^(?P<unique_id>[A-Z0-9-]+)', views.UpdateSquirrel, name = 'update'),
        path('stats/', views.Stats, name = 'stat'),
]

