from django.shortcuts import render
from django.http import HttpResponse

from .models import *

# Create your views here.
def index(request):
    products_list = Product.objects.order_by('price')
    context = {'products_list': products_list}
    return render(request, 'shoppingapp/home.html', context)
