from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect

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

def category_detail(request, category_id):
    category = get_object_or_404(Category, pk=category_id)
    context = {'category': category}
    return render(request, 'shoppingapp/category_detail.html', context)

def products(request):
    products_list = Product.objects.order_by('product_name')
    context = {'products_list': products_list}
    return render(request, 'shoppingapp/products.html', context)

def product_detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    context = {'product': product,
               'range': range(product.stock)}
    return render(request, 'shoppingapp/product_detail.html', context)

def search(request):
    categories_list = Category.objects.order_by('category_name')
    context = {'categories_list': categories_list}
    return render(request, 'shoppingapp/search.html', context)

def buy(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    quantity = request.POST.get("quantity", 0)
    if quantity > product.stock:
        return render(request, 'shoppingapp/product_detail.html', {
            'product': product,
            'status': "Error: Not enough items in stock",
        })
    else:
        product.stock -= quantity
        product.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return render(request, 'shoppingapp/product_detail.html', {
            'product': product,
            'status': "Success! Your order has been placed.",
        })
