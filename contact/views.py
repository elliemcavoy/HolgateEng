from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.conf import settings
from django.core.mail import send_mail
from django.template.loader import render_to_string
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


def contact_form_success(request, ref_number):

    contactform = get_object_or_404(Contact, ref_number=ref_number)
    
    def _send_confirmation_email(self, contactform):
        """Send the user a confirmation email"""
        customer_email = contactform.email
        subject = render_to_string(
            'contact/email/email_subject.txt',
            {'contactform': contactform})
        body = render_to_string(
            'contact/email/email_body.txt',
            {'contactform': contactform, 'contact_email': settings.DEFAULT_FROM_EMAIL})

        send_mail(
            subject,
            body,
            settings.DEFAULT_FROM_EMAIL,
            [customer_email]
        )
    template = 'contact/contactform_success.html'
    context = {
        'contactform': contactform,
    }
    return render(request, template, context)