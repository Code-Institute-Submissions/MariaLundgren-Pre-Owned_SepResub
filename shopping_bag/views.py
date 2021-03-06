from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from products.models import Product
from django.contrib import messages


def shopping_bag(request):

    return render(request, 'shopping_bag/shopping_bag.html')


def add_to_shopping_bag(request, item_id):

    product = get_object_or_404(Product, pk=item_id)
    redirect_url = request.POST.get('redirect_url')
    shopping_bag = request.session.get('shopping_bag', {})

    item = request.POST.get('item')
    shopping_bag[item_id] = item
    messages.success(request, f'Added {product.name} to your bag')

    request.session['shopping_bag'] = shopping_bag
    return redirect(redirect_url)


def remove_from_shopping_bag(request, item_id):

    try:
        product = get_object_or_404(Product, pk=item_id)
        shopping_bag = request.session.get('shopping_bag', {})
        shopping_bag.pop(item_id)
        messages.success(request, f'Removed {product.name} from your bag')

        request.session['shopping_bag'] = shopping_bag
        return HttpResponse(status=200)
    except Exception as e:
        messages.error(request, f'Error removing items: {e}')
        return HttpResponse(status=500)
