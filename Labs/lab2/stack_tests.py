#
#Name: Nathan Diekema
#Date: 1/23/18
#
#Lab 2
#Section 202-05
#Purpose of Project: Implement the stack abstract data type useing two different implementations (built-in python List construct & linked data structure)
#


import unittest

# Use the imports below to test either your array-based stack
# or your link-based version
#from stack_array import Stack
from stack_linked import Stack


#These are my test cases for both stacks_linked and stacks_array
class TestLab2(unittest.TestCase):
    def test_simple(self):
        stack = Stack(5)
        stack.push(0)
        self.assertFalse(stack.is_empty())
        self.assertFalse(stack.is_full())
        self.assertEqual(stack.size(),1)

    def test_1(self):
        stack = Stack(9)
        stack.push(1)
        stack.push(2)
        stack.pop()
        stack.pop()
        with self.assertRaises(IndexError): stack.pop()
        self.assertTrue(stack.is_empty())
        self.assertFalse(stack.is_full())
        self.assertEqual(stack.size(),0)
        with self.assertRaises(IndexError): stack.peek() 
    
    def test_2(self):
        stack = Stack(3)
        stack.push(2)
        stack.push(3)
        stack.push(9)
        with self.assertRaises(IndexError): stack.push(1)
        self.assertFalse(stack.is_empty())
        self.assertTrue(stack.is_full())
        self.assertEqual(stack.size(),3)
        self.assertEqual(stack.peek(), 9)


    def test_3(self):
        stack = Stack(5)
        stack.push(5)
        stack.push(8)
        self.assertEqual(stack.peek(), 8)
        self.assertFalse(stack.is_empty())
        self.assertFalse(stack.is_full())
        self.assertEqual(stack.size(),2)
        stack.pop()
        self.assertEqual(stack.peek(), 5)
        stack.pop()
        self.assertTrue(stack.is_empty())
        self.assertFalse(stack.is_full())
        with self.assertRaises(IndexError): stack.pop()







if __name__ == '__main__': 
    unittest.main()
