from django.http import HttpResponse
from django.shortcuts import render


def home_page(request):
  context = {'title': 'my_title'}
  return render(request, 'index.html')

def home_page2(request):
    return render(request, 'indexprofil.html', {'title': 'About'})

def faisal(request):
    return render(request, 'faisal.html', {'title': 'About'})
