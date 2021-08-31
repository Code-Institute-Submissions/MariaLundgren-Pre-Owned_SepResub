from django.shortcuts import get_object_or_404
from .models import Favourites


def favourite_products(request):
    favourite_products = []
    if request.user.is_authenticated:
        favourite = get_object_or_404(Favourites, user=request.user)
        favourite_products = favourite.products.all()

    context = {
        "favourite_products": favourite_products,
    }

    return context
