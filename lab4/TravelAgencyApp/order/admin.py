from django.contrib import admin
from .models import Order
from travel.models import Trip


class TripInline(admin.TabularInline):
    model = Trip
    extra = 0


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['client', 'creation_date']
    inlines = [TripInline]
    list_filter = ['creation_date', 'client']
