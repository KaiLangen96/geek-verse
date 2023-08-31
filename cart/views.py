from django.shortcuts import render


def view_cart(request):
    """ A view to render the shopping cart with its items """

    return render(request, 'cart/cart.html')
