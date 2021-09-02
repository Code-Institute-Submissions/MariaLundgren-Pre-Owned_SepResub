from django.shortcuts import get_object_or_404
from .models import Contact


def contact_form(request):
    contact_form = []
    if request.user.is_authenticated:
        contact = get_object_or_404(Contact, user=request.user)
        contact_form = contact.form.all()

    context = {
        "contact_form": contact_form,
    }

    return context
