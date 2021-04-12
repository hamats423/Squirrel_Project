from django.urls import path
from . import views
urlpatterns = [
        path('', views.index,name='index'),
        path('add/', views.AddSquirrel, name ='add'),
        path('<squirrel_id>/', views.UpdateSquirrel, name = 'update'),
        path('stats/', views.Stats, name = 'stat'),
]

