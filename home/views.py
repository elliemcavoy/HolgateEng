from django.shortcuts import render


def index(request):
    """ View to render the index page """

    return render(request, 'home/index.html')
