from django.shortcuts import render, HttpResponse
from datetime import datetime

def Hello(request):
    if request.method == 'GET':
        return HttpResponse('Hello')

def now_date(request):
    if request.method == 'GET':
        return HttpResponse(datetime.now().date())

def goodby(request):
    if request.method == 'GET':
        return HttpResponse('Goodby user!')