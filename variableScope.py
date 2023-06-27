# SCOPE = A variable is only available from inside the region it is created. This is called scope.

# Local scope, global scope

name1='ninja'
name2='roller'

def callName():
    print('the name inside the function is:', name1)

callName()

print('the name outside the function is:', name2)

# the name inside the function is: ninja
# the name outside the function is: roller

