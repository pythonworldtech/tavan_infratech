from django.shortcuts import render,redirect
from django.views import  View
from django.contrib.auth.models import User
from django.contrib import messages
import random
from .models import *

def homepage(request):
    all_services = Service.objects.all()
    data = {
        'all_services': all_services,
    }
    return render(request, 'index.html')



def about_us(request):
    data = {}
    return render(request, 'main_about.html',data)


def services(request):
    return render(request, 'main_services.html')


def project(request):
    return render(request, 'main_projects.html')

def achievements(request):
    return render(request, 'achievements.html')


class Contact(View):
    def get(self, request):
       return render(request, 'contact.html')

    def post(self, request):
        full_name = request.POST.get("full_name")
        email = request.POST.get("email")
        subject = request.POST.get("subject")
        message = request.POST.get("message")
        contact_id = random.randint(00000000,99999999)
        value = {
          'full_name' : full_name,
          'email':email,
          'subject':subject,
          'message':message
        }
        error_message = None
        save_data = Contact_us(
            contact_id=contact_id,
            full_name=full_name,
            email=email,
            subject=subject,
            message = message,
        )
        save_data.save()
        return render(request, 'contact.html', {'error':error_message,'value':value})
        
