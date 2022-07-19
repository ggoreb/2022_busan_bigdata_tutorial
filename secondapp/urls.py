from django.contrib import admin
from django.urls import include, path
from . import views

app_name = 'secondapp'

urlpatterns = [
  path('course/create/', views.course_create, name='course_create'),


  # Shift + Alt + ↓
  path('main/', views.main),
  path('insert/', views.insert),
  path('show/', views.show, name='show'),
  path('army_shop/', views.army_shop, name='army_shop'),
  path(
    'army_shop/<int:year>/<int:month>/', 
    views.army_shop_path),

  path('army_shop/add/', views.army_shop_add),
  path(
    'army_shop/remove/', 
    views.army_shop_remove),

]