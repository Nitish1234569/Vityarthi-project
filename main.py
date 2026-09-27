from room_manager import RoomManager
from guest_manager import GuestManager
from booking_manager import BookingManager
from billing_manager import BillingManager
from reports import Reports

def main():
    room_manager = RoomManager()
    guest_manager = GuestManager()
    booking_manager = BookingManager()
    billing_manager = BillingManager()
    reports = Reports()

    while True:
        print("\n" + "=" * 50)
        print("             HOTEL MANAGEMENT SYSTEM")
        print("=" * 50)
        print("1. View Rooms")
        print("2. Add Guest")
        print("3. View Guests")
        print("4. Book Room")
        print("5. View Bookings")
        print("6. Check-In")
        print("7. Check-Out")
        print("8. Generate Bill")
        print("9. Hotel Report")
        print("10. Exit")
        print("=" * 50)

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            room_manager.display_rooms()

        elif choice == "2":
            guest_manager.add_guest()

        elif choice == "3":
            guest_manager.display_guests()

        elif choice == "4":
            booking_manager.book_room(guest_manager, room_manager)

        elif choice == "5":
            booking_manager.display_bookings()

        elif choice == "6":
            booking_manager.check_in()

        elif choice == "7":
            booking_manager.check_out(room_manager)

        elif choice == "8":
            billing_manager.generate_bill(booking_manager)

        elif choice == "9":
            reports.show_report(room_manager, guest_manager, booking_manager)

        elif choice == "10":
            print("Thank you for using the Hotel Management System!")
            break

        else:
            print("Invalid choice. Please enter a number from 1 to 10.")

if __name__ == "__main__":
    main()
