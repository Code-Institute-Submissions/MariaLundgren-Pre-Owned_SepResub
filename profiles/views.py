from django.shortcuts import render


def profile(request):
    """ A view that renders the bag contents page """

    return render(request, 'profiles/profile.html')
