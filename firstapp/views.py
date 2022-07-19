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

def date(request, year, month):
  return HttpResponse('%s - %s' % (year, month))

def search(request):
  page = request.GET.get('page')
  title = request.GET.get('title')

  return HttpResponse('%s - %s' % (page, title))

def req_get(request):
  a = request.GET.get('a')
  b = request.GET.get('b')
  c = request.GET['c']
  result = '%s %s %s' % (a, b, c)
  return HttpResponse(result)

def req_post(request):
  
  if request.method == 'POST':
    a = request.POST.get('a')
    b = request.POST.get('b')
    c = request.POST['c']
    result = '%s %s %s' % (a, b, c)
    return HttpResponse(result)

  return render(request, 'firstapp/post.html')

def template(request):
  return render(
    request, 'firstapp/template.html')

from firstapp.forms import NameForm

def basic_form(request):
  if request.method == 'POST':
    # 사용자의 요청 데이터 입력 + 유효성 검사
    form = NameForm(request.POST)  
  else:
    form = NameForm()

  return render(
    request,
    'firstapp/basic_form.html',
    { 'form': form }
  )

from django.shortcuts import redirect
from .forms import CurriculumForm
def form_model(request):
  if request.method == 'POST':
    form = CurriculumForm(request.POST)
    if form.is_valid():
      curriculum = form.save(commit=False)
      # (필요하다면) 데이터 추가 / 변경
      curriculum.save()

      return redirect('/first/form/model/')
  else:
    form = CurriculumForm()
  return render(
    request, 'firstapp/form_model.html',
    { 'form': form }
  )