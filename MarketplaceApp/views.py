from django.shortcuts import render
from .models import Product

# Create your views here.

def marketplace(request):
    
    products = Product.objects.all()
    return render(request, "MarketplaceApp/marketplace.html", {'products': products})
