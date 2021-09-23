import unittest
from ordered_list import *

class TestLab4(unittest.TestCase):

    def test_simple(self):
        t_list = OrderedList()
        t_list.add(10)
        self.assertEqual(t_list.python_list(), [10])
        self.assertEqual(t_list.size(), 1)
        self.assertEqual(t_list.index(10), 0)
        self.assertTrue(t_list.search(10))
        self.assertFalse(t_list.is_empty())
        self.assertEqual(t_list.python_list_reversed(), [10])
        self.assertTrue(t_list.remove(10))
        t_list.add(10)
        self.assertEqual(t_list.pop(0), 10)

    def test_1(self):
        t_list = OrderedList()
        self.assertTrue(t_list.is_empty())
        t_list.add(10)
        self.assertFalse(t_list.is_empty())
        self.assertEqual(t_list.size(), 1)
        t_list.add(10)
        self.assertEqual(t_list.size(), 1)
        t_list.add(11)
        self.assertEqual(t_list.size(), 2)
        t_list.add(12)
        t_list.add(4)
        t_list.add(7)
        self.assertEqual(t_list.python_list(),[4,7,10,11,12])
        self.assertEqual(t_list.python_list_reversed(),[12,11,10,7,4])
        self.assertEqual(t_list.pop(2),10)
        self.assertFalse(t_list.remove(24))
        self.assertFalse(t_list.search(10))
        self.assertTrue(t_list.search(7))
        t_list.add(56)
        t_list.add(39)
        self.assertFalse(t_list.is_empty())
        self.assertEqual(t_list.python_list(),[4,7,11,12,39,56])
        self.assertEqual(t_list.index(4),0)
        self.assertEqual(t_list.index(56),5)
        self.assertEqual(t_list.index(12),3)
        self.assertEqual(t_list.index(578),None)
   
    def test_2(self):
        temp = OrderedList()
        self.assertFalse(temp.remove(0))
        with self.assertRaises(IndexError): temp.pop(0)
        with self.assertRaises(IndexError): temp.pop(-1)
        temp.add(5)
        temp.add(-5)
        self.assertEqual(temp.pop(0),-5)
        self.assertEqual(temp.pop(0),5)
        self.assertTrue(temp.is_empty())
        self.assertFalse(temp.search(10))
        temp.add(7)
        self.assertFalse(temp.search(8))
        self.assertEqual(temp.python_list(),[7])
        self.assertEqual(temp.python_list_reversed(),[7])
        temp.add(18)
        temp.add(67)
        self.assertEqual(temp.python_list(), [7,18,67])
        with self.assertRaises(IndexError): temp.pop(5)






if __name__ == '__main__': 
    unittest.main()
