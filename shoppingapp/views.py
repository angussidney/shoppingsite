from django.shortcuts import render
from django.http import HttpResponse

from .models import *

# Create your views here.
def index(request):
    newest_products_list = Product.objects.order_by('-date_added')[:4]
    specials_list = Product.objects.filter(special__gt=0.0);
    context = {'newest_products_list': newest_products_list,
               'specials_list': specials_list}
    return render(request, 'shoppingapp/home.html', context)

def categories(request):
    products_list = Product.objects.order_by('-price')[:4]
    context = {'products_list': products_list}
    return render(request, 'shoppingapp/home.html', context)
