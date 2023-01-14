"""
Write a python script to create a list of squares of numbers of a given list
"""

# creating a list of elements 
# list in python can be created either of using square braces or list() method
l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,]

# creating a new empty list using list() method
sq_list = list()

# appending squares in list
for e in l1 :
    sq_list.append(e**2)

# printing list and square list 
print(l1, sq_list, sep='\n')

"""
    we can also use list comphrension to code preciesly
    
    sq_list1 = [e**2 for e in list(range(1, 11))]
"""