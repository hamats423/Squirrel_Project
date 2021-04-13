from django.urls import path
from . import views
from django.conf.urls import url

urlpatterns = [
        path('', views.index, name='index'),
        path('add/', views.AddSquirrel, name ='add'),
        path('<unique_squirrel_id>/', views.UpdateSquirrel, name = 'update'),
        path('stats/', views.Stats, name = 'stat'),
]

