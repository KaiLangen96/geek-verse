from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_wishlist, name='view_wishlist'),
    path('toggle/<item_id>/', views.toggle_wishlist_item, name='toggle_wishlist_item'),
    path('remove/<item_id>/', views.remove_from_wishlist, name='remove_from_wishlist'),
]
