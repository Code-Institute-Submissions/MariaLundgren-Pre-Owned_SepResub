from django.shortcuts import render, redirect, get_object_or_404
from products.models import Product


def shopping_bag(request):

    return render(request, 'shopping_bag/shopping_bag.html')
