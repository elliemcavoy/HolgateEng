from django.shortcuts import render


def contact(request):
    """ View to render the index page """

    return render(request, 'contact/contact.html')
