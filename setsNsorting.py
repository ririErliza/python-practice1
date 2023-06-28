# Set
# Sets are used to store multiple items in a single variable.

# Set is one of 4 built-in data types in Python used to store 
# collections of data, the other 3 are List, Tuple, and Dictionary, 
# all with different qualities and usage.

# A set is a collection which is unordered, unchangeable*, and unindexed.

# * Note: Set items are unchangeable, but you can remove items and add new items.

# Duplicates Not Allowed

#-------------------------------------------

# sorting data (lists) in to numerical and 
# alphabetical order. 
# We'll also look at a new data type called sets. 
# Sets are a collection of data which do 
# not allow duplicate values within them.

#-------------------------------------------

nums = [1,4,2,7,2,3,4,6,1,8] #this is a list
# we want to sort it
print(sorted(nums))
# [1, 1, 2, 2, 3, 4, 4, 6, 7, 8]

names = ['shaun', 'ryu', 'abe', 'Apple', 'Brian', 'shaun']
print(sorted(names))
# ['Apple', 'Brian', 'abe', 'ryu', 'shaun', 'shaun']
# in python, capital letter comes first


# say we want to eliminate the duplicates in nums
# we can use set
print(set(nums))
# {1, 2, 3, 4, 6, 7, 8}
# it returns a set data type
# with NO DUPLICATE

print(set(names))


