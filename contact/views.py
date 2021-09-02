from django.shortcuts import render
from .forms import ContactForm


def contact(request):
    if request.method == 'POST':
        form =ContactForm(request.POST)
        if form.is_valid():
            contact = form.save(commit=False)
            contact.user = request.user
            contact.save()
    form = ContactForm()
    context = {'form': form}
    return render(request, 'contact/contact.html', context)

