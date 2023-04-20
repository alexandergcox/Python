#!/usr/bin/env python
# coding: utf-8

# ### LSE Data Analytics Online Career Accelerator 
# 
# # DA201:  Data Analytics with Python

# ## Methods of a tuple (tutorial video)

# This file contains the code snippets that are introduced in the Methods of a tuple video. Follow along with the demonstration to:
# - check tuple length
# - use the tuple initiator
# - access tuple items
# - combine tuples
# - return specific items from a tuple.
# 
# Play and pause the video to follow along with the demonstration.

# ### 1. Create a tuple and check its length

# In[ ]:


# Example of the len() function to check the number of items in a tuple.
# Start with a tuple.
spices = ('Pepper', 'Thyme', 'Cinnamon', 'Oregano', 'Rosemary')

# View the tuple.
# Measure the length of the tuple.
print(spices)
len(spices)


# ### 2. Use the tuple initiator to create a tuple

# In[ ]:


# Example of the tuple() initiator to create a tuple. 
# Notice the round brackets.
tup_1 = tuple(['Basil', 'Anise'])

# View the tuple.
tup_1


# ### 3. Accessing tuple items

# In[ ]:


# Example of indexing to access a tuple item.
# Note: The index position in Python starts at 0.
# Locate item at index position 1.
spices[1]

# View the item.
print(spices[1])


# ### 4. Combining tuples

# In[ ]:


# Example of using the + operator to combine tuples.
total_spices = spices + tup_1

# This will show the concatenated tuple and its length.
print(total_spices)
print(len(total_spices))


# In[ ]:


# Example of using the * operator to multiply a tuple.
# This will make three copies of the tuple.
spices * 3


# ### 5. Max and min functions

# In[ ]:


# Example of using max() and min() to return specific items.
amount = (500, 250, 333, 450, 100)

# This will show the highest value.
print(max(amount))

# This will show the lowest value.
print(min(amount))

