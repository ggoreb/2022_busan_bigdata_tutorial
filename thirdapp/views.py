from django.shortcuts import render
from .models import Emp, Shop, JejuOlle

def shop(request):
  shop_list = Shop.objects.all()
  return render(
    request,
    'thirdapp/shop.html',
    {'shop_list': shop_list}
  )

def jeju_olle(request):
  q = request.GET.get('q')

  # jeju_olle_list = JejuOlle.objects.all()
  jeju_olle_list = JejuOlle.objects.filter(
    course_name__contains=q)

  return render(
    request,
    'thirdapp/jeju_olle.html',
    {'jeju_olle_list': jeju_olle_list}
  )

from django.http import JsonResponse
from django.forms.models import model_to_dict
from .models import Emp

# 장고 모델 자료형태 반환
def model_data(request):
  emp = Emp.objects.all()

  data = []
  for c in emp:
    c = model_to_dict(c) # QuerySet -> Dict
    data.append(c)
  # dict가 아닌 자료는 항상 safe=False 옵션 사용
  return JsonResponse(data, safe=False)


def jeju_olle_search(request, course_name):
  jeju_olle_list = JejuOlle.objects.filter(
    course_name__contains=course_name)

  # return render(
  #   request,
  #   'thirdapp/jeju_olle.html',
  #   {'jeju_olle_list': jeju_olle_list}
  # )

  data = []
  for c in jeju_olle_list:
    c = model_to_dict(c)
    data.append(c)
  return JsonResponse(data, safe=False)
