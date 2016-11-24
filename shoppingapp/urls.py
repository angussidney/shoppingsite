from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^categories/$', views.categories, name='categories'),
    url(r'^categories/(?P<category_id>[0-9]+)/', views.category_detail, name='category_detail'),
    url(r'^products/$', views.products, name='products'),
    url(r'^products/(?P<product_id>[0-9]+)/', views.product_detail, name='product_detail'),
]
