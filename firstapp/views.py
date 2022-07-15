from django.http import HttpResponse
from django.shortcuts import render

def index1(request):
  return HttpResponse('<u>Hello</u>')

def index2(request):
  return HttpResponse('<u>Hi</u>')

def main(request):
  return HttpResponse('<u>Main</u>')

from .models import Curriculum
def insert(request):
  # 1-linux 입력
  Curriculum.objects.create(name='linux')
  # 2-python 입력
  c = Curriculum(name='python')
  c.save()
  # 3-html/css/js 입력
  Curriculum(name='python').save()
  # 4-django 입력
  Curriculum(name='django').save()
  return HttpResponse('데이터 입력 완료')

def show(request):
  curriculum = Curriculum.objects.all()
  # result = ''
  # for c in curriculum:
  #   result += c.name + '<br>'
  # return HttpResponse(result)

  #      인자 3개   1-request, 2-템플릿, 3-context (딕셔너리)
  return render(request, 'firstapp/show.html', {
    'my_data': curriculum, 'age': 30
  })