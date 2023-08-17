from django.shortcuts import render

from main.models import Product


def home(request):
    products = Product.objects.all()
    return render(request, 'main/home.html', {'products': products})


def contact(request):
    return render(request, 'main/contact.html')
