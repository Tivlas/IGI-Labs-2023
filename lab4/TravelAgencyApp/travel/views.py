\
from django.shortcuts import render, redirect, get_object_or_404
from .models import Trip, Country
from django.http import HttpResponseRedirect
from django.http import HttpResponseNotFound
from django.core.exceptions import PermissionDenied

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
    if not request.user.is_staff:
        raise PermissionDenied("Permission denied!")

    try:
        trip = Trip.objects.get(id=id)
        trip.delete()
        return HttpResponseRedirect("/")
    except trip.DoesNotExist:
        return HttpResponseNotFound("<h2>trip does not exist</h2>")
