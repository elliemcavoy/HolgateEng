from django.contrib import admin
from .models import Contact


class ContactAdmin(admin.ModelAdmin):
    
    list_display = ('full_name', 'email', 'phone_number',
                    'request',)

admin.site.register(Contact)