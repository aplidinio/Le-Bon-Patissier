from django.contrib import admin
from .models import ProductCategory, Product

# Register your models here.

class ProdAdminCategory(admin.ModelAdmin):

    readonly_fields = ("created", "updated")

class ProductAdmin(admin.ModelAdmin):

    readonly_fields = ("created", "updated")

admin.site.register(ProductCategory, ProdAdminCategory)
admin.site.register(Product, ProductAdmin)

