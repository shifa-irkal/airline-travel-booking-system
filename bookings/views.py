from datetime import date
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Booking

FLIGHTS = [
    {"id": 1, "airline": "IndiGo", "flight_number": "6E 204", "origin": "Bengaluru", "destination": "Delhi", "depart": "06:15", "arrive": "09:05", "duration": "2h 50m", "cabin": "Economy", "fare": 5200},
    {"id": 2, "airline": "Air India", "flight_number": "AI 804", "origin": "Bengaluru", "destination": "Delhi", "depart": "10:30", "arrive": "13:20", "duration": "2h 50m", "cabin": "Economy", "fare": 6100},
    {"id": 3, "airline": "Akasa Air", "flight_number": "QP 1351", "origin": "Bengaluru", "destination": "Mumbai", "depart": "08:00", "arrive": "09:45", "duration": "1h 45m", "cabin": "Economy", "fare": 3900},
    {"id": 4, "airline": "IndiGo", "flight_number": "6E 621", "origin": "Delhi", "destination": "Bengaluru", "depart": "17:10", "arrive": "20:05", "duration": "2h 55m", "cabin": "Economy", "fare": 5400},
    {"id": 5, "airline": "Air India", "flight_number": "AI 639", "origin": "Mumbai", "destination": "Bengaluru", "depart": "14:20", "arrive": "16:05", "duration": "1h 45m", "cabin": "Economy", "fare": 4200},
]

def home(request):
    origin = request.GET.get("origin", "Bengaluru")
    destination = request.GET.get("destination", "Delhi")
    travel_date = request.GET.get("travel_date", "")
    try:
        passengers = max(1, min(9, int(request.GET.get("passengers", 1))))
    except (TypeError, ValueError):
        passengers = 1

    results = [f for f in FLIGHTS if f["origin"].lower() == origin.lower()
               and f["destination"].lower() == destination.lower()]
    return render(request, "bookings/home.html", {
        "flights": results, "origin": origin, "destination": destination,
        "travel_date": travel_date, "passengers": passengers,
        "today": date.today().isoformat(),
    })

def book_flight(request, flight_id):
    flight = next((f for f in FLIGHTS if f["id"] == flight_id), None)
    if not flight:
        messages.error(request, "That flight could not be found.")
        return redirect("home")

    if request.method == "POST":
        try:
            passengers = max(1, min(9, int(request.POST.get("passengers", 1))))
        except (TypeError, ValueError):
            passengers = 1
        full_name = request.POST.get("full_name", "").strip()
        email = request.POST.get("email", "").strip()
        phone = request.POST.get("phone", "").strip()
        travel_date = request.POST.get("travel_date")
        if not all([full_name, email, phone, travel_date]):
            messages.error(request, "Please complete all passenger and travel details.")
        else:
            taxes = 350 * passengers
            total = (flight["fare"] * passengers) + taxes
            booking = Booking.objects.create(
                airline=flight["airline"], flight_number=flight["flight_number"],
                origin=flight["origin"], destination=flight["destination"],
                travel_date=travel_date, passengers=passengers,
                full_name=full_name, email=email, phone=phone,
                base_fare=flight["fare"] * passengers, taxes=taxes, total_price=total,
            )
            return redirect("confirmation", booking_id=booking.id)

    return render(request, "bookings/book.html", {
        "flight": flight, "today": date.today().isoformat(),
        "travel_date": request.GET.get("travel_date", ""),
        "passengers": request.GET.get("passengers", "1"),
    })

def confirmation(request, booking_id):
    booking = get_object_or_404(Booking, pk=booking_id)
    return render(request, "bookings/confirmation.html", {"booking": booking})
