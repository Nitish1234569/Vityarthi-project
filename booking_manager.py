from database import load_data, save_data
from validators import get_non_empty, get_positive_int
from datetime import datetime

class BookingManager:
    def __init__(self):
        self.filename = "bookings.json"
        self.bookings = load_data(self.filename)

    def save(self):
        save_data(self.filename, self.bookings)

    def book_room(self, guest_manager, room_manager):
        print("\nBOOK A ROOM")
        available = room_manager.available_rooms()
        if not available:
            print("Sorry, no rooms are currently available.")
            return

        guest_id = get_non_empty("Enter guest ID: ").upper()
        guest = guest_manager.find_guest(guest_id)
        if not guest:
            print("Guest not found. Register the guest first.")
            return

        print("\nAvailable Rooms:")
        for room in available:
            print(f"Room {room['room_no']} - {room['type']} - ₹{room['price']}/night")

        room_no = get_positive_int("Enter room number: ")
        room = room_manager.find_room(room_no)

        if not room:
            print("Room does not exist.")
            return
        if room["status"] != "Available":
            print("Room is not available.")
            return

        nights = get_positive_int("Enter number of nights: ")
        booking_id = "B" + str(len(self.bookings) + 1).zfill(3)

        booking = {
            "booking_id": booking_id,
            "guest_id": guest_id,
            "guest_name": guest["name"],
            "room_no": room_no,
            "room_type": room["type"],
            "price_per_night": room["price"],
            "nights": nights,
            "status": "Booked",
            "booking_date": datetime.now().strftime("%Y-%m-%d")
        }

        self.bookings.append(booking)
        room_manager.set_status(room_no, "Booked")
        self.save()
        print(f"Booking successful. Booking ID: {booking_id}")

    def display_bookings(self):
        print("\nBOOKING DETAILS")
        print("-" * 110)
        if not self.bookings:
            print("No bookings found.")
            return
        print(f"{'ID':<8}{'Guest':<20}{'Room':<8}{'Nights':<10}"
              f"{'Amount':<15}{'Status':<15}{'Date':<12}")
        print("-" * 110)
        for b in self.bookings:
            amount = b["price_per_night"] * b["nights"]
            print(f"{b['booking_id']:<8}{b['guest_name']:<20}{b['room_no']:<8}"
                  f"{b['nights']:<10}₹{amount:<14}{b['status']:<15}{b['booking_date']:<12}")

    def find_booking(self, booking_id):
        for booking in self.bookings:
            if booking["booking_id"].upper() == booking_id.upper():
                return booking
        return None

    def check_in(self):
        booking_id = get_non_empty("Enter booking ID for check-in: ").upper()
        booking = self.find_booking(booking_id)
        if not booking:
            print("Booking not found.")
            return
        if booking["status"] != "Booked":
            print(f"Cannot check in. Current status: {booking['status']}")
            return
        booking["status"] = "Checked-In"
        self.save()
        print("Guest checked in successfully.")

    def check_out(self, room_manager):
        booking_id = get_non_empty("Enter booking ID for check-out: ").upper()
        booking = self.find_booking(booking_id)
        if not booking:
            print("Booking not found.")
            return
        if booking["status"] != "Checked-In":
            print("Guest must be checked in before checkout.")
            return
        booking["status"] = "Checked-Out"
        room_manager.set_status(booking["room_no"], "Available")
        self.save()
        print("Guest checked out successfully.")
