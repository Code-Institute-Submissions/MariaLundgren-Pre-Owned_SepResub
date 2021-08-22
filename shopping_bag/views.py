from django.shortcuts import render, redirect, get_object_or_404
from products.models import Product


def shopping_bag(request):

    return render(request, 'shopping_bag/shopping_bag.html')


def add_to_shopping_bag(request, item_id):

    product = get_object_or_404(Product, pk=item_id)
    item = int(request.POST.get('item'))
    redirect_url = request.POST.get('redirect_url')
    shopping_bag = request.session.get('shopping_bag', {})

    shopping_bag[item_id] = item

    request.session['shopping_bag'] = shopping_bag
    return redirect(redirect_url)

