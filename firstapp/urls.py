from django.contrib import admin
from django.urls import include, path
from . import views

app_name = 'firstapp'

urlpatterns = [
  path('form/model/', views.form_model),
  path('form/basic/', views.basic_form),

  path('template/', views.template),

  path('req/get/', views.req_get),
  path('req/post/', views.req_post),

  path('main/', views.main),
  path('insert/', views.insert),
  path('show/', views.show, name='show'),
  
  # path parameter
  path(
    '<str:year>/<int:month>', 
    views.date),
    
  # query parameter
  path(
    'search/', 
    views.search)
]