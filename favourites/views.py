from django.shortcuts import render, get_object_or_404, redirect, reverse, HttpResponse

from .models import Favourites
from products.models import Product
from django.contrib.auth.decorators import login_required
from django.contrib import messages


@login_required
def favourites(request):

    favourites = None
    try:
        favourites = Favourites.objects.filter(user=request.user)
    except Favourites.DoesNotExist:
        pass

    context = {
        'favourites': favourites,
    }

    template = "favourites/favourites.html"

    return render(request, template, context)


@login_required
def add_favourite(request, product_id):

    if request.method == "POST":
        redirect_url = request.POST.get('redirect_url')
        product = get_object_or_404(Product, pk=product_id)
        product = request.POST.get('product')
        user = request.user
        record = Favourites(product_id=product_id, user=user)
        record.save()
        messages.success(request, 'Added product to your favorites')
        return redirect(redirect_url)
    else:
        return redirect(reverse("products"))


def remove_favourite(request, product_id):
    if request.method == "POST":
        product = get_object_or_404(Product, pk=product_id)
        favourites = get_object_or_404(Favourites, product=product,
                                       user=request.user)
        favourites.delete()
        messages.success(request, 'Removed product to your favorites')
        return HttpResponse(status=200)
    else:
        return redirect(reverse("favourites"))
