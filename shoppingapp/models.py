from django.db import models

from shoppingsite.settings import IMAGES_FOLDER

# Create your models here.
class Category(models.Model):
    category_name = models.CharField(max_length=200)
    def __str__(self):
        return self.category_name
    class Meta:
        verbose_name_plural = "categories"

class Product(models.Model):
    category = models.ForeignKey(Category)
    product_name = models.CharField(max_length=200)
    price = models.IntegerField(default=0)
    rating = models.IntegerField(default=0)
    stock = models.IntegerField(default=10)
    thumbnail = models.FilePathField(path=IMAGES_FOLDER, recursive=True)
    def __str__(self):
        return self.product_name
