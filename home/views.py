from django.shortcuts import render
from products.models import Product


def index(request):
    """ A view to return the index page """
    products = Product.objects.filter(category__name="new_arrivals")
    context = {
        'products': products,
    }
    print(products)
    return render(request, 'home/index.html', context)
