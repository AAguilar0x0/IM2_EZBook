from django.shortcuts import render
from django.views.generic import View

# Create your views here.


def home(request):
    return render(request, 'ezbook_client/home.html')


def about(request):
    return render(request, 'ezbook_client/about.html', {'title': 'about'})


def features(request):
    return render(request, 'ezbook_client/features.html', {'title': 'features'})


def signin(request):
    return render(request, 'ezbook_client/signin.html', {'title': 'signin'})


def register(request):
    return render(request, 'ezbook_client/register.html', {'title': 'register'})


def contact(request):
    return render(request, 'ezbook_client/contact.html', {'title': 'contact'})
