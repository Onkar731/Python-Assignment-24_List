"""
Write a python script to sort list elements in descending order
"""

# creating a list of elements 
# list in python can be created either of using square braces or list() method
l1 = [2, 123, 3, 45, 5, 343, 54, 345, 34, 787, 887,]

# to sort list elements in descending order we can use builtins method sorted()
# or sort() method of list
# to sort list elements in descending order we should pass a keyword argument
# in method i.e. reverse = True

# using sorted() method - sorted() method doesn't perform any changes in list
# instead it returns new list of sorted elements
print(sorted(l1, reverse=True))

# using sort() method - sort() method changes the position of elements in list
l1.sort(reverse=True)
print(l1)
