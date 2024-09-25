from django.shortcuts import render, redirect
from . import models

from django.shortcuts import get_object_or_404

from django.shortcuts import render
from django.http import HttpResponse

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def main(request):
    if request.method == 'POST':
        search = request.POST.get('search')  # 'search' kaliti mavjud bo'lmasa bo'sh string
        product = models.Category.objects.filter(name__icontains=search)

        if product:  # products bo'sh emasligini tekshirish
            return render(request, 'app_main/cart.html', {'products': product, "value": search})
        else:
            return render(request, 'app_main/home.html', {'message': 'No products found'})

    products = models.Category.objects.all()[:8]

    return render(request, 'app_main/home.html'
                  , {'products': products})


def popular(request):
    if request.method == 'POST':
        search = request.POST.get('search')  # 'search' kaliti mavjud bo'lmasa bo'sh string
        product = models.Category.objects.filter(name__icontains=search)

        if product:  # products bo'sh emasligini tekshirish
            return render(request, 'app_main/cart.html', {'products': product, "value": search})
        else:
            return render(request, 'app_main/home.html', {'message': 'No products found'})

    products = models.Category.objects.all().order_by('-rating')[:4]
    return render(request, 'app_main/popular.html'
                  , {'products': products})


def expensive(request):
    if request.method == 'POST':
        search = request.POST.get('search')  # 'search' kaliti mavjud bo'lmasa bo'sh string
        product = models.Category.objects.filter(name__icontains=search)

        if product:  # products bo'sh emasligini tekshirish
            return render(request, 'app_main/cart.html', {'products': product, "value": search})
        else:
            return render(request, 'app_main/home.html', {'message': 'No products found'})

    products = models.Category.objects.all().order_by('-old_price')
    return render(request, 'app_main/expensive.html'
                  , {'products': products})


def likes(request):
    if request.method == 'POST':
        search = request.POST.get('search')  # 'search' kaliti mavjud bo'lmasa bo'sh string
        product = models.Category.objects.filter(name__icontains=search)

        if product:  # products bo'sh emasligini tekshirish
            return render(request, 'app_main/cart.html', {'products': product, "value": search})
        else:
            return render(request, 'app_main/home.html', {'message': 'No products found'})

    products = models.Category.objects.all().order_by('-rating')[:3]

    return render(request, 'app_main/likes.html'
                  , {'products': products})


def cheap(request):
    if request.method == 'POST':
        search = request.POST.get('search')  # 'search' kaliti mavjud bo'lmasa bo'sh string
        product = models.Category.objects.filter(name__icontains=search)

        if product:  # products bo'sh emasligini tekshirish
            return render(request, 'app_main/cart.html', {'products': product, "value": search})
        else:
            return render(request, 'app_main/home.html', {'message': 'No products found'})

    products = models.Category.objects.all().order_by('-new_price')
    return render(request, 'app_main/cheap.html'
                  , {'products': products})


def detail(request, product_id):
    if request.method == 'POST':
        search = request.POST.get('search')  # 'search' kaliti mavjud bo'lmasa bo'sh string
        product = models.Category.objects.filter(name__icontains=search)

        if product:  # products bo'sh emasligini tekshirish
            return render(request, 'app_main/cart.html', {'products': product, "value": search})
        else:
            return render(request, 'app_main/home.html', {'message': 'No products found'})

    product = get_object_or_404(models.Category, id=product_id)

    products = models.Category.objects.all().order_by('-rating')[:5]

    return render(request, 'app_main/detail.html', {'product': product} | {'products': products})


def all_products(request):
    if request.method == 'POST':
        search = request.POST.get('search')  # 'search' kaliti mavjud bo'lmasa bo'sh string
        product = models.Category.objects.filter(name__icontains=search)

        if product:  # products bo'sh emasligini tekshirish
            return render(request, 'app_main/cart.html', {'products': product, "value": search})
        else:
            return render(request, 'app_main/home.html', {'message': 'No products found'})

    products = models.Category.objects.all()
    return render(request, 'app_main/all_products.html'
                  , {'products': products})


def for_sale(request):
    if request.method == 'POST':
        search = request.POST.get('search')  # 'search' kaliti mavjud bo'lmasa bo'sh string
        product = models.Category.objects.filter(name__icontains=search)

        if product:  # products bo'sh emasligini tekshirish
            return render(request, 'app_main/cart.html', {'products': product, "value": search})
        else:
            return render(request, 'app_main/home.html', {'message': 'No products found'})

    products = models.Category.objects.all()
    return render(request, 'app_main/for_sale.html'
                  , {'products': products})


def new_arr(request):
    if request.method == 'POST':
        search = request.POST.get('search')  # 'search' kaliti mavjud bo'lmasa bo'sh string
        product = models.Category.objects.filter(name__icontains=search)

        if product:  # products bo'sh emasligini tekshirish
            return render(request, 'app_main/cart.html', {'products': product, "value": search})
        else:
            return render(request, 'app_main/home.html', {'message': 'No products found'})

    products = models.Category.objects.all().order_by('-created_at')[:4]
    return render(request, 'app_main/new_arr.html'
                  , {'products': products})
