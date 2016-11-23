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
    categories_list = Category.objects.order_by('category_name')
    context = {'categories_list': categories_list}
    return render(request, 'shoppingapp/categories.html', context)

def products(request):
    products_list = Product.objects.order_by('product_name')
    context = {'products_list': products_list}
    return render(request, 'shoppingapp/products.html', context)
