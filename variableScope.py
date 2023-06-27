# SCOPE = A variable is only available from inside the region it is created. This is called scope.

# Local scope, global scope

name1='ninja' #this is global variable can accesed globally
name2='roller'

def callName():
    print('the name inside the function is:', name1)

callName()

print('the name outside the function is:', name2)

# the name inside the function is: ninja
# the name outside the function is: roller



print('____________________________________')

# the varibale inside this function is local
# cant be accesed outside this func

def print_name():
    the_name= 'heral'
    print('name inside func:', the_name)

print_name()

# print('outside func: ', the_name)
# this will throw error
# the_name varibale is not defined


print('____________________________________')

# overwriting the global variable
# by changing the value locally
# but only change locally not globally

other_name = 'Trish'
def print_Othername():
    other_name= 'Clump'
    print('name inside func:', other_name)

print_Othername()

print('outside func: ', other_name)

# name inside func: Clump
# outside func:  Trish

print('____________________________________')

# typing global inside func next to variable name
# will change the value globally

some_name = 'Trish'
def print_Somename():
    global some_name
    some_name= 'Clump'
    print('name inside func:', some_name)

print_Somename()

print('outside func: ', some_name)

# name inside func: Clump
# outside func:  Clump

print('____________________________________')
