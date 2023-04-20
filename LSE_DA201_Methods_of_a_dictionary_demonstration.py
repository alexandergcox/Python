#!/usr/bin/env python
# coding: utf-8

# ### LSE Data Analytics Online Career Accelerator 
# 
# # DA201:  Data Analytics with Python

# ## Methods of a dictionary (tutorial video)

# This file contains the code snippets that are introduced in the Methods of a dictionary video. Follow along with the demonstration to:
# - delete an entry from a dictionary
# - iterate through keys and values
# - create a dictionary from a sequence.
# 
# Play and pause the video to follow along with the demonstration.

# ### 1. Create a dictionary

# In[ ]:


# Create a dictionary
d1 = {'key1': 'Name',
     'key2': 'Age',
     'key3': 'Nationality',
     'key4': 'Email'}


# ### 2. Delete an entry

# In[ ]:


# Example of deleting an entry from a dictionary.
# Delete an entry.
del d1['key1']

print(d1)


# In[ ]:


# Example of deleting an entry from a dictionary using the pop() method
# Delete key 3.
d1.pop('key3')

print(d1)


# ### 3. Key and value iterators

# In[ ]:


# Example of the keys() method to retrieve keys from a dictionary.
# Create a dictionary.
d2 = {'key1': 'Name',
     'key2': 'Age',
     'key3': 'Nationality'}

# Show keys only.
print(d2.keys())


# In[ ]:


# Example of the values() method to retrieve values from a dictionary.
# Show values only.
print(d2.values())


# ### 4. Create a dictionary from sequence

# In[ ]:


# Example of creating a dictionary from a sequence.
# Create two sequences.
key_list = ['key1', 'key2', 'key3', 'key4', 'key5']
value_list = ['Apple', 'Fruit', 'Red', 'Juicy', 'Firm']

# View keys.
print(key_list)
# View values.
print(value_list)

# Create a new dictionary.
d3 = dict(zip(key_list, value_list))

# View dictionary.
print(d3)

