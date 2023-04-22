#!/usr/bin/env python
# coding: utf-8

# ### LSE Data Analytics Online Career Accelerator 
# 
# # DA201:  Data Analytics using Python

# ## Week 1: Introduction to Python programming!

# The focus this week is on introducing, setting up, and exploring Python. You will use this notebook to follow along with the demonstrations throughout the week. If you are using Jupyter Notebook for the first time, please refer to the documentation to lear about the interface and how best to use your notebook. 
# 
# Learn about using your Jupyter Notebook here: https://jupyter-notebook.readthedocs.io/en/latest/ui_components.html
# 
# This is your notebook. Use it to follow along with the demonstrations, test ideas and explore what is possible. The hands-on experience of writing your own code will accelerate your learning!

# ### 1.1 Python for data analysis 

# There are no Jupyter Notebook demonstrations in this section.

# # 

# ### 1.2 Basics of Python programming

# In[1]:


#string data type
a= "This is a string value"
b='This is a string value'

print(type(a))
print(type(b))


# In[1]:


#Integer vs float data types
value_a = 1299
value_b = 10.39

print(type(value_a))
print(type(value_b))


# In[ ]:





# In[2]:


#string data type
a= This is a string value
b=This is a string value

print(type(a))
print(type(b))


# In[3]:


#boolean data type
a= True
b= False

print(type(a))
print(type(b))


# In[4]:


#create a variable
n = 300
#view the variable with the print() function
print(n)


# In[5]:


#create three variable
var_a = 100
var_b = 100.05
name = 'Soni'

print (var_a, var_b, name)


# In[6]:


# Assign three variable with the same value

a = b = c = 50

print(a)
print(b)
print(c)
print(a,b,c)


# # 

# In[7]:


#Assign multiple values to multiple variables
a, b, c = 50, 50, 50

print(a)
print(b)
print(a, b, c)

#stipulate a single value.
a, b, c = 50

print(a,b,c)


# In[8]:


# Multiple variables with different values and data types.
a, b, c = 5, 50.25, "Python"
print(a, b, c)
print(a)
print(b)
print(c)


# In[9]:


# View the list of keywords.
import keyword
print(keyword.kwlist)


# In[10]:


# create three variable

jedi = warrior = saviour = 'luke skywalker'
print(jedi)

print(warrior)
print(saviour)
print(jedi, warrior, saviour)


# In[2]:


#create three variable for a name and create a tuple

a = b = c = 'Darth Vader'
print(a)
print(b)
print(c)
print(a,b,c)


# In[3]:


#create a list with all pizza names
pizza = ['Regina', 'Hawaiian', 'Mexican', 'Margarita', 'Marinara']

#print all the pizza names
for i in pizza:
    print(i)


# In[4]:


#creating a block comment

#comment line 1
#comment line 2
#comment line 3

print("hello world")


# In[5]:


""" This is the method of writing comments inside triple quotations.
Any lines between these triple quotations are treated as comments. """


# In[ ]:


#Assigning a sales tax of 20% at the end of the year
companytax20 = 1.20

#Assigning a sales tax of 30% at the end of the year
companytax30 = 1.30


# In[ ]:


#accounts for travel time
traveltime *= 2.5


# In[ ]:


# Switch turns to other player.
if playerTurn == PLAYER_X:
    playerTurn = PLAYER_O
elif playerTurn == PLAYER_O:
    playerTurn = PLAYER_X


# In[ ]:


# Keep asking the user until they enter a valid email.
while True:   


# In[ ]:


""" Cat Herder 3.0 Copyright (C) 2022 AI Master. All rights reserved.
See license.txt for the full details. """


# In[ ]:


# TODO : Investigate why this fails every Tuesday.
chargeIonFluxStream() 


# In[ ]:


# !/usr/bin/env python3 
# -*- coding: utf-8 -*-


# In[6]:


#demonstrating the = operator
a = 10
print (a)


# In[7]:


#demonstrating the + operator.
# Adds the right operand to the left operand

a = 10
a +=5
print(a)


# In[8]:


#demonstrating the - operator.
a = 10
a -= 5

print(a)


# In[9]:


#demonstrating the * operator.
a = 10
a *= 5

print(a)


# In[10]:


#demonstrating the / operator 
a = 10
a /=5

print(a)


# In[11]:


#demonstrating the % operator
a = 10
a %=5

print(a)


# In[12]:


#demonstrating the ** operator
a = 10
a **= 2

print(a)


# In[13]:


#demonstrating the // operator
a = 10
a //=5

print(a)


# In[14]:


#demonstrating the + operator
a = 10
b = 5

print(a + b)


# In[15]:


#demonstrating the - operator
a = 10
b = 5

print(a - b)


# In[16]:


#demonstrating the * operator
a = 10
b = 5

print(a * b)


# In[17]:


#demonstrating the / operator
a = 10
b = 5

print(a / b)


# In[18]:


#demonstrating the modulus operator
a = 10
b = 5

print(a % b)


# In[19]:


#demonstrating the exponent operator
a = 9 

print(a ** 2)


# In[20]:


#demonstrating the == operator
a = 10
b = 10

print(a == b)


# In[21]:


#demonstrating the not equal operator
a = 10
b = 10

print(a != b)


# In[22]:


#demonstraing the > operator
a = 10
b = 5

print(a > b)


# In[23]:


#demonstrating the < operator
a = 10
b = 5

print  (a < b)


# In[24]:


#demonstrating the greater or equal to operator 
a = 10
b = 5

print(a >= b )


# In[25]:


#demonstrating the <= operator.
a = 10
b = 5

print(a <= b)


# In[ ]:


#here is the syntax to define a function.
#The indented statements are the reusable portion.
#Defining a function doesn't use the function.
#Notice the colon.
def function_name (optional arguments or parameters):
    #use four spaces to indent each level of the function code.
    statement_1
    statement_2
    statement_3
    
#To use a function, we have to call it using a function call.
#A function call is performed using the functions name and parentheses().
#If any arguments or parameters are required these will sit in the paretheses().


function_name()
# This will run all the statements you have defined in the function.
# This single line of code - the function name and arguments - will run
# All the statements in the function.


# In[26]:


# Define a function to welcome new members to the programme.
# No arguments in the parethesis, include the colon.

def new_member():
    #The function code statement.
    print("Hello and welcome to the programme")
    
#call the function.
new_member()


# In[27]:


# Define an output variable
output = new_member()

# Check if the function returns a value.
output is None


# In[28]:


# Assign the function output to a variable.
# Function must return explicitly.
def new_member():
    return "Hello and welcome to the programme"

# Define an output variable.
output = new_member()

# Check if the function returns a value.
output is None


# In[29]:


# Example using f string interpolation.
def new_member(name):
    # Notice the "f".
    return f"Hello and welcome to the program, {name}!"

# The print function allows you to easily preview the output.
print(new_member('Sarah'))


# In[30]:


#Alternative line for the previous example
def new_member(name):
    # Note the space before closing the quotation mark after.
    return "Hello and welcome to the program, " + name + '!'

#The print function allows you to easily preview the output.
print(new_member('Sarah'))


# In[31]:


# Example of providing incorrect arguments.
def new_member(name):
    #Alternative line for the previous example
    return "Hello and welcome to the program, " + name + '!'

print(new_member('Sarah, 'Josh', 'Rae'))


# In[33]:


# Example of adding two positional arguments.
def add_optional_bonus(a, b, c=0, d=0):
    return a + b + c + d

add_optional_bonus(5,6)


# In[34]:


# Example of adding two positional arguments and a keyword argument.
def add_optional_bonus(a, b, c=0, d=0):
    return a + b + c + d

# Include the keyword c
add_optional_bonus(5, 6, c=5)


# In[35]:


# Example of adding two positional arguments and a keyword argument out of sequence.
def add_optional_bonus (a,b, c=0, d=0):
    return a + b + c + d

# Including the keyword d
add_optional_bonus(5, 6, d=6)


# In[36]:


# Example of adding two positional arguments and multiple keyword arguments.
def add_optional_bonus(a, b, c=0, d=0):
    return a + b + c + d 

#Including both d and c (out of sequence).
add_optional_bonus (5, 6, d=6, c=5)


# In[37]:


# Keyword arguments must follow positional arguments.
def add_optional_bonus (a, b, c=0, d=0):
    return a + b + c + d

#Including d and c
add_optional_bonus(d=6, c=5, 5, 6)


# In[41]:


# Returning multiple values
def membership_number(x):
    a = x + 1
    b = x + 2
    c = x + 3
    return a, b, c
    
# To show the membership numbers
x, y, z = membership_number(5)

print(x, y, z)


# In[43]:


# Using the * for a variable argument.
def workout_time(*reported):
    total_minutes = sum(reported)
    if total_minutes < 60:
        return f"Total weekly workout time is {total_minutes}minutes."
    else:return f"Total weekly workout time is {total_minutes/60}hours."
        
# The function passes any number of minutes.
print(workout_time(10, 10, 20))

# The function passes any number of minutes.
print(workout_time(60, 60, 20, 40))


# In[45]:


# Example of creating a list
# Notice the square brackets

new_list = ['Python', 'Java', 'Ruby']

print(new_list)


# In[46]:


# List can also store different data types such as strings, integers and float.

list_2 = ['cat', 12, 15.2]

print(list_2)


# In[47]:


# Example of a list with duplicates.

list_a = ['apple', 'banana', 5, 2, 5, 10.2, 8, 10.2, 'banana', 'apple']

print(list_a)


# In[48]:


# Example of list with duplicate
# Nested list

list_a = ['apple', 'banana', 5, 2, 10.2, 8.3, ['apple', 'banana', 5, 2, 10.2, 8.3]]

print(list_a)


# In[49]:


# Example of the len() function.
# Start with a list.
planets = ['Mercury', 'Venus', 'Earth', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']

# Measure the length of the list.
len(planets)


# In[53]:


# Example of slicing
# Create a list 

veg = ['spinach', 'pumpkin', 'onion', 'lettuce', 'carrot', 'cabbage', 'broccoli', 'aspargus']

# Don't use the print function for the slicing method
veg[2:6]


# In[54]:


# Using step increments for slicing

veg = ['spinach', 'pumpkin', 'onion', 'lettuce', 'carrot', 'cabbage', 'broccoli', 'aspargus']

# Index position in python is 0.
# List name [start index : stop index : step size].

veg[1:7:2]


# In[55]:


print(veg)


# In[56]:


# Example of selecting a range of elements and changing default step parameter
# Empty values will use the defaults.

veg[::2]


# In[58]:


# Example of using negative index.
# Pass -2 to reverse the list.

veg[::-2]


# In[59]:


# Create a tuple
tuple_1 = ('Python', 'Java', 'Ruby')

print(tuple_1)
len(tuple_1)


# In[60]:


# Example of a list with different data types.

tuple_a = ('apple', 'banana', 5, 2, 10.2, 8.3)

print(tuple_a)


# In[61]:


# Example of a list with duplicate items.
tuple_b = ('apple', 'banana', 5, 2, 10.2, 8.3, 'apple', 'banana', 5, 2, 10.2, 8.3)

print(tuple_b)


# In[62]:


# Example of a nested tuple.
tuple_c = ('apple', 'banana', 5, 2, 10.2, 8.3, ('apple', 'banana', 5, 2, 10.2, 8.3))

print(tuple_c)


# In[64]:


# Example of assigning values to objects.
celestial_objects = ('Earth', 'Saturn', 'Pluto')

planet, gas_giant, dwarf_planet = celestial_objects

# Each of these will output the corresponding object from the tuple.
print(planet)
print(gas_giant)
print(dwarf_planet)
print(dwarf_planet, gas_giant, planet)


# In[65]:


# Example of assigning values to objects.
celestial_objects = ('Earth', 'Saturn', 'Pluto')

# Notice two variables, while the tuple contains three objects.
# This will result in an error.
planet, gas_giant = celestial_objects


# In[67]:


# Example of modifying a list within a tuple.
tup = (1, 2, 'Pluto', [1 , 2, 3])

# Identify the index position of the list and make the modification.
# Appending 4 to the list
tup[3].append(4)

print(tup)
print(len(tup))


# In[68]:


# Create a tuple with three different data types.
tup_1 = (1, 1.10, 5, 5.1, 6.8)

# View the tuple.
print(tup_1)

# View the length of the table
print(len(tup_1))

# View the minimum value of the tuple
print(min(tup_1))

# View the maximum value of the tuple
print(max(tup_1))

# View the first value of the tuple.
print(tup_1[0])

# View the middle value of the tuple.
print(tup_1[2])


# In[70]:


# Example of the dictionary data structure
# Notice how each key has a value joined by:.
# Notice the curly brackets.
dict_1 = {'key1':'Name',
          'key2': 'Age',
          'key3': 1964}
    
print(dict_1)


# In[71]:


# Original dictionary
print(dict_1)

# Change the value of key 2.
dict_1['key2'] = 'new_value'
print(dict_1)


# In[72]:


# Dictionary before edits.
print(dict_1)

# Add a new key value pair.
dict_1['key4'] = 'address'

print(dict_1)


# In[73]:


# Dictionary before edits
print(dict_1)

# Example of changing and replacing values in a dictionary.
dict_1['key4'] = ['48 Mainstreet']

print(dict_1)


# In[74]:


# dictionary before edit
print(dict_1)

# Example of storing values in a separate variable.
# Define the new varaible.
new_val = dict_1['key4']

print(new_val)


# In[75]:


# Example of a set.
set1 = set([1, 2, 3, 4, 4, 2])

# View the set.
print(set1)

# View the data type.
print(type(set1))


# In[76]:


# Example of a set.
set2 = {5, 6, 7, 7, 6, 5}

#View the set.
print(set2)

#View the data type.
print(type(set2))


# In[77]:


# Find the intersection 
fruit = {'apple', 'pear', 'watermelon', 'tomato'}
vegetables = {'carrot', 'tomato', 'parsnip', 'leek'}

print(fruit.intersection(vegetables))


# In[78]:


# Add beetroot to vegetables with add().
vegetables.add('beetroot')

# View set vegetable.
print(vegetables)


# In[79]:


# combine two sets with union()#
edible_plants = vegetables.union(fruit)

# View the vegetables set.
print(edible_plants)


# In[80]:


# Identify the vegetables in the edible_plants set.
# Use .difference().

print(edible_plants.difference(fruit))


# In[81]:


# Create two variable.

a = 20
b = 5

# Use the if statement.
# Specify the test expression a > b.

if a > b:
    # Note the indentation
    # View the output as a string.
    print("a is greater than b")


# In[82]:


# Create two variables.
a = 2
b = 5

# Use the if statement.
# Specify the test expression a > b.
# Note the colon.

if a>b:
    # View the output as a string.
    print("a is greater than b")


# In[83]:


# Create two variables.
a = 20
b = 5 

# Use the if statement.
# Specify the test expression a < b.
# Note then colon(:).

if a < b:
    # Note the indention.
    # View the output as a string.
    print("a is smaller than b")

# Use the elif statement.
# Specify the test expression as a > b.
elif a > b:
    print("a is greater than b")


# In[84]:


# create two variables.
a = 2
b = 5

# Use the if statement.
#Specify the test expression as a > b.
if a > b:
    print("a is greater than b")
    
# specify test expression

elif a < b:
    print("a smaller than b")


# In[85]:


# Create two variables.
a = 20
b = 5

# Use the if statement,
# Specify the test expression a == b

if a == b:
    print(" a is equal to b")
    
elif a < b:
    print("a is smaller than b")

else:
    print("a is bigger than b")


# In[86]:


# Create two variables.
a = 20
b = 5

# Use the if statement.
# Specify the test expression a > b

if a > b:
    print("a is bigger than b")
    
elif a == b:
    print("a is equal to b")
    
else:
    print("a is smaller than b")


# In[87]:


# Print each iteam in the list
cities = ['London', 'Paris', 'New York City', 'Singapore']

# 'item' in this line is an object in the list.
for item in cities:
    #View the list.
    print(item)


# In[88]:


# Print each item in the string.
a = 'Top Cities'
# i is a variable.
for i in a:
    #View the list.
    print(i)


# In[89]:


# Print each item in the string.
a = 'Top Cities'
# i is a variable.
for l in a:
    #View the list.
    print(l)


# In[90]:


# Print each item in a tuple.
tup_a = ('London', 'Paris', 'New York City')
#Print each item inside a tuple.
for i in tup_a:
    print(i)


# In[91]:


# Print each iteam in a tuple
tup_a = ('London', 'Paris', 'New York')

#Print each item inside a tuple.
for i in tup_a:
    print(i)


# In[92]:


#  Print each item in a tuple.
a_dict = {'city': 'London', 'age': 2000, 'population':8.9}
# Age given in years and pop. in millions.
for i in a_dict:
    print(i)


# In[93]:


# create a variable
i = 1
# Specify the condition.
while i < 9:
    # This is the loop body - the += operator is adding the 1 to i.
    i += 1
    # View the output.
    print(i)


# In[95]:


# Define the variable
count = 0
# Specify the condition.
while count < 5:
    count = count + 1
    # Specify the docstring with f""
    print(f"count : {count}")
    # View the output
    print("Python is fun!")


# In[96]:


i = 0
a = 'aeroplane'

# The len function returns the length of the object.
while i < len(a):
    if a[i] == 'a' or a[i] == 'n':
        i+= 1
        continue
        
    print("Current letter :", a[i])
    i += 1


# In[97]:


#Print each adjective for every fruit.
adj = ['red', 'big', 'tasty']
fruits = ['apple', 'banana', 'cherry']

for x in adj:
    for y in fruits:
        print (x,y)


# In[98]:


# Exit the loop when 'x' is New York City.
cities = ['London', 'Paris', 'New York City', 'Singapore']
for x in cities:
    print(x)
    
    if x == 'New York City':
        break


# In[101]:


#Do not print New York City and continue to Singapore.
cities = ['London', 'Paris', 'New York City', 'Singapore']
for x in cities:
    
    if x == "New York City":
        continue
    print(x)


# In[102]:


cities = ['London', 'Paris', 'New York City', 'Singapore']

for i in cities:
    pass


# In[108]:


# Creat a list of five cars.
cars = ["Nissan", "Ford", "Toyota", "Fiat", "VW"]

# Create a for loop.
for i in cars:
    # Create a statement.
    print(i)
    
    #Create an if statement.
    if i == 'Toyota' 
    
    #insert a break statement.
    break


# In[ ]:





# In[ ]:





# ### 1.3 Python libraries and reproducibility of code

# In[115]:


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def introduce(self):
        print(f"Hello my name is {self.name} and I\'m {self.age} years old")
        
person_object = Person("alex", "28")
person_object.introduce()


# In[ ]:


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def introduce(self):
        print(f"Hello my name is {self.name} and I\'m {self.age} years old")
        
person_object = Person("alex", "28")
person_object.introduce()


# In[118]:


class person:
    name = 'Jane'
    age = 22

x = hasattr(Person, 'age')
print(x)


# In[119]:


class Person:
    name = 'Jane'
    age = 22

x = getattr(Person, 'age')
print(x)


# In[120]:


class Person:
    name = 'Jane'
    age = 22

setattr(Person, 'age', 32)
    
x = getattr(Person, 'age')

print(x)


# In[121]:


class Person:
    name = 'Jane'
    age = 32
    
delattr(Person, 'age')

x = getattr(Person, 'age')
print(x)


# In[122]:


class Person:
    def __init__(self, name, age, language):
        self.name = name
        self.age = age
        self.language = language
    def introduce(self):
        print(f"Hello my name is {self.name} and I\'m {self.age} years old and I speak {self.language}.")
        
class Student(Person):
    pass

person_object = Student('James', 30, 'English')
person_object.introduce()


# In[123]:


# write a class weather with three attributes temperature, wind speed and wind direction

class Weather:
    def __init__(self, temperature, wind_speed, wind_direction):
        self.temp = temperature
        self.wspeed = wind_speed
        self.wdirection = wind_direction
    def introduce(self):
        print(f"Hello! The weather today is {self.temp}, {self.wspeed} and {self.wdirection}.")

person_object = Weather('30 degress Celsius', '30km/h', 'SSE')
person_object.introduce()


# In[124]:


# Printing a specific date.
import datetime
d = datetime.date(2021, 6, 10)

print(d)
print(type(d))


# In[125]:


# Import date module from date class
from datetime import date
print(d - date(2022, 2, 10))
print(d)
print(type(d))


# In[126]:


# Printing current year, month and day.
from datetime import date
#date object of today's date
today = date.today()

print("Current year:", today.year)
print("Current month:", today.month)
print("Current day:", today.day)


# In[127]:


# Import module
from datetime import time
# Creating a time object.
# time(hour, minute, second, microsecond).
t = (6, 45, 25, 234566)

print("time =",t)


# In[128]:


# Import module and class
from datetime import datetime

t = datetime (2017, 11, 28, 23, 55, 59, 342380)
print("year =" t.year)
print("month =" t.month)
print("day =", t.day)
print("hour =" t.hour)
print("minute =", t.minute)
print("seconds =", t.second)
print("micro seconds =", t.microsecond)


# In[129]:


# Import the datetime module and datetime class.
from datetime import datetime

# Current date and time.
now = datetime.now()
print('Current time', now)

# Using strftime to only print hours, minutes and seconds.
t = now.strftime("&H:%M:%S")
print("Time with only hours, minutes and seconds", t)


# In[130]:


# The date string you create in the previous code snippet.
date_String = "30 October 2021"

#Print the date_string.
print("date_string=", date_string)
print("Data type of date-string -->", type(date_string))

# This is the date format
date_object = datetime.strptime(date_string, "&d %B %Y")

# Print the date_object.
print("date_object =", date_object)
print("Datatype of the date_string after formatting with strptime -->",
     type(date_object))


# In[131]:


# Solution: 
from datetime import time 
t = time(14, 42, 5, 566)
# if you type in 05 instead of 5 seconds, you will get an error

print("hour =", t.hour)
print("minute =", t.minute)
print("second =", t.second)
print("microsecond =", t.microsecond)


# In[132]:


# Solution : 
from datetime import datetime

dt = datetime(2019, 1, 28, 23, 55, 59, 1023)
print("year =", dt.year)
print("month =", dt.month)
print("day =", dt.day)
print("hour =", dt.hour)
print("minute =", dt.minute)
print("'seconds =", dt.second)
print("microsecond =", dt.microsecond)


# In[133]:


# Printing current year, month and day
from datetime import date

# Date object of today's date
today = date.today()

print("Current year:", today.year)
print("Current month:", today.month)
print("Current day:", today.day)


# In[134]:


import this


# In[ ]:





# In[ ]:




