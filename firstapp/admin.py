from django.contrib import admin

#   현재경로의 models 라는 모듈에서 Curriculum 가져오기
from .models import Curriculum

admin.site.register(Curriculum)