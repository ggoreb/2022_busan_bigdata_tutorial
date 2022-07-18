from django.contrib import admin
from django.urls import include, path
from . import views

urlpatterns = [
  # Shift + Alt + ↓
  path('main/', views.main),
  path('insert/', views.insert),
  path('show/', views.show),
  path('army_shop/', views.army_shop),
  path(
    'army_shop/<int:year>/<int:month>/', 
    views.army_shop_path),
]