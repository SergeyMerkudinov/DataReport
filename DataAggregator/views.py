import urllib.parse
from urllib.parse import parse_qs


from django.shortcuts import render
from django.http import HttpResponse

from  .apps import DataaggregatorConfig
from django.apps import apps
from DataAggregator.library.DataLoader import DataLoader

from .models import Coach

def index(request):
    return render(request, 'index.html', {'template_name': 'index'})


def about(request):
    return render(request, 'about.html', {'template_name': 'about'})


def coaches(request):
    return render(request, 'coaches.html', {'template_name': 'coaches', 'coachList': DataLoader(DataaggregatorConfig).extract(maxRecords=DataaggregatorConfig.DATA_LOAD_MAX_RECORDS)})

def filteredCoaches(request):
    body_unicode = request.body.decode('utf-8')
    body = parse_qs(body_unicode)
    return render(request, 'coaches.html', {'template_name': 'coaches', 'coachList': DataLoader(DataaggregatorConfig).extract(query=body['queryString'][0])})
