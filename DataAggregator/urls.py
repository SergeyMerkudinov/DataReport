from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about',views.about, name='about'),
    path('coaches', views.coaches, name='coaches'),
    path('search', views.filteredCoaches, name='search')
]