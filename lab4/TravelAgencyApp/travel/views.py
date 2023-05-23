\
from django.shortcuts import render, redirect, get_object_or_404
from .models import Trip, Country
from django.http import HttpResponseRedirect
from django.http import HttpResponseNotFound
from django.core.exceptions import PermissionDenied
from .forms import TripForm

def list_trips(request, trip_country_name=None):
    trips = Trip.objects.all()
    country = None
    sort = request.GET.get('sort')
    min_cost = request.GET.get('min_cost')
    max_cost = request.GET.get('max_cost')
    min_stars = request.GET.get('min_stars')
    max_stars = request.GET.get('max_stars')

    if trip_country_name:
        country = get_object_or_404(Country, name=trip_country_name)
        trips = trips.filter(country=country)

    if min_cost and max_cost:
        trips = trips.filter(total_cost__gte=min_cost, total_cost__lte=max_cost)

    if min_stars and max_stars:
        trips = trips.filter(chosen_hotel__stars__gte=min_stars, chosen_hotel__stars__lte=max_stars)

    if sort == 'ascending':
        trips = trips.order_by('total_cost')
    elif sort == 'descending':
        trips = trips.order_by('-total_cost')

    countries = Country.objects.all()
    return render(request, 'trips/list_trips.html', {'trips': trips, 'countries': countries, 'country': country})

def trip_details(request,id):
    trip = get_object_or_404(Trip,id=id)
    return render(request,'trips/trip_details.html',{'trip':trip})

def edit_trip(request,id):
    trip = None
    try:
        trip = get_object_or_404(Trip,id=id)
    except:
        return HttpResponseNotFound("<h2>No such trip :(</h2>")
    
    if request.method == 'POST':
        form = TripForm(request.POST, instance=trip)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = TripForm(instance=trip)

    return render(request, 'trips/edit_trip.html', {'form': form, 'trip': trip})

def delete_trip(request,id):
    if not request.user.is_staff:
        raise PermissionDenied("Permission denied!")
    
    try:
        trip = get_object_or_404(Trip,id=id)
        trip.delete()
        return redirect("/")
    except:
        return HttpResponseNotFound("<h2>No such trip :(</h2>")
