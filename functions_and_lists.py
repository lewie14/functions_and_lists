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

#Create a function named double_index that has two parameters named lst and index. 
#The function should double the value of the element at index of lst and return the new list with the doubled value.

def double_index(lst, index):
  if index < len(lst):
  	lst[index] = lst[index] * 2
  return lst

#Uncomment the line below when your function is done
print(double_index([3, 8, -10, 12], 2))

#Create a function named remove_middle which has three parameters named lst, start, and end. 
#The function should return a sub-list of lst with all elements with index between start and end removed (inclusive).

#For example, the following code should return [4, 23, 42] because elements at indices 1, 2, and 3 have been removed
#removeMiddle([4, 8 , 15, 16, 23, 42], 1, 3)

def remove_middle(lst, start, end):
  return lst[:start] + lst[end+1:]

#Uncomment the line below when your function is done
print(remove_middle([4, 8, 15, 16, 23, 42], 1, 3))
