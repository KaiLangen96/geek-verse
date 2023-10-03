"""geek_verse URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from .views import handler400, handler403, handler404, handler500

urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/", include("allauth.urls")),
    path("", include("home.urls")),
    path("products/", include("products.urls")),
    path("cart/", include("cart.urls")),
    path("checkout/", include("checkout.urls")),
    path("profile/", include("profiles.urls")),
    path("wishlist/", include("wishlist.urls")),
    path("help_center/", include("help_center.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# The handlers are created based on the tutorial:
# Project - Boutique Ado > Code Refactoring > Adding a custom 404 page
handler400 = "geek_verse.views.handler400"  # noqa
handler403 = "geek_verse.views.handler403"  # noqa
handler404 = "geek_verse.views.handler404"  # noqa
handler500 = "geek_verse.views.handler500"  # noqa
