from django.shortcuts import render
from django.http import HttpResponse
from .models import Venue


def home(request):
    venues = Venue.objects.all().order_by('-id')
    return render(request, 'events/home.html', {'venues': venues})


def read_view(request, venue_id):
    venue = Venue.objects.get(id=venue_id)
    return render(request, 'events/read_view.html', {'venue': venue})


def about(request):
    return render(request, 'events/about.html')


def contact(request):
    return render(request, 'events/contact.html')
