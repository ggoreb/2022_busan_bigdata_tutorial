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
  jeju_olle_list = JejuOlle.objects.all()
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