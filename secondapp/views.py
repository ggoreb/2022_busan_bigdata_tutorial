from django.http import HttpResponse
from django.shortcuts import render

def main(request):
  return HttpResponse('<u>Main</u>')

from .models import Course
def insert(request):
  Course.objects.create(name='데이터 분석', cnt=30)
  c = Course(name='데이터 수집', cnt=20)
  c.save()
  Course(name='웹개발', cnt=25).save()
  Course(name='인공지능', cnt=20).save()
  return HttpResponse('데이터 입력 완료')

def show(request):
  course = Course.objects.all()

  # result = ''
  # for c in course:
  #   # result += c.name + str(c.cnt) + '<br>'
  #   result += '%s (%s)<br>' % (c.name, c.cnt)
  # return HttpResponse(result)

  return render(
    request, 'secondapp/show.html', 
    { 'course_list': course }
  )

from .models import ArmyShop
def army_shop(request):
  shops = ArmyShop.objects.order_by('-id')
  return render(
    request, 'secondapp/army_shop.html',
    { 'shops': shops }
  )