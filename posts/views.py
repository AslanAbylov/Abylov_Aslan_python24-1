from django.shortcuts import render, HttpResponse
from datetime import datetime
from . models import Products

def Hello(request):
    if request.method == 'GET':
        return HttpResponse('Hello')

def main_view(request):
    if request.method == 'GET':
        return render(request, 'layouts/index.html')



def product_view(request):
    if request.method == 'GET':
        products = Products.objects.all()
        context = {
            'products': products
        }

        return render(request, 'posts/posts.html', context=context)
