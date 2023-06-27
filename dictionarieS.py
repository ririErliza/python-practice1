# another data type

# a lil bit like objects in JS

fruits = {
    'banana' : 'yellow',
    'apple': 'red'
}

print(fruits)
# {'banana': 'yellow', 'apple': 'red,'}

print('oranges' in fruits)
# False
print('apple' in fruits)
# True

print(fruits.keys())
# dict_keys(['banana', 'apple'])

print(list(fruits.keys()))
# ['banana', 'apple']

print(fruits.values())
# dict_values(['yellow', 'red,'])

vals = list(fruits.values())
print(vals)
# ['yellow', 'red,']

print(vals.count('red'))
# 1

print(vals.count('blue'))
# 0

fruits['kiwi'] = 'green'
print(fruits)
# {'banana': 'yellow', 'apple': 'red', 'kiwi': 'green'} 

print('_____________________________________')
# creating dictionaries

person = dict(name='Liyl', age = 34, height = '160cm')
print(person)
{'name': 'Liyl', 'age': 34, 'height': '160cm'}

print('_____________________________________')

# adding key n value to empty dict

def fruits_collection(dict):
    for key, val in dict.items():
        print(f'{key} : {val}')

fruits1={}

while True:
    fruit_name = input('enter fruit name: ')
    fruit_color = input('enter the color: ')
    fruits1[fruit_name]=fruit_color

    another=input('add another? (y/n)')
    if another == 'y':
        continue
    else:
        break

fruits_collection(fruits1)