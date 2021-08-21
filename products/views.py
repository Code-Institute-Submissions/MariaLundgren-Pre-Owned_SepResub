from django.shortcuts import render, get_object_or_404
from .models import Product


def products(request):

    products = Product.objects.all()

    context = {
        'products': products,
    }

    return render(request, 'products/products.html', context)


def selected_product(request, product_id):

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/selected_product.html', context)


def favourites(request, product_id):

    product = get_object_or_404(Product, pk=product_id)

    if product.favourites.filter(id=request.user.id).exists():
        product.favourites.remove(request.user)
    else:
        product.favourites.add(request.user)
    return render(request, 'favourites/favourites.html')
