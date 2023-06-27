str = 'hello how are you?'

# use split to make a list from a string variable

print(str.split(' '))
# ['hello', 'how', 'are', 'you?']



fib1 = [1,1,2,3,5,8,13]
print(fib1)             # [1, 1, 2, 3, 5, 8, 13]

print(fib1[0])          # 1

print(fib1[5])          # 8

print(fib1[-1])         # 13

print(fib1[-3])         # 5

print(fib1[0:4])        # [1, 1, 2, 3]


# Concatenate Lists

fib2 = [21, 34, 55]

print(fib1 + fib2)      # [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]



# Change the values of the list
fib1[0] = 9
print(fib1)             # [9, 1, 2, 3, 5, 8, 13]


# append value to list
fib2.append(89)
print(fib2)             # [21, 34, 55, 89]


# remove last value on the list
fib2.pop()
print(fib2)             # [21, 34, 55]


# remove particular element
fib1.remove(9)          # this method only remove one of duplicate value (if there are two 9s on the list, it will remove one of them, not both of them)
print(fib1)             # [1, 2, 3, 5, 8, 13]


# delete method, removing element according to it's position
del(fib1[3])
print(fib1)             # [1, 2, 3, 8, 13]


#--------------------------------------

# list can contain different types of data
chars = ['mario', 'luigi', 'don']
chars.append(5)
print(chars)         # ['mario', 'luigi', 'don', 5]   


#--------------------------------------


# lists within lists
super = [chars, fib1, [1,2,2,3,4]]
print(super)          # [['mario', 'luigi', 'don', 5], [1, 2, 3, 8, 13], [1, 2, 2, 3, 4]]

print(super[0])       # ['mario', 'luigi', 'don', 5]

print(super[1])       # [1, 2, 3, 8, 13]

print(super[2])       # [1, 2, 2, 3, 4]

print(super[2][1])    # 2
# returning value at index 1 from 
# the list at position or index) 2