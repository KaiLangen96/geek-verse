from django.shortcuts import render
from products.models import Product


def index(request):
    """ A view to return the index page """
    products = Product.objects.filter(category__name="new_arrivals")[:6]
    context = {
        'products': products,
    }
    return render(request, 'home/index.html', context)
