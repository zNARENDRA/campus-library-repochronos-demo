import unittest
from library import calculate_fine

class FineTests(unittest.TestCase):
    def test_no_negative_fine(self):
        self.assertEqual(calculate_fine(-2), 0)

    def test_tiered_fine(self):
        self.assertEqual(calculate_fine(8), 17)
