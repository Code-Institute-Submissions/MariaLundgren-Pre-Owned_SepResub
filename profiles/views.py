from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required

from .models import UserProfile
from .forms import UserProfileForm
from django.contrib import messages

from checkout.models import Order
from contact.models import Contact

@login_required
def profile(request):

    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()

    form = UserProfileForm(instance=profile)
    orders = profile.orders.all()
    users_contact = Contact.objects.filter(user=request.user)

    template = 'profiles/profile.html'
    context = {
        'form': form,
        'orders': orders,
        'users_contact': users_contact,
    }

    return render(request, template, context)


def order_history(request, order_number):
    order = get_object_or_404(Order, order_number=order_number)

    messages.info(request, (
        f'This is a past confirmation for order number {order_number}.'
    ))

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
        'from_profile': True,
    }

    return render(request, template, context)
