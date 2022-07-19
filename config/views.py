from django.http import HttpResponse
from django.shortcuts import render

def home(request):
  return HttpResponse('<u>home</u>')

def index(request):
  return render(
    request,
    'index.html')