from validators import get_non_empty, get_positive_float

class BillingManager:
    def generate_bill(self, booking_manager):
        print("\nGENERATE BILL")
        booking_id = get_non_empty("Enter booking ID: ").upper()
        booking = booking_manager.find_booking(booking_id)

        if not booking:
            print("Booking not found.")
            return

        room_charge = booking["price_per_night"] * booking["nights"]
        food_charge = get_positive_float("Enter food/service charges (₹): ")
        tax = (room_charge + food_charge) * 0.05
        total = room_charge + food_charge + tax

        print("\n" + "=" * 45)
        print("                 HOTEL BILL")
        print("=" * 45)
        print(f"Booking ID       : {booking['booking_id']}")
        print(f"Guest Name       : {booking['guest_name']}")
        print(f"Room Number      : {booking['room_no']}")
        print(f"Room Type        : {booking['room_type']}")
        print(f"Number of Nights : {booking['nights']}")
        print("-" * 45)
        print(f"Room Charges     : ₹{room_charge:.2f}")
        print(f"Food/Services    : ₹{food_charge:.2f}")
        print(f"Tax (5%)         : ₹{tax:.2f}")
        print("-" * 45)
        print(f"TOTAL AMOUNT     : ₹{total:.2f}")
        print("=" * 45)
