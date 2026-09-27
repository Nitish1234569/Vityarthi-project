# Hotel Management System

A beginner-friendly Python project for managing hotel rooms, guests, bookings,
check-in/check-out, billing, and basic reports.

## Features

- View room details and availability
- Register guests
- View guest records
- Book available rooms
- Check-in and check-out guests
- Generate bills with 5% tax
- View hotel statistics and room revenue
- JSON-based local data storage
- Input validation and error handling
- Unit tests for core calculations

## Technologies Used

- Python 3
- JSON
- Object-Oriented Programming
- File Handling
- unittest

## Project Structure

```text
Hotel-Management-System/
├── main.py
├── room_manager.py
├── guest_manager.py
├── booking_manager.py
├── billing_manager.py
├── database.py
├── validators.py
├── reports.py
├── test_hotel.py
├── data/
│   ├── rooms.json
│   ├── guests.json
│   └── bookings.json
├── README.md
└── statement.md
```

## How to Run

1. Install Python 3.
2. Open a terminal in the project folder.
3. Run:

```bash
python main.py
```

## How to Test

Run:

```bash
python -m unittest test_hotel.py
```

## Workflow

Guest Registration -> Room Selection -> Booking -> Check-In ->
Stay -> Billing -> Check-Out -> Room Becomes Available

## Future Enhancements

- Graphical user interface
- Login and role-based access
- SQLite/MySQL database
- Online booking
- Email/SMS confirmation
- Advanced revenue analytics
