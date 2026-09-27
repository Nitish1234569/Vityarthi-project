class Reports:
    def show_report(self, room_manager, guest_manager, booking_manager):
        total_rooms = len(room_manager.rooms)
        available = len(room_manager.available_rooms())
        occupied = total_rooms - available
        guests = len(guest_manager.guests)
        bookings = len(booking_manager.bookings)

        revenue = 0
        for booking in booking_manager.bookings:
            revenue += booking["price_per_night"] * booking["nights"]

        print("\n" + "=" * 45)
        print("              HOTEL REPORT")
        print("=" * 45)
        print(f"Total rooms       : {total_rooms}")
        print(f"Available rooms   : {available}")
        print(f"Occupied rooms    : {occupied}")
        print(f"Registered guests : {guests}")
        print(f"Total bookings    : {bookings}")
        print(f"Room revenue      : ₹{revenue:.2f}")
        print("=" * 45)
