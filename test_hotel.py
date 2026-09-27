import unittest
import os
import tempfile
import json

class TestHotelCalculations(unittest.TestCase):
    def test_room_charge(self):
        price = 2500
        nights = 3
        self.assertEqual(price * nights, 7500)

    def test_tax_calculation(self):
        subtotal = 5000
        tax = subtotal * 0.05
        self.assertEqual(tax, 250)

    def test_total_bill(self):
        room = 5000
        food = 1000
        tax = (room + food) * 0.05
        self.assertEqual(room + food + tax, 6300)

    def test_booking_status(self):
        booking = {"status": "Booked"}
        booking["status"] = "Checked-In"
        self.assertEqual(booking["status"], "Checked-In")

if __name__ == "__main__":
    unittest.main()
