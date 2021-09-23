import unittest
from location import *

class TestLab1(unittest.TestCase):

    def test_repr(self):
        loc = Location("SLO", 35.3, -120.7)
        self.assertEqual(repr(loc),"Location('SLO', 35.3, -120.7)")
    
    def test_eq(self):
        loc1 = Location("SLO", 35, -120)
        loc2 = Location("SLO", 35, -120)
        self.assertTrue(loc1 == loc2)
    def test_eq2(self):
        loc1 = Location("SLO", 25, -120)
        loc2 = Location("CHI", 78, -45)
        self.assertFalse(loc1 == loc2)

    def test_repr2(self):
        loc3 = Location("SEA", 67, -118)
        self.assertEqual(repr(loc3), "Location('SEA', 67, -118)")

if __name__ == "__main__":
        unittest.main()
