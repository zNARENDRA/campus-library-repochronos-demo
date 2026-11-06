import unittest
from library import calculate_fine

class FineTests(unittest.TestCase):
    def test_no_negative_fine(self):
        self.assertEqual(calculate_fine(-2), 0)

    def test_tiered_fine(self):
        self.assertEqual(calculate_fine(8), 17)

    def test_due_today_has_no_fine(self):
        self.assertEqual(calculate_fine(0), 0)

    def test_first_week_fines(self):
        self.assertEqual(calculate_fine(1), 2)
        self.assertEqual(calculate_fine(7), 14)

    def test_month_boundary(self):
        self.assertEqual(calculate_fine(30), 83)
        self.assertEqual(calculate_fine(31), 88)
