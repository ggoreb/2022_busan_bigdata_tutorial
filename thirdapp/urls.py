from django.urls import path
from . import views

app_name = 'thirdapp'

urlpatterns = [
  path('shop/', views.shop),
  path('jeju_olle/', views.jeju_olle, name='jeju_olle'),
  path('model_data/', views.model_data),

  path(
    'jeju_olle/<str:course_name>/', 
    views.jeju_olle_search),
]