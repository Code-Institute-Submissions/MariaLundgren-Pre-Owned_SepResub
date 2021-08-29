from django.shortcuts import render, get_object_or_404, redirect, reverse, HttpResponse

from .models import Favourites
from products.models import Product


def favourites(request):

    template = "favourites/favourites.html"

    return render(request, template)


def add_favourite(request, product_id):

    if request.method == "POST":
        product = get_object_or_404(Product, pk=product_id)
        favourites = get_object_or_404(favourites, user=request.user)
        if product not in favourites.products.all():
            favourites.products.add(product)
            return HttpResponse(status=200)
    else:
        return redirect(reverse("products"))


def remove_favourite(request, product_id):
    if request.method == "POST":
        product = get_object_or_404(Product, pk=product_id)
        favourites = get_object_or_404(favourites, user=request.user)
        if product in favourites.products.all():
            favourites.products.pop(product)
            return HttpResponse(status=200)
    else:
        return redirect(reverse("favourites"))
