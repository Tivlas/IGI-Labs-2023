from django.db import models
from travel.models import Trip
from login.models import MyUser


class Order(models.Model):
    client = models.ForeignKey(MyUser, on_delete=models.CASCADE, null=True)
    creation_date = models.DateTimeField(auto_now_add=True)
    trips = models.ManyToManyField(Trip, related_name='orders')

    def __str__(self):
        return f"Order {self.id}, made on {self.creation_date}."
