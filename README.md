# SkyWay Airline Travel Booking (Django)

A beginner-friendly airline booking demo built with HTML, CSS, Django and SQLite.

## Features
- Home page with flight search
- Origin, destination, travel date and passenger count
- Sample airline flight options with airline name, flight number, timings, duration and cabin
- Fare updates automatically when passenger count changes
- Booking form with passenger details
- Booking confirmation page
- SQLite database stores bookings
- Responsive layout

## Run on Windows (VS Code terminal)

1. Extract the ZIP file.
2. Open the extracted `airline_travel_booking` folder in VS Code.
3. Open Terminal > New Terminal.
4. Create a virtual environment:
   `py -m venv venv`
5. Activate it:
   `venv\Scripts\activate`
6. Install Django:
   `pip install -r requirements.txt`
7. Create the database:
   `py manage.py migrate`
8. Start the website:
   `py manage.py runserver`
9. Open the URL shown in the terminal, usually `http://127.0.0.1:8000/`.

## Notes
- This is an educational demo. Flight names, schedules and fares are sample data, not live airline inventory.
- The displayed total is base fare × number of passengers. Taxes are shown separately and calculated per passenger.
