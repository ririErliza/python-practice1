ninjas = ['ryu', 'chrystal', 'yoshi', 'ken']

# use for loop to access individual ninja from the list ninjas

# for ninja in ninjas:
#     print(ninja)

# ryu
# chrystal
# yoshi
# ken

# we can use whatever name to call each ninja from ninjas list

# for x in ninjas:
#     print(x)

# this will give same results as above



# loop/ cycle through a portion of the list (using slice)

fruits = ['banana', 'apple', 'oranges', 'grapes']

# for x in fruits[1:3]:
#     print(x)

# apple
# oranges

# for fruit in fruits:
#     if fruit == 'apple':
#         print(f'{fruit} is sweet!')

# apple is sweet!


# for fruit in fruits:
#     if fruit == 'kiwi':
#         print(f'{fruit} is green!')
#     else:
#         print(fruit)

# banana
# apple
# oranges
# grapes


# (because the is no kiwi on the list)

# for fruit in fruits:
#     if fruit == 'oranges':
#         print(f'{fruit} is sweet!')
#     else:
#         print(fruit)

# banana
# apple
# oranges is sweet!
# grapes

for fruit in fruits:
    if fruit == 'oranges':
        print(f'{fruit} is sweet!')
        break
    else:
        print(fruit)

# banana
# apple
# oranges is sweet!

# (after looping through and found oranges, it prints the fruit and 
# other fruits on the list preceded oranges
# but because of 'break' operation, it stopped looping after oranges)

