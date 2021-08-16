from django.shortcuts import render, get_object_or_404
from products.models import Product


def favourites(request, product_id):

    product = get_object_or_404(Product, pk=product_id)

    if product.favourites.filter(id=request.user.id).exists():
        product.favourites.remove(request.user)
    else:
        product.favourites.add(request.user)
    return render(request, 'favourites/favourites.html')


def favourite_list(request):
    user = request.user

    favourites = user.favourites.all()

    context = {
        'favourites': favourites,
    }

    return render(request, 'favourites/favourite_list.html', context)
