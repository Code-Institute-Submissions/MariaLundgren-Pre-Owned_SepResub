from django.shortcuts import render, get_object_or_404
from .models import Product, Category


def products(request):

    products = Product.objects.all()
    categories = None
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            if sortkey == 'name':
                products = products.annotate(name=('name'))
            if sortkey == 'category':
                sortkey = 'category__name'
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)

        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

    context = {
        'products': products,
        'current_categories': categories,
    }

    return render(request, 'products/products.html', context)


def selected_product(request, product_id):

    is_favourites = False
    product = get_object_or_404(Product, pk=product_id)

    if product.favourites.filter(id=request.user.id).exists():
        is_favourites = True

    context = {
        'product': product,
        'is_favourites': is_favourites,
    }

    return render(request, 'products/selected_product.html', context)


def favourites(request, product_id):

    product = get_object_or_404(Product, pk=product_id)

    if product.favourites.filter(id=request.user.id).exists():
        product.favourites.remove(request.user)
    else:
        product.favourites.add(request.user)
    return render(request, 'products/selected_product.html')
