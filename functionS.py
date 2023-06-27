# block of code which can be used and calles upon whenever we need it later on in our code

def greet():
    print('Hello World')

greet() # Hello World

print('---------------------------------')


def hello(name,time):
    print(f'Good {time} {name}, hope you are well')


hello('Shaun', 'morning')
# Good morning Shaun, hope you are well

name=input('enter your name: ')
time=input('enter your time of day: ')

hello(name,time)
# Good afternoon Erliz, hope you are well


print('---------------------------------')

def hello(name='Ryu',time='morning'):
    print(f'Good {time} {name}, hope you are well')

hello()
# Good morning Ryu, hope you are well

hello('Shaun', 'Afternoon') #this will overwrite the defined parameter above
# Good Afternoon Shaun, hope you are well

hello(name='Shaun')
# Good morning Shaun, hope you are well