# block of code which can be used and calles upon whenever we need it later on in our code

def greet():
    print('Hello World')

greet() # Hello World

print('---------------------------------')


# def hello(name,time):
#     print(f'Good {time} {name}, hope you are well')


# hello('Shaun', 'morning')
# # Good morning Shaun, hope you are well

# name=input('enter your name: ')
# time=input('enter your time of day: ')

# hello(name,time)
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

print('---------------------------------')

# calculating using function



# def area(radius):
#     print(3.142*radius*radius)

# radius=int(input('enter radius: '))

# area(radius)

print('---------------------------------')

def area(radius):
    return 3.142*radius*radius

def vol(area,length):
    print('The volume is:', area*length)

radius=int(input('enter radius: '))
length=int(input('enter a length: '))

# area_calc=area(radius)
# vol(area_calc,length)

vol(area(radius),length) 
# this also work the same as above




