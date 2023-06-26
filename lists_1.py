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
print(fib1) # [9, 1, 2, 3, 5, 8, 13]


# append value to list
fib2.append(89)
print(fib2)


