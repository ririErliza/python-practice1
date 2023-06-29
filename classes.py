# how to find out the type of a variable

name = 'gisel'
age = 33
nums = [1,2,11,22,3,4,8]

# just use type(theVariableName)

print(type(name)) #<class 'str'>
print(type(age)) #<class 'int'>
print(type(nums)) #<class 'list'>

#----------------------------------------------

# Python Classes/Objects
# Python is an object oriented programming 
# language.
# Almost everything in Python is an object, 
# with its PROPERTIES and METHODS.
# A Class is like an object constructor, 
# or a "blueprint" for creating objects.

#----------------------------------------------

class Planet:

    def __init__(self):
        self.name = 'Mars'
        self.radius = 20000
        self.gravity = 5.5
        self.system = 'Mars System'

Mars = Planet()
print(f'name is: {Mars.name}')
print(f'radius is: {Mars.radius}')
print(f'gravity is: {Mars.gravity}')
print(f'system is: {Mars.system}')

# name is: Mars
# radius is: 20000
# gravity is: 5.5
# system is: Mars System

class laptop:

    def __init__(self):
        self.name = 'Acer'
        self.ram = 20000
        self.battery = 5.5
        self.system = 'windows'

    def os(self):
        return f'{self.name} has {self.system} as it\'s OS'
    
acer=laptop()

print(acer.os())
# Acer has windows as it's OS

# we attached method and properties to this class

# if we declare another variable and attach the same class
# that varibale will get the same poperties

noBrand = laptop()
print(noBrand.os())
# Acer has windows as it's OS


#-------------------------------------------
# now we want to make the class dynamic, can be used by other variables

class flour:
    def __init__(self, name, price, manufacture): # this is attributes
        self.name = name
        self.price = price
        self.manufacture = manufacture
    
    def prod(self): # this is method
        return f'This flour, {self.name}, is produced by {self.manufacture}'


terigu = flour('Terigu', 15000, 'Bogasari')
print(f'Name: {terigu.name}')
print(f'Price: {terigu.price}')
print(f'Manufacture: {terigu.manufacture}')
print(terigu.prod())
# This flour, Terigu, is produced by Bogasari

tepBeras = flour('Tepung beras', 18000, 'Rose Brand')
print(f'Name: {tepBeras.name}')
print(f'Price: {tepBeras.price}')
print(f'Manufacture: {tepBeras.manufacture}')
print(tepBeras.prod())
# This flour, Tepung beras, is produced by Rose Brand



#--------------Methods  &  Attributes-------------------------
# class level attributes

class Balls:

    shape = 'round' # this is class level attribute

    def __init__(self, name, price, manufacture): # this is instance attributes
        self.name = name
        self.price = price
        self.manufacture = manufacture
    
    def prod(self): # this is instance method
        return f'This ball, {self.name}, is produced by {self.manufacture}'


print(Balls.shape) # round

pingpong = Balls('Pingpong', 5000, 'Flutter')
print(pingpong.shape) # round

# print(Balls.name)
# this throws an error because the class balls dont have
# name attribute at class level
# name attribute is instance attribute

# @classmethod
class Balls_1:

    shape = 'round' # this is class level attribute

    def __init__(self, name, price, manufacture): # this is instance attributes
        self.name = name
        self.price = price
        self.manufacture = manufacture
    
    def prod(self): # this is instance method
        return f'This ball, {self.name}, is produced by {self.manufacture}'

    @classmethod
    def commons(cls):
        return f'All balls are {cls.shape}'
    

print(Balls_1.commons())
# All balls are round

pingpong = Balls_1('Pingpong', 5000, 'Flutter')
print(pingpong.commons())
# All balls are round


# print(Balls_1.prod())
# this will give an error because prod() is instance method

