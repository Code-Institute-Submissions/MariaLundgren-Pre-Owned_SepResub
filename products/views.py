from django.shortcuts import render, get_object_or_404
from .models import Product


def products(request):

    products = Product.objects.all()

    context = {
        'products': products,
    }

    return render(request, 'products/products.html', context)


def selected_product(request, product_id):

    product = get_object_or_404(Product)

    context = {
        'product': product,
    }

    return render(request, 'products/selected_product.html', context)
