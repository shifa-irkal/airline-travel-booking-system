from django.db import models

class Booking(models.Model):
    airline = models.CharField(max_length=100)
    flight_number = models.CharField(max_length=20)
    origin = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    travel_date = models.DateField()
    passengers = models.PositiveIntegerField(default=1)
    full_name = models.CharField(max_length=120)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    base_fare = models.PositiveIntegerField()
    taxes = models.PositiveIntegerField()
    total_price = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.full_name} - {self.flight_number}"
