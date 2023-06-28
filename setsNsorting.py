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
#{'ryu', 'abe', 'Apple', 'shaun', 'Brian'}
# duplicates eliminated
# but the order is messed


# we have dictionary here
ninjas = {
    'rey':'black',
    'yoshi':'red',
    'crystal':'red'
    }

print(set(ninjas.values()))
# {'black', 'red'}

print('_____________________________________')

# def fruit_count(dict):
#     fruits=list(dict.values())
#     for fruit in fruits: 
#         num = fruits.count(fruit)
#         print(f'There are {num} {fruit} fruits')

# above code cause duplicate
# add SET to code below
# so we can loop though data and avoid duplicate

def fruit_count(dict):
    fruits=list(dict.values())
    for fruit in set(fruits): 
        num = fruits.count(fruit)
        print(f'There are {num} {fruit} fruits')

fruits={}

while True:
    fruit_name = input('enter fruit name: ')
    fruit_color = input('enter the color: ')
    fruits[fruit_name]=fruit_color

    another=input('add another? (y/n)')
    if another == 'y':
        continue
    else:
        break

fruit_count(fruits) # we need to pass the dictionary here inside the func