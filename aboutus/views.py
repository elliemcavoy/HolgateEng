from django.shortcuts import render


def about_us(request):
    """ View to render the index page """

    return render(request, 'about_us/about_us.html')
