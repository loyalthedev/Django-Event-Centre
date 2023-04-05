from django.shortcuts import render
from django.http import HttpResponse
from .models import Venue


def home(request):
    venues = Venue.objects.all()
    return render(request, 'events/home.html', {'venues': venues})


def about(request):
    return render(request, 'events/about.html')


def contact(request):
    return render(request, 'events/contact.html')
