#!/usr/bin/env python
# coding: utf-8

# ### LSE Data Analytics Online Career Accelerator 
# 
# # DA201:  Data Analytics using Python

# ## Practical activity: Identify, interpret, and fix the errors

# **This is the solution to the activity.**
# 
# Your team member has a set of erroneous Python code and they've asked you for help. Project deadlines are looming and the work is threatening to pile up. After fighting the urge to preach the virtues of programming with the right problem-solving mindset to your clearly distressed colleague, you happily commit 10 minutes of your time to help them out and keep the project on track.
# 
# As a senior member of the team, you are expected to consider the following questions when encountering an error in the code:
# - Why is it an error?
# - What caused the error?
# - How do you interpret the error message?

# ## Code 1

# In[ ]:


# Code 1
# Print the price
sales_price = 24500

print(total_price)


# ### Code 1: Possible solution
# - Solution: Replace `print(total_price)` with `print(sales_price)`.
# - Reason: Variable was defined as `sales_price = 24500`.

# In[ ]:


# Code 1 - solution
# Print the sales price
sales_price = 24500

print(sales_price)


# # 

# ## Code 2

# In[ ]:


# Code 2
# Print a text string verbatim
print "My name is James Bond"


# ### Code 2: Possible solution
# - Solution: Add round brackets before and after string, delete the space between print and the string.
# - Reason: The `print()` function needs to specify what variable to print.

# In[ ]:


# Code 2 - solution
# Print a text string verbatim
print("My name is James Bond")


# # 

# ## Code 3

# In[ ]:


# Code 3
# Determine if x is greater than 10
x = 11 

if x > 10:
print('X is greater than 10')
else: 
    print('X is not greater than 10')


# ### Code 3: Possible solution
# - Solution: Four spaces before the first `print()` function. Best practices is to have a string in double quotes. 
# - Reason: The `print()` function forms part of the `if` statement code block.

# In[ ]:


# Code 3 possible solution
# Determine if x is greater than 10
x = 11 

if x > 10:
    print("X is greater than 10")
else: 
    print("X is not greater than 10")


# # 

# ## Code 4: 

# In[ ]:


# Code 4
# Create the variable list_a
list_a = [1,2,3,4,'Ayaan', 'Hirsi']

list_a[11]


# ### Code 4: Possible solution
# - Solution: There is no index number 11.
# - Reason: The index starts at `0` and there are a total of `6`; there is no index `11`. 

# In[ ]:


# Code 4 Possible solution
# Create the variable list_a
list_a = [1, 2, 3, 4, 'Ayaan', 'Hirsi']

list_a
print(list_a)


# In[ ]:




