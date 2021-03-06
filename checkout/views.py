from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .forms import OrderForm
from shopping_bag.context import shopping_bag_contents
from products.models import Product
from .models import Order, OrderLineItem
from profiles.models import UserProfile

import stripe


@login_required
def checkout(request):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    current_shopping_bag = shopping_bag_contents(request)
    total = current_shopping_bag['total']

    if request.method == 'POST':
        shopping_bag = request.session.get('shopping_bag', {})
        print("ADDED BY JO: SHOPPING BAG ON LINE 20 = ", shopping_bag)

        form_data = {
            'name': request.POST['name'],
            'email': request.POST['email'],
            'phone_number': request.POST['phone_number'],
            'street_address': request.POST['street_address'],
            'postcode': request.POST['postcode'],
            'town_or_city': request.POST['town_or_city'],
            'country': request.POST['country'],
        }

        order_form = OrderForm(form_data)
        if order_form.is_valid():
            order = order_form.save()
            order.total = total
            order.save()
            for item_id, item in shopping_bag.items():
                try:
                    product = Product.objects.get(id=item_id)
                    order_line_item = OrderLineItem(
                            order=order,
                            product=product,
                        )
                    order_line_item.save()
                except Product.DoesNotExist:
                    messages.errror(request, (
                        "One of the products in your bag wasn't \
                         found in our database.")
                    )
                    order.delete()

                    return redirect(reverse(shopping_bag))

            return redirect(reverse('checkout_success',
                            args=[order.order_number]))
        else:
            messages.error(request, 'There was an error with your form. \
                Please check your information.')
    else:
        shopping_bag = request.session.get('shopping_bag')
        if not shopping_bag:
            return redirect(reverse('products'))

        current_shopping_bag = shopping_bag_contents(request)
        total = current_shopping_bag['total']
        stripe_total = round(total * 100)
        stripe.api_key = stripe_secret_key
        intent = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency=settings.STRIPE_CURRENCY,
        )

        if request.user.is_authenticated:
            try:
                profile = UserProfile.objects.get(user=request.user)
                order_form = OrderForm(initial={
                    'name': profile.default_name,
                    'email': profile.user.email,
                    'phone_number': profile.default_phone_number,
                    'country': profile.default_country,
                    'postcode': profile.default_postcode,
                    'town_or_city': profile.default_town_or_city,
                    'street_address': profile.default_street_address,
                })
            except UserProfile.DoesNotExist:
                order_form = OrderForm()
        else:
            order_form = OrderForm()

    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
    }

    return render(request, template, context)


@login_required
def checkout_success(request, order_number):

    order = get_object_or_404(Order, order_number=order_number)

    profile = UserProfile.objects.get(user=request.user)
    order.user_profile = profile
    order.save()

    if 'shopping_bag' in request.session:
        del request.session['shopping_bag']

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
    }

    return render(request, template, context)
