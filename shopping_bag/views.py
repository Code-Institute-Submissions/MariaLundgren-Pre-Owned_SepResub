from django.shortcuts import render, redirect, get_object_or_404
from products.models import Product


def shopping_bag(request):

    return render(request, 'shopping_bag/shopping_bag.html')


def add_to_shopping_bag(request, item_id):

    product = get_object_or_404(Product, pk=item_id)
    redirect_url = request.POST.get('redirect_url')
    shopping_bag = request.session.get('shopping_bag', {})

    bag[item_id]

    request.session['shopping_bag'] = shopping_bag
    return redirect(redirect_url)
