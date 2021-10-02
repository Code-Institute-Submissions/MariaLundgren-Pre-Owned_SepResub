from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', include('home.urls')),
    path('profile/', include('profiles.urls')),
    path('products/', include('products.urls')),
    path('shopping_bag/', include('shopping_bag.urls')),
    path('checkout/', include('checkout.urls')),
    path('favourites/', include('favourites.urls')),
    path('contact/', include('contact.urls')),
]
