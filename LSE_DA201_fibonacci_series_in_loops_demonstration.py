#!/usr/bin/env python
# coding: utf-8

# ### LSE Data Analytics Online Career Accelerator
# 
# # DA201: Data Analytics using Python

# ## Fibonacci Series in loops (tutorial video)

# *Use this Jupyter Notebook to follow along with the tutorial video. You can pause the video to make notes as comments or text blocks.*
# 
# Loops are used to iterate over a sequence, for example, lists, dictionaries, tuples, and sets. Let's investigate the Fibonacci Series.

# ## Example of a `for` loop

# In[1]:


# Create a variable.
beverages = ['coffee', 'tea', 'juices']

for beverage in beverages:
    print(beverage)


# ## Fibonacci Series with `for` and `while` loops

# In[ ]:


# Create a list with the first and second values of the Fibonacci series:
list_1 = [0, 1]

# Indicate n = the number of terms.
n = int(input("Enter number of term: "))
if n ==1:
    print('0')
elif n == 2:
    print(list_1)
else:
    while(len(list_1) < n):
        list_1.append(0)
    if (n == 0 or n == 1):
        print(1)
    else:
        list_1[0] = 0
        list_1[1] = 1
        for i in range(2, n):
            list_1[i] = list_1[i-1]+list_1[i-2]
            print(f'First {n} terms of Fibonacci Series {list_1}')


# #### Type any number in the open square and press enter.

# In[ ]:




