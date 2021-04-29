from django.db import models

# Create your models here.

class ProductCategory(models.Model):
    name = models.CharField(max_length = 50)
    created = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now_add = True)

    class Meta:
        verbose_name = 'productCategory'
        verbose_name_plural = 'productCategories'

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length = 50)
    categories = models.ForeignKey(ProductCategory, on_delete = models.CASCADE)
    image = models.ImageField(upload_to = 'marketplace', null = True, blank = True)
    price = models.FloatField()
    price_by_unit = models.CharField(max_length = 20, null = True, blank = True)
    availability = models.BooleanField(default = True)
    created = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now_add = True)

    class Meta:
        verbose_name = 'product'
        verbose_name_plural = 'products'
