#
#Name: Nathan Diekema
#Date: 1/23/18
#
#Lab 2
#Section 202-05
#Purpose of Project: Implement the stack abstract data type useing two different implementations (built-in python List construct & linked data structure)
#

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    '''Implements an efficient last-in first-out Abstract Data Type using a Linked List'''

    def __init__(self, capacity):
        '''Creates an empty stack with a capacity'''
        self.capacity = capacity
        self.head = None
        self.num_items = 0

    def is_empty(self):
        '''Returns True if the stack is empty, and False otherwise
           MUST have O(1) performance'''
        return self.num_items == 0
             

    def is_full(self):
        '''Returns True if the stack is full, and False otherwise
           MUST have O(1) performance'''
        return self.capacity == self.num_items

    def push(self, item):
        '''If stack is n-ot full, pushes item on stack. 
           If stack is full when push is attempted, raises IndexError
           MUST have O(1) performance'''
        tempNode = Node(item)
        if self.capacity == self.num_items:
           raise IndexError('This stack is full')
         

        tempNode.next = self.head
        self.head = tempNode
        self.num_items += 1


    def pop(self): 
        """If stack is not empty, pops item from stack and returns item.
           If stack is empty when pop is attempted, raises IndexError
           MUST have O(1) performance"""
        
        if self.num_items == 0:
            raise IndexError
         
        tempNode = Node(self.head)

        self.head = self.head.next
        self.num_items -= 1
        return tempNode.data


    def peek(self):
        '''If stack is not empty, returns next item to be popped (but does not pop the item)
           If stack is empty, raises IndexError
           MUST have O(1) performance'''
        if self.num_items == 0:
            raise IndexError('This stack is empty')
        return self.head.data


    def size(self):
        '''Returns the number of elements currently in the stack, not the capacity
           MUST have O(1) performance'''
        return self.num_items

 