from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^categories/', views.categories, name='categories'),
    url(r'^products/', views.products, name='products'),
]
