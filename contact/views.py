from django.shortcuts import render
from django.contrib import messages
from django.conf import settings
from .models import Contact
from .forms import ContactForm


def contact(request):
    """ View to render the index page """
    if request.method == 'POST':
        form_data = {
            'full_name': request.POST['full_name'],
            'email': request.POST['email'],
            'phone_number': request.POST['phone_number'],
            'request': request.POST['request'],
        }
        contact_form = ContactForm(form_data)
        if contact_form.is_valid():
            contactus = contact_form.save(commit=False)
            contactus.save()
        else:
            messages.error(request, 'There was an error with your form. \
                Please double check your information.')
    else:
        contact_form = ContactForm()

    template = 'contact/contact.html'
    context = {
        'contact_form': contact_form,
    }
    return render(request, template, context)
