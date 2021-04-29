from django.shortcuts import render
from .cart import Cart
from MarketplaceApp.models import Product
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required


# Create your views here.

# @login_required(login_url="/templates/registration/login")

@login_required
def go_to_cart(request):

    return render(request, 'ShoppingCartApp/shoppingcart.html')

@login_required
def add_product(request, product_id):

    cart = Cart(request)
    product = Product.objects.get(id = product_id)
    cart.add(product = product)
    return redirect("marketplace")

@login_required
def delete_product(request, product_id):

    cart = Cart(request)
    product = Product.objects.get(id = product_id)
    cart.delete(product = product)
    return redirect("marketplace")

@login_required
def increment_product(request, product_id):

    cart = Cart(request)
    product = Product.objects.get(id = product_id)
    cart.add(product = product)
    return redirect("marketplace")

@login_required
def decrement_product(request, product_id):

    cart = Cart(request)
    product = Product.objects.get(id = product_id)
    cart.decrement(product = product)
    return redirect("marketplace")

@login_required
def clear_cart(request, product_id):

    cart = Cart(request)
    cart.clear_cart()
    return redirect("marketplace")

@login_required
def cart_detail(request):
    return render(request, 'marketplace')  # ojo



