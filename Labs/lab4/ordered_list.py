class Node:
    '''Node for use with doubly-linked list'''
    def __init__(self, item):
        self.item = item
        self.next = None
        self.prev = None

class OrderedList:
    '''A doubly-linked ordered list of items, from lowest (head of list) to highest (tail of list)'''

    def __init__(self):
        '''Use ONE dummy node as described in class
           ***No other attributes***
           Do not have an attribute to keep track of size'''
        self.sentinel = Node(None)
        self.sentinel.next = self.sentinel
        self.sentinel.prev = self.sentinel

    def is_empty(self):
        '''Returns back True if OrderedList is empty
            MUST have O(1) performance'''
        return self.sentinel.next == self.sentinel
        
    def add(self, item):
        '''Adds an item to OrderedList, in the proper location based on ordering of items
           from lowest (at head of list) to highest (at tail of list)
           If the item is already in the list, do not add it again 
           MUST have O(n) average-case performance'''
        newNode = Node(item)
        current = self.sentinel.next
        stop = 0
        dupe = 0

        while current != self.sentinel and stop == 0 and dupe == 0:
          if current.item >= item:
            if current.item == item:
              dupe = 1
            else:
              stop = 1
          else:
            current = current.next

        if dupe == 1:
          pass

        else:
          newNode.next = current
          newNode.prev = current.prev
          current.prev.next = newNode
          current.prev = newNode


    def remove(self, item):
        '''Removes an item from OrderedList. If item is removed (was in the list) returns True
           If item was not removed (was not in the list) returns False
           MUST have O(n) average-case performance'''
        current = self.sentinel.next
        while current.item != item:
            current = current.next
            if current == self.sentinel:
              return False

        current.prev.next = current.next
        current.next.prev = current.prev
        return True


    def index(self, item):
        '''Returns index of an item in OrderedList (assuming head of list is index 0).
           If item is not in list, return None
           MUST have O(n) average-case performance'''
        current = self.sentinel.next
        count = 0
        DNE = 0
        while item != current.item:
          current = current.next
          count += 1
          if current == self.sentinel:
            return None

        return count


    def pop(self, index):
        '''Removes and returns item at index (assuming head of list is index 0).
           If index is negative or >= size of list, raises IndexError
           MUST have O(n) average-case performance'''
        current = self.sentinel.next
        
        #Raises error if list is empty or index is negative  
        if current == self.sentinel or index < 0:
          raise IndexError
        count = 0
        
        while count != index:
          count += 1
          current = current.next  
          if current == self.sentinel: #Checks if index is > size of list
            raise IndexError
        
        current.prev.next = current.next
        current.next.prev = current.prev
        return current.item

    def search(self, item):
        '''Searches OrderedList for item, returns True if item is in list, False otherwise
           To practice recursion, this method must call a RECURSIVE method that
           will search the list
           MUST have O(n) average-case performance'''
        current = self.sentinel.next
        if current.item == None:
          return False 
        else:
          return self.search_helper(current,item)   #Question
    
    def search_helper(self,node,item):
        if node.item == item:
          return True
        elif node.item == None:
          return False
        elif node.item > item:
          return False
        else:
          return self.search_helper(node.next,item)

    def python_list(self):
        '''Return a Python list representation of OrderedList, from head to tail
           For example, list with integers 1, 2, and 3 would return [1, 2, 3]
           MUST have O(n) performance'''
        current = self.sentinel.next
        pythonlist = []
        while current != self.sentinel:
          pythonlist.append(current.item)
          current = current.next

        return pythonlist


    def python_list_reversed(self):
        '''Return a Python list representation of OrderedList, from tail to head, using recursion
           For example, list with integers 1, 2, and 3 would return [3, 2, 1]
           To practice recursion, this method must call a RECURSIVE method that
           will return a reversed list
           MUST have O(n) performance'''
        current = self.sentinel.next
        pythonlist = []
        while current != self.sentinel:
          pythonlist.append(current.item)
          current = current.next
        pythonlist.reverse()
        return pythonlist

    def size(self):
        '''Returns number of items in the OrderedList
           To practice recursion, this method must call a RECURSIVE method that
           will count and return the number of items in the list
           MUST have O(n) performance'''
        current = self.sentinel.next
        return self.size_helper(current, 0)


    def size_helper(self, node, count):
      if node == self.sentinel:
        return count
      else:
        return self.size_helper(node.next, count + 1)


