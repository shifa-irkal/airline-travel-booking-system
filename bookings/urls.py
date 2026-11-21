from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("book/<int:flight_id>/", views.book_flight, name="book_flight"),
    path("confirmation/<int:booking_id>/", views.confirmation, name="confirmation"),
]
