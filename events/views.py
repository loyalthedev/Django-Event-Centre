from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request, 'events/home.html')


def about(request):
    return render(request, 'events/about.html')


def contact(request):
    return render(request, 'events/contact.html')
