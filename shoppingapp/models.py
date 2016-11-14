from django.db import models

# Create your models here.
class Category(models.Model):
    category_name = models.CharField(max_length=200)

class Product(models.Model):
    product_name = models.CharField(max_length=200)
    cost = models.IntegerField(default=0)
    rating = models.IntegerField(default=0)
    stock = models.IntegerField(default=10)
