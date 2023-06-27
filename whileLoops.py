# while loop repeats a block of code as long as
# a certain CONDIITION is true.

#------------------------

# while CONDITION:
    #block of code

#------------------------

age = 25
num = 0

 
# while num < age:
#     print(num)
#     num+=5

# 0
# 5
# 10
# 15
# 20


# we only want to print EVEN number
# while num < age:
#     if num%2 ==0:
#         print(num)
#     num+=5

# 0
# 10
# 20

# break it at certain condition
while num < age:
    if num%2 ==0:
        print(num)
    if num > 10:
        break