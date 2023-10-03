from django.db import models
from django.contrib.auth.models import User

from products.models import Product


class WishlistItem(models.Model):
    """
    A wishlist item model to give users the ability to create
    a wishlist of items in the store.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
