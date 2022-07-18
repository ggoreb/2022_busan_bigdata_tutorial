from django.contrib import admin
from django.urls import include, path
from . import views

urlpatterns = [
  path('main/', views.main),
  path('insert/', views.insert),
  path('show/', views.show),
  
  # path parameter
  path(
    '<str:year>/<int:month>', 
    views.date),
    
  # query parameter
  path(
    'search/', 
    views.search)
]