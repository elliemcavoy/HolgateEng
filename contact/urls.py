from django.contrib import admin
from django.urls import path 
from . import views

urlpatterns = [
    path('', views.contact, name='contact'),
    path('success/<ref_number>', views.contact_form_success, name='contact_form_success'),
]