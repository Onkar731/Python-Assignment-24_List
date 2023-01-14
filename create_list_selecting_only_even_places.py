"""
Write a python script to create a list from a given list by selecting only even
places elements
"""

# creating a list of elements 
# list in python can be created either of using square braces or list() method
l1 = [2, 123, 3, 45, 5, 343, 54, 345, 34, 787, 887,]


# creating a new empty list
even_place_list = list()

# appending only even places elements in new list
i = 0
while i < len(l1) :
    even_place_list.append(l1[i])
    i += 2
    
# printing new list 
print(even_place_list)