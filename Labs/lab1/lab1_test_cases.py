import unittest
from lab1 import *

 # A few test cases.
class TestLab1(unittest.TestCase):


    #TEST_MAX_ITER
    def test_max_list_iter_1(self):
        """Test 1 for max_list_iter"""
        tlist = None
        with self.assertRaises(ValueError):  # used to check for exception
            max_list_iter(tlist)

    def test_max_list_iter_2(self):
        """Test 2 for max_list_iter"""
        self.assertEqual(max_list_iter([1,2,3]),3)

    def test_max_list_iter_3(self):
        """Test 3 for max_list_iter"""
        self.assertEqual(max_list_iter([-1,2,3,5,9,19,-24]),19)


    #TEST_REVERSE_REC
    def test_reverse_rec_1(self):
        """Test 1 for reverse_rec"""
        self.assertEqual(reverse_rec([1,2,3]),[3,2,1])

    def test_reverse_rec_2(self):
        """Test 2 for reverse_rec"""
        self.assertEqual(reverse_rec([2,2,9,4,5]),[5,4,9,2,2])
    
    def test_reverse_rec_3(self):
        """Test 3 for reverse_rec"""
        self.assertEqual(reverse_rec([1]),[1])

    def test_reverse_rec_4(self):
        """Test 4 for reverse_rec"""
        lst = []
        with self.assertRaises(ValueError):
            reverse_rec(lst)


    #TEST_BINARY_SEARCH
    def test_bin_search_1(self):
        """Test 1 for bin_search_rec"""
        list_val =[0,1,2,3,4,7,8,9,10]
        low = 0
        high = len(list_val)-1
        self.assertEqual(bin_search(4, 0, len(list_val)-1, list_val), 4 ) #bin_search(target,low,high,list)

    def test_bin_search_2(self):
        """Test 2 for bin_search_rec"""
        list_val =[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
        low = 0
        high = len(list_val)-1
        self.assertEqual(bin_search(20, 0, len(list_val)-1, list_val), 20 )

    def test_bin_search_3(self):
        """Test 3 for bin_search_rec"""
        list_val =[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
        low = 0
        high = len(list_val)-1
        self.assertEqual(bin_search(13, 0, len(list_val)-1, list_val), 13 )

    def test_bin_search_4(self):
        """Test 4 for bin_search_rec"""
        list_val =[0,1,2,3,4,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
        low = 0
        high = len(list_val)-1
        self.assertEqual(bin_search(30, 0, len(list_val)-1, list_val), None )

    def test_bin_search_5(self):
        """Test 5 for bin_search_rec"""
        list_val =[3,5,9,13,15,16,20,25,35]
        low = 0
        high = len(list_val)-1
        self.assertEqual(bin_search(5, 0, len(list_val)-1, list_val), 1 )


if __name__ == "__main__":
        unittest.main()

    
