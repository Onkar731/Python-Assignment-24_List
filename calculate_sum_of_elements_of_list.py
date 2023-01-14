"""
Write a python script to calculate sum of elements of a list
"""

# creating a list of elements 
# list in python can be created either of using square braces or list() method
l1 = [2, 123, 3, 45, 5, 343, 54, 345, 34, 787, 887,]

# to calculate sum of elements we can use builtins method sum() which returns the 
# sum of all elements of list
print("Sum() : Sum of elements is", sum(l1))

"""
we can also use for loop or while loop
defining sum variable to store sum of elements of list
    sum = 0
    for e in l1 :
        sum += e

    print("for loop : Sum of elements is", sum)

# using while loop
    i = 0
    sum1 = 0
    while i < len(l1) :
        sum1 += l1[i]
        i += 1

    print("while loop : Sum of elements is", sum1)
"""
