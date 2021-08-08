from django.shortcuts import render, redirect, get_object_or_404
from products.models import Product


def shopping_bag(request):

    return render(request, 'shopping_bag/shopping_bag.html')


def add_to_shopping_bag(request, product_id):

    get_object_or_404(Product, pk=product_id)

    shopping_bag = request.session.get('shopping_bag', {})

    shopping_bag[product_id]

    request.session['shopping_bag'] = shopping_bag
    print(request.session["shopping_bag"])
    return redirect('products')
