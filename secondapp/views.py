from django.forms import model_to_dict
from django.http import HttpResponse, JsonResponse
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
  prd = request.GET.get('prd')
  if not prd:
    prd = ''

  # shops = ArmyShop.objects.order_by('-id')
  shops = ArmyShop.objects.filter(
    name__contains=prd).order_by('-id')
  # return render(
  #   request, 'secondapp/army_shop.html',
  #   { 'shops': shops }
  # )

  data = []
  for c in shops:
    c = model_to_dict(c)
    data.append(c)
  return JsonResponse(data, safe=False)

def army_shop_path(request, year, month):
  shops = ArmyShop.objects.filter(
    year=year, month=month).order_by('-id')
  return render(
    request, 'secondapp/army_shop.html',
    { 'shops': shops }
  )

def army_shop_add(request):
  if request.method == 'POST':
    year = request.POST.get('year')
    month = request.POST.get('month')
    type = request.POST.get('type')
    name = request.POST.get('name')

    army = ArmyShop(
      year=year, month=month, 
      type=type, name=name)
    army.save()

    return HttpResponse('입력 완료 %s' % name)

  return render(
    request, 
    'secondapp/army_shop_add.html')

def army_shop_remove(request):
  id = request.GET.get('id')

  army = ArmyShop.objects.get(pk=id)
  name = army.name
  army.delete()

  return HttpResponse('삭제 완료 %s' % name)

from django.shortcuts import redirect
from .forms import CourseForm
def course_create(request):
  if request.method == 'POST':
    form = CourseForm(request.POST)
    if form.is_valid():
      course = form.save(commit=False)
      course.save()

      return redirect('/second/course/create/')
  else:
    form = CourseForm()
  return render(
    request, 'secondapp/course_create.html',
    { 'form': form }
  )