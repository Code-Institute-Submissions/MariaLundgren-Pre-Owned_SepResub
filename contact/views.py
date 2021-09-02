from django.shortcuts import render
from .forms import ContactForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages


@login_required
def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            messages.success(request, 'Thank you for your message!')
            contact = form.save(commit=False)
            contact.user = request.user
            contact.save()
    form = ContactForm()
    context = {'form': form}
    return render(request, 'contact/contact.html', context)
