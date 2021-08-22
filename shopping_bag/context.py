from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Product


def shopping_bag_contents(request):

    shopping_bag_items = []
    total = 0
    shopping_bag = request.session.get('shopping_bag', {})

    for item_id, item in shopping_bag.items():
        product = get_object_or_404(Product, pk=item_id)
        total += product.price
        shopping_bag_items.append({
            'item_id': item_id,
            'product': product,
        })

    context = {
        'shopping_bag_items': shopping_bag_items,
        'total': total,
    }

    return context
