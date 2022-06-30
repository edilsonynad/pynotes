"""primitive types"""
#x = 12 #int 
#y =2.5 #float 
#name = "Jhon" #string
#is_cool = True #bool

#multiple assignment
from turtle import pensize


x, y, name, is_cool = (12, 2.5, 'Jhon', True)

#Math
a = int(x + y) #casting
b = x * y
c = x / y
d = x - y

#print(type(a), a, b, c, d)


"""Strings""" 

name = "Edilson"
age = 25

#Contatenate 
#print("Hello, my name is " + name + "and i am " + str(age))

#argments by position 
#print("My name is {name} and I am {age}".format(name=name,  age=age))

#F-Strings
#print(f'Hello my name is {name} and I am {age}')

#Strings methods
s = 'hello world'

#print(s.capitalize()) #capitalize string 

leng = len(s) #length of the string

#print(leng)


"""Lists"""

#Create a list 
numbers = [1,2,3,4,5,6]
numbers2 = list((1,2,3,4,5,6)) #using a constructor

fruits = ['Aplles', 'Oranges', 'Grapes', 'Pears']

#get a value from a position
#print(fruits[0])

#length of a list
#print(len(fruits))

#Change values 
fruits[0] = "Blueberries"

#Append to list 
fruits.append("Mangos")
#print(fruits)

#Remove items from list 
fruits.remove("Grapes")
#print(fruits)

#insert into a specific position
fruits.insert(2, "Strawberries")
#print(fruits)

#remove from a specific position 
fruits.pop(2)

#Reverse list 
fruits.reverse()
#print(fruits)

#Sort list 
fruits.sort()

#Reverse sort 
fruits.sort(reverse=True)


"""Tuples and sets"""
## A Tuple is a collection wich is ordered and unchangeable. Allows duplicate menbers.

#Create Tuple

frutas = ('Aplles', 'Oranges', 'Grapes')
#frutas2 = tuple(('Aplle', 'Orange', 'Grapes')) #using constructor

#single value needs trailing comma
frutas2 = ('Apples',)
#print(frutas2, type(frutas2))

#Get value from Tuple
#print(frutas[1])

#Can't change values in a tuple
frutas[0] = "Pears"

#delete a tuple
del frutas2

#lenght of a tuple 
#print(len(frutas))

## A Set is a collection which is unorded and unindexed. No duplicate menbers.

#Create a set
frutas_set = {'Apples', 'Oranges', 'Mango'}

#Check if an item is or not in a set
#print('Banana' in frutas_set)

#Add to set 
frutas_set.add('Grapes')
#print(frutas_set)

#Remove from set 
frutas_set.remove('Grapes')
#print(frutas_set)

#Clear set
frutas_set.clear()

#delete set 
del frutas_set

"""Dictionary"""
##A dictionary is a collection which is unordered, changeable an indexed. No duplicate menbers.

#Create a Dictionary

person = {
    'first_name': 'Jhon',
    'last_name': 'Doe',
    'age': 30
}

#person2 = dict(first_name='Sara', last_name='Williams') #using constuctor
#print(person2, type(person2))

#Get a value 
print(person['first_name'])
print(person.get('last_name'))

# Add key/value
person['phone'] = '555-555-5555'

#Change values 
person['first_name'] = "Edilson"
person['last_name'] = 'Lopes'

# Get dict keys 
print(person.keys())

# Get dict items 
print(person.items())

# Copy a dict 
person2 = person.copy()
person2['city'] = 'Boston'

# Remove a item
del(person['age'])
person.pop('phone')

# Clear dict 
person.clear()

# Get length
#print(len(person2))

#List od dict 
people = [
    {'name': 'Martha', 'age': 30},
    {'name': 'Helena', 'age': 15}
]

print(people[0]['name'])


"""Functions"""
#Create a function
def sayHello(name):
    print(f'Hello {name}')

sayHello('Jhon Doe')

# Return Valeus

def getSum(num1, num2):
    total = num1 + num2
    
    return total


print(getSum(2, 5))

"""Lambda Function"""
# A lambda function is a small anonymous function.
# A lambda function can take any number of arguments, but can only have one expression. Very similar to arrow function in JavaScript.


# Create a lambda func

getSoma = lambda num1, num2 : num1 + num2

print(getSoma(10, 3))




"""Conditionals"""
x = 10 
y = 5

#Simple if
if x > y:
    print(f'{x} is larger then {y}')

#If/Else
if x > y:
    print(f'{x} is larger then {y}')
else:
    print(f'{y} is larger than {x}')

#elif
if x > y:
    print(f'{x} is larger then {y}')
elif x == y:
    print(f'{x} is equal to {y}')
else:
    print(f'{y} is larger than {x}')
    
    
#Nested if
if x > 2:
    if x<= 10:
        print(f'{x} is greater than 2 and less than or equal to 10')

# Logical operators (and, or, not)
if x > 2 and x <= 10:
    print(f'{x} is greater than 2 and less than or equal to 10')
    
if x > 2 or x <= 10:
    print(f'{x} is greater than 2 and less than or equal to 10')
    
if not(x == y):
    print(f'{x} is greater than 2 and less than or equal to 10')


"""Menbership operators (not, not in) - are used to test if a sequence is presented in an object"""

numbers = [1,2,3,4,5,6]

# in
if x in numbers:
    print(x in numbers)
    
# not in
if x not in numbers:
    print(x not in numbers)


"""Identify operators (is, is not) - Compare the objects, not if they are equal, but if they are actually the same object with the same menory location"""

if x is y: 
    print(x is y)
    
if x is not y: 
    print(x is not y)
    
    
"""Loops"""


peoples = ['Jhon', 'Paul', 'Sara', 'Susan']   

#for loops 
for person in people:
    print(f"Current Person: {person}")
    
#break
for person in peoples:
    if person == 'Sara':
        break
    print(f"Currente Person: {person}")
    
#continue 
for person in peoples:
    if person == 'Sara':
        continue
    print(f"Currente Person: {person}")
    
#range 
for i in range(len(peoples)):
    print(peoples[i])

for i in range(0, 11):
    print(peoples[i])

#While loops 
count = 0
while count <= 10:
    print(f'Count: {count}')
    count += 1
    
    
"""Modules"""

# A module is basicaly a file containning a set of functions to include in your aplication.
# There are core python modules, modules you can install using pip package manager(including Django) as well as custom modules
#import datetime #importing a modules 
from datetime import date #importing a specific obeject from a module
import time 

today = date.today()
timestamp = time.time()

print(today)
print(timestamp)


#import from other Python files 
from ficha1 import reajusteSalarial

salario = float(input("Insira o seu salario"))
reajusteSalarial(salario)


