from django.shortcuts import render
from .forms import ContactForm


def contact(request):
    if request.method == 'POST':
        form =ContactForm(request.POST)
        contact = form.save(commit=False)
        contact.user = request.user
        contact.save
        if form.is_valid():
            form.save()
    form = ContactForm()
    context = {'form': form}
    return render(request, 'contact/contact.html', context)


def view_conversation(request, user):

    contact = None
    user = request.session['user']
    contact = contact.objects.filter(user=request.user)

    context = {
        'contact': contact,
    }
    return render(request, context)
