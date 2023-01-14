"""
Write a python script to calculate average of elements of a list
"""

# creating a list of elements 
# list in python can be created either of using square braces or list() method
l1 = [2, 123, 3, 45, 5, 343, 54, 345, 34, 787, 887,]

# to calculate average of list elements we can use builtins method sum() and len()
print("Average of list elements is", sum(l1)/len(l1))