from django.shortcuts import (
    render, reverse, get_object_or_404)
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect

from products.models import Product
from wishlist.models import WishlistItem


@login_required
def view_wishlist(request):
    """ Displays the user's wishlist """
    wishlist = WishlistItem.objects.filter(user=request.user)
    template = 'wishlist/wishlist.html'
    context = {
        'wishlist': wishlist,
        'on_profile_page': True,
    }

    return render(request, template, context)
