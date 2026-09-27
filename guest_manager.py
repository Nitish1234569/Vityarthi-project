from database import load_data, save_data
from validators import get_non_empty

class GuestManager:
    def __init__(self):
        self.filename = "guests.json"
        self.guests = load_data(self.filename)

    def save(self):
        save_data(self.filename, self.guests)

    def add_guest(self):
        print("\nADD GUEST")
        guest_id = "G" + str(len(self.guests) + 1).zfill(3)
        name = get_non_empty("Enter guest name: ")
        phone = get_non_empty("Enter phone number: ")
        email = input("Enter email (optional): ").strip()

        guest = {
            "guest_id": guest_id,
            "name": name,
            "phone": phone,
            "email": email
        }
        self.guests.append(guest)
        self.save()
        print(f"Guest registered successfully. Guest ID: {guest_id}")

    def find_guest(self, guest_id):
        for guest in self.guests:
            if guest["guest_id"].upper() == guest_id.upper():
                return guest
        return None

    def display_guests(self):
        print("\nGUEST DETAILS")
        print("-" * 80)
        if not self.guests:
            print("No guests registered.")
            return
        print(f"{'ID':<10}{'Name':<25}{'Phone':<18}{'Email':<25}")
        print("-" * 80)
        for guest in self.guests:
            print(f"{guest['guest_id']:<10}{guest['name']:<25}"
                  f"{guest['phone']:<18}{guest['email']:<25}")
