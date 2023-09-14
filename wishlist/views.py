from django.shortcuts import render, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect

from products.models import Product
from wishlist.models import WishlistItem


@login_required
def view_wishlist(request):
    """Displays the user's wishlist"""
    wishlist = WishlistItem.objects.filter(user=request.user)
    template = "wishlist/wishlist.html"
    context = {
        "wishlist": wishlist,
        "on_profile_page": True,
    }

    return render(request, template, context)


@login_required
def toggle_wishlist_item(request, item_id):
    """Add a specified product to the wishlist"""

    if request.method == "POST":
        product = get_object_or_404(Product, pk=item_id)
        product_id = request.POST.get("product-id")
        products = Product.objects.get(id=product_id)

        try:
            wishlist_item = WishlistItem.objects.get(
                user=request.user, product=products
            )
            if wishlist_item:
                messages.success(
                    request, f"Removed {product.name} from your wishlist"
                )
                wishlist_item.delete()
                return HttpResponseRedirect(
                    reverse("product_detail", args=product_id)
                )
        except:
            WishlistItem.objects.create(user=request.user, product=products)
            messages.success(request, f"Added {product.name} to your wishlist")
            return HttpResponseRedirect(reverse("view_wishlist"))


def remove_from_wishlist(request, item_id):
    if request.method == "POST":
        item_id = request.POST.get("item-id")
        WishlistItem.objects.filter(id=item_id).delete()
        return HttpResponseRedirect(reverse("view_wishlist"))
