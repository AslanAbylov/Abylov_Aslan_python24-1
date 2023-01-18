from django.shortcuts import render, HttpResponse
from datetime import datetime
from . models import Products, Review



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

def review_view(request, id):
    if request.method == 'GET':
        product = Products.objects.get(id=id)
        reviews = Review.objects.filter(product=product)
        return render(request, 'posts/detail.html', context={
            'reviews': reviews,
            'product': product
        })
