from django.contrib import admin
from django.urls import include, path

from airport import views

urlpatterns = [
    path("", views.city_list, name="city_list"),
    path("home/", views.index, name="index"),
    path('search/<str:from_city>/<str:to_city>/<str:departure_date>/', views.search, name='search_flights'),
    path('not_found/<str:from_city>/<str:to_city>/<str:departure_date>/', views.search, name='not_found')
]