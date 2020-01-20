from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
# Create your views here.

def index(request):
    return  render(request, 'index.html', {'template_name':'index'})

def about(request):
    return render(request, 'about.html', {'template_name':'about'})

def coaches(request):
    return render(request, 'coaches.html', {'template_name':'coaches'})