from django.contrib import admin
from .models import Booking

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ("full_name", "flight_number", "origin", "destination", "travel_date", "passengers", "total_price")
    search_fields = ("full_name", "email", "flight_number")
    list_filter = ("travel_date", "airline")
