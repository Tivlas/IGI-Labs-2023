from django.contrib import admin
from .models import SeasonClimateDescription, Country, Trip, Hotel

# Register your models here.


@admin.register(SeasonClimateDescription)
class SeasonClimateDescriptionAdmin(admin.ModelAdmin):
    list_display = ['season_name', 'climate_description']


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ['name']
    filter_horizontal = ['climate_descriptions']


@admin.register(Hotel)
class HotelAdmin(admin.ModelAdmin):
    list_display = ['name', 'stars', 'price_per_day', 'country']
    list_filter = ['stars', 'country']
