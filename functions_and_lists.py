#Example syntax

def first_plus_last(lst):
  return lst[0] + lst[-1]

#produces
'''
>>> first_plus_last([1, 2, 3, 4])
5
>>> first_plus_last([8, 2, 5, -8])
0
>>> first_plus_last([-10, 2, 3, -4])
-14
'''
#-------------------Double Values-------------------------------------
#Create a function named double_index that has two parameters named lst and index. 
#The function should double the value of the element at index of lst and return the new list with the doubled value.

def double_index(lst, index):
  if index < len(lst):
  	lst[index] = lst[index] * 2
  return lst

print(double_index([3, 8, -10, 12], 2))

#-------------------Remove Middle----------------------------------------
#Create a function named remove_middle which has three parameters named lst, start, and end. 
#The function should return a sub-list of lst with all elements with index between start and end removed (inclusive).

#For example, the following code should return [4, 23, 42] because elements at indices 1, 2, and 3 have been removed
#removeMiddle([4, 8 , 15, 16, 23, 42], 1, 3)

def remove_middle(lst, start, end):
  return lst[:start] + lst[end+1:]

print(remove_middle([4, 8, 15, 16, 23, 42], 1, 3))

#-----------------More than N--------------------------------------------
#Create a function named more_than_n that has three parameters named lst, item, and n. 
#The function should return True if item appears in the list more than n times. The function should return False otherwise

def more_than_n(lst, item, n):
  if lst.count(item) > n:
    return True
  else:
    return False

print(more_than_n([2, 4, 6, 2, 3, 2, 1, 2], 2, 3))

#-------------------More Frequent item--------------------------------------------------
#Create a function named more_frequent_item that has three parameters named lst, item1, and item2. 
#Return either item1 or item2 depending on which item appears more often in lst. 
#If the two items appear the same number of times, return item1

#Write your function here
def more_frequent_item(lst, item1, item2):
  if lst.count(item1) > lst.count(item2):
    return item1
  elif lst.count(item1) == lst.count(item2):
    return item1
  else:
    return item2

print(more_frequent_item([2, 3, 3, 2, 3, 2, 3, 2, 3], 2, 3))

#---------------Middle iten-------------------------------------
#Create a function called middle_element that has one parameter named lst. 
#If there are an odd number of elements in lst, the function should return the middle element. 
#If there are an even number of elements, the function should return the average of the middle two elements.

def middle_element(lst):
  if len(lst) % 2 == 0:
    return (lst[int(len(lst)/2)] + lst[(int(len(lst)/2))-1])/2
  else:
    return lst[int(len(lst)/2)]
print(middle_element([5, 2, -10, -4, 4, 5]))

#---------------Append Sum---------------------
def append_sum(lst):
  lst.append(lst[-1] + lst[-2])
  lst.append(lst[-1] + lst[-2])
  lst.append(lst[-1] + lst[-2])
  return lst

print(append_sum([1, 1, 2]))

#---------------------------Larger list---------------------------

def larger_list(lst1, lst2):
  if len(lst1) == len(lst2):
    return lst1[-1]
  elif len(lst1) < len(lst2):
    return lst2[-1]
  else:
    return lst1[-1]

print(larger_list([4, 10, 2, 5], [-10, 2, 5, 10]))

#------------------------Combine Sort----------------------------------
#The function should combine these two lists into one new list and sort the result. Return the new sorted list.
def combine_sort(lst1, lst2):
  lst3 = lst1 + lst2
  sorted_lst3 = sorted(lst3)
  return sorted_lst3

print(combine_sort([4, 10, 2, 5], [-10, 2, 5, 10]))

#-------------------------Append Size----------------------------
#Create a function called append_size that has one parameter named lst. The function should add all of the 
#numbers between 1 and the size of lst (inclusive) to the end of lst. The function should then return this new list.
def append_size(lst):
  for i in range(1, len(lst) + 1):
  	lst.append(i)
  return lst

print(append_size([23, 42, 108]))

#--------------------Every 3 numbers--------------------------------------
#Create a function called every_three_nums that has one parameter named start. 
#The function should return a list of every third number between start and 100 (inclusive). 
#For example, every_three_nums(91) should return the list [91, 94, 97, 100]. 
#If start is greater than 100, the function should return an empty list.

def every_three_nums(start):
  return list(range(start, 101, 3))

print(every_three_nums(91))
