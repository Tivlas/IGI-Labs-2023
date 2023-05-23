\
from django.shortcuts import render, redirect, get_object_or_404
from .models import Trip, Country


def list_trips(request, trip_country_name=None):
    trips = Trip.objects.all()
    country = None
    if trip_country_name:
        country = get_object_or_404(Country, name=trip_country_name)
        trips = trips.filter(country=country)

    countries = Country.objects.all()
    return render(request, 'trips/list_trips.html', {'trips': trips, 'countries': countries, 'country': country})

def trip_details(request,id):
    trip = get_object_or_404(Trip,id=id)
    return render(request,'trips/trip_details.html',{'trip':trip})

def edit_trip(request,id):
    pass

def delete_trip(request,id):
    pass
