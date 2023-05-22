from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from datetime import date, timedelta


class Client(models.Model):
    first_name = models.CharField(max_length=255, help_text="Enter first name")
    last_name = models.CharField(max_length=255, help_text="Enter last name")
    email = models.EmailField(unique=True, help_text='something@gmail.com')
    phone_number = models.CharField(
        max_length=20, help_text='+375 (29) 123-45-67')
    date_of_birth = models.DateField(validators=[MinValueValidator(
        limit_value=date.today() - timedelta(days=18*365))])

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class SeasonClimateDescription(models.Model):
    alias = models.CharField(max_length=50, null=True)
    season_name = models.CharField(max_length=6, choices=(('summer', 'summer'), ('winter', 'winter'),
                                                          ('spring', 'spring'), ('autumn', 'autumn')), default='summer')
    climate_description = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.season_name


class Country(models.Model):
    name = models.CharField(max_length=50)
    climate_descriptions = models.ManyToManyField(
        SeasonClimateDescription, related_name='countries')

    def __str__(self) -> str:
        return self.name


class Hotel(models.Model):
    name = models.CharField(max_length=50)
    stars = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)])
    price_per_day = models.DecimalField(
        default=0.0, max_digits=10, decimal_places=2)
    country = models.ForeignKey(
        Country, related_name='hotels', on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.name}"


class Trip(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    duration = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(4)])
    chosen_hotel = models.ForeignKey(
        Hotel, related_name='trips', on_delete=models.CASCADE)
    departure_date = models.DateField()
    total_cost = models.DecimalField(
        default=0.0, max_digits=10, decimal_places=2)
