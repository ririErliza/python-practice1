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


