"""
views for the boutique app
"""
from django.shortcuts import render, get_object_or_404
from .models import Product

# Create your views here.


def all_products(request):
    """ A view to show the product details of a selected product """

    products = Product.objects.all()

    context = {
        'products': products,
    }

    return render(request, "products.html", context)


def product_detail(request, product_id):
    """ A view to show all product, with search and filter """

    product = get_object_or_404(Product, id=product_id)

    context = {
        'product': product,
    }

    return render(request, "product_detail.html", context)
