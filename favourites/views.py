from django.shortcuts import render, get_object_or_404, redirect, reverse, HttpResponse

from .models import Favourites
from products.models import Product
from django.contrib.auth.models import User


def favourites(request):

    template = "favourites/favourites.html"

    return render(request, template)


def add_favourite(request, product_id):

    if request.method == "POST":
        redirect_url = request.POST.get('redirect_url')
        product = get_object_or_404(Product, pk=product_id)
        product = request.POST.get('product')
        user = request.user
        record = Favourites(product_id=product_id, user=user)
        record.save()
        return redirect(redirect_url)
    else:
        return redirect(reverse("products"))


def remove_favourite(request, product_id):
    if request.method == "POST":
        product = get_object_or_404(Product, pk=product_id)
        favourites = get_object_or_404(Favourites, user=request.UserProfile)
        if product in favourites.products.all():
            favourites.products.pop(product)
            return HttpResponse(status=200)
    else:
        return redirect(reverse("favourites"))
