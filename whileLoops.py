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
# while num < age:
#     if num%2 ==0:
#         print(num)
#     if num > 10:
#         break
#     num+=1

# 0
# 2
# 4
# 6
# 8
# 10

# continue (we dont want to print the 0)
while num < age:
    if num == 0:
        num +=1 #this is a must otherwise we will get an infinite loop
        continue
    if num%2 ==0:
        print(num)
    if num > 10:
        break
    num+=1

# 2
# 4
# 6
# 8
# 10

