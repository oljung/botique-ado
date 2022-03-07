"""
views for the boutique app
"""
from django.shortcuts import render
from .models import Product

# Create your views here.


def all_products(request):
    """ A view to show all product, with search and filter """

    products = Product.objects.all()

    context = {
        'products': products,
    }

    return render(request, "products.html", context)
