"""
views for the boutique app
"""
from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from django.db.models import Q
from .models import Product

# Create your views here.


def all_products(request):
    """ A view to show the product details of a selected product """

    products = Product.objects.all()
    query = None

    if request.GET:
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria")
                return redirect(reverse('products'))
            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

    context = {
        'products': products,
        'search_term': query,
    }

    return render(request, "products.html", context)


def product_detail(request, product_id):
    """ A view to show all product, with search and filter """

    product = get_object_or_404(Product, id=product_id)

    context = {
        'product': product,
    }

    return render(request, "product_detail.html", context)
