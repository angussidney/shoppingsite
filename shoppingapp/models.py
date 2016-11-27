from django.db import models
import django.utils

from shoppingsite.settings import IMAGES_FOLDER

# Create your models here.
class Category(models.Model):
    category_name = models.CharField(max_length=200)
    description = models.TextField()
    def __str__(self):
        return self.category_name
    class Meta:
        verbose_name_plural = "categories"

class Product(models.Model):
    category = models.ForeignKey(Category)
    product_name = models.CharField(max_length=200)
    thumbnail = models.FilePathField(path=IMAGES_FOLDER, recursive=True)
    price = models.DecimalField(default=0.0, decimal_places=2, max_digits=3)
    rating = models.FloatField(default=2.5)
    stock = models.IntegerField(default=10)
    date_added = models.DateTimeField('date added', default=django.utils.timezone.now)
    special = models.DecimalField(default=0.0, decimal_places=2, max_digits=3)
    ingredients = models.TextField(default="Insert ingredients here")
    def __str__(self):
        return self.product_name
