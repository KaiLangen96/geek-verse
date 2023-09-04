from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    cart = request.session.get('cart', {})
    if not cart:
        messages.error(request, "There's nothing in your cart.")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51Ng1uHKabJkYf3n7SMp3m9MnHQq6Menu4l3U15q2JZsm5oHr7MQkjML3XZvcc5uyjDEdxactxlcAcD6jXAwdSvCo000DTT0NqL',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)
