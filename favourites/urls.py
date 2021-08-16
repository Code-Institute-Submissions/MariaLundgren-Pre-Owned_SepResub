from django.urls import path
from . import views

urlpatterns = [
    path('', views.favourites, name='favourites'),
    path('favourite_list', views.favourite_list,
         name='favourite_list'),
]
