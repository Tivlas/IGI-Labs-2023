# Generated by Django 4.2.1 on 2023-05-23 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travel', '0004_alter_client_date_of_birth_alter_trip_departure_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='trip',
            name='name',
            field=models.CharField(default='Trip', max_length=50),
        ),
    ]
