from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from products.models import Product


def shopping_bag(request):

    return render(request, 'shopping_bag/shopping_bag.html')


def add_to_shopping_bag(request, item_id):

    product = get_object_or_404(Product, pk=item_id)
    item = request.POST.get('item')
    redirect_url = request.POST.get('redirect_url')
    shopping_bag = request.session.get('shopping_bag', {})

    shopping_bag[item_id] = item

    request.session['shopping_bag'] = shopping_bag
    return redirect(redirect_url)


def remove_from_shopping_bag(request, item_id):

    try:
        shopping_bag = request.session.get('shopping_bag', {})
        shopping_bag.pop(item_id)

        request.session['shopping_bag'] = shopping_bag
        return HttpResponse(status=200)
    except Exception as e:
        return HttpResponse(status=500)
