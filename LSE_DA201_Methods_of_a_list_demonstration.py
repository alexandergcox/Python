#!/usr/bin/env python
# coding: utf-8

# ### LSE Data Analytics Online Career Accelerator 
# 
# # DA201:  Data Analytics with Python

# ## Methods of a list (tutorial video)

# This file contains the code snippets that are introduced in the Methods of a list video. Follow along with the demonstration to:
# - add and remove elements from a list
# - join and sort lists.
# 
# Play and pause the video to follow along with the demonstration.

# ### 1. Create a list

# In[2]:


# Start with a list
cheese = ['Brie', 'Mozzarella', 'Feta', 'Edam', 'Gouda', 'Camembert', 'Gruyere', 'Gorgonzola']


# ### 2. Add elements to a list

# In[3]:


# Add a new item at the end of the list using the append() method.
cheese.append('Blue')

# View the list and its length.
print(cheese)
print(len(cheese))


# In[4]:


# Add a new item at the end of the list using the insert() method.
# Here "1" is the index position.
# Note: The index position in Python starts at 0.
cheese.insert(1, 'Swiss')

# View the list and its length.
print(cheese)
print(len(cheese))


# In[5]:


# Example of the extend() method.
# Create a second list.
new_cheese = ['Parmesan']

# Second list is appended to starting list.
cheese.extend(new_cheese)

# View the list and its length.
print(cheese)
print(len(cheese))


# ### 3. Remove elements from a list

# In[6]:


# Example of the remove() method.
# Remove the first instance of an item from the list.
cheese.remove('Swiss') 

# View the list and its length.
print(cheese)
print(len(cheese))


# In[7]:


# Example of the pop() method
# Remove an item at a specific index position from the list.
# Note: The index position in Python starts at 0.
cheese.pop(8) 

# View the list and its length.
print(cheese)
print(len(cheese))


# In[8]:


# Example of the pop() method
# No index specified
cheese.pop()

# View the list and its length.
print(cheese)
print(len(cheese))


# ### 4. Joining two lists (concatenate)

# In[9]:


# Create two lists.
fruit_1 = ['apple', 'strawberry', 'pear', 'raspberry']
fruit_2 = ['apricot', 'peach', 'fig', 'plum']

# View the two lists.
print(fruit_1)
print(fruit_2)


# In[10]:


# Join the two lists with the + operator.
fruit = fruit_1 + fruit_2

# View the list and its length.
print(fruit)
print(len(fruit))


# ### 5. Sorting lists

# In[11]:


# Example of the sort() method.
# The default is to sort in ascending order.
fruit.sort()

# View the list.
print(fruit)


# In[12]:


# Example of the sort() method.
# To sort in descending order, the reverse is true.
fruit.sort(reverse = True)

# View the list.
print(fruit)


# In[ ]:




