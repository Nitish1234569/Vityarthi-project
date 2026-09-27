from database import load_data, save_data

class RoomManager:
    def __init__(self):
        self.filename = "rooms.json"
        self.rooms = load_data(self.filename)
        if not self.rooms:
            self.rooms = [
                {"room_no": 101, "type": "Single", "price": 1500, "status": "Available"},
                {"room_no": 102, "type": "Single", "price": 1500, "status": "Available"},
                {"room_no": 201, "type": "Double", "price": 2500, "status": "Available"},
                {"room_no": 202, "type": "Double", "price": 2500, "status": "Available"},
                {"room_no": 301, "type": "Deluxe", "price": 4000, "status": "Available"},
                {"room_no": 302, "type": "Deluxe", "price": 4000, "status": "Available"}
            ]
            self.save()

    def save(self):
        save_data(self.filename, self.rooms)

    def find_room(self, room_no):
        for room in self.rooms:
            if room["room_no"] == room_no:
                return room
        return None

    def display_rooms(self):
        print("\nROOM DETAILS")
        print("-" * 65)
        print(f"{'Room':<10}{'Type':<15}{'Price/Night':<15}{'Status':<15}")
        print("-" * 65)
        for room in self.rooms:
            print(f"{room['room_no']:<10}{room['type']:<15}"
                  f"₹{room['price']:<14}{room['status']:<15}")
        print("-" * 65)

    def available_rooms(self):
        return [r for r in self.rooms if r["status"] == "Available"]

    def set_status(self, room_no, status):
        room = self.find_room(room_no)
        if room:
            room["status"] = status
            self.save()
            return True
        return False
