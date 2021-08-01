from django.shortcuts import render

def products(request):

    return render(request, 'products/products.html')


def selected_product(request):

    return render(request, 'products/selected_product.html')
