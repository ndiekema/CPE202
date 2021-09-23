#
#Name: Nathan Diekema
#Student ID:
#Date: 1/13/18
#
#Lab 2
#Section 202-05
#Purpose of Lab: Recursion vs Iteration
#


#This function will return the largest of a list of numbers
#list -> int
def max_list_iter(int_list):  # must use iteration not recursion
   """finds the max of a list of numbers and returns the value (not the index)
   If int_list is empty, returns None. If list is None, raises ValueError"""
   if int_list == None:
      raise ValueError
   if len(int_list) == 0:
      return None

   maxNum = int_list[0]
   for x in int_list:
      if x > maxNum:
         maxNum = x
   return maxNum

#This function will reverse the order of a list
#list -> list
def reverse_rec(int_list):   # must use recursion
   """recursively reverses a list of numbers and returns the reversed list
   If list is None, raises ValueError"""
   if len(int_list) == 0:
        raise ValueError

   return helper(int_list)

def helper(lst):
  if len(lst) == 0 or len(lst) == 1:
     return lst
  return (helper(lst[1:]) + [lst[0]])


#This function will use binary search to return the index of a target number
#int int int list -> int
def bin_search(target, low, high, int_list):  # must use recursion
   """searches for target in int_list[low..high] and returns index if found
   If target is not found returns None. If list is None, raises ValueError """
   
   if len(int_list) == 0:
      raise ValueError
   else:     
       midpoint = ((high+low)//2)
       if midpoint == high == low and int_list[midpoint] != target:
          return None
       #print("NOW", int_list[low], int_list[high], target)
       if target == int_list[midpoint]:
          return midpoint
       elif target > int_list[midpoint]:
          return bin_search(target,midpoint+1,high,int_list)
       elif target < int_list[midpoint]:
          return bin_search(target,low,midpoint-1,int_list)