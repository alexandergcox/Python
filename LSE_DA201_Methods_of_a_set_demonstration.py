#!/usr/bin/env python
# coding: utf-8

# ### LSE Data Analytics Online Career Accelerator 
# 
# # DA201:  Data Analytics with Python

# ## Methods of a set (tutorial video)

# This file contains the code snippets that are introduced in the Methods of a set video. Follow along with the demonstration to:
# - add items to a set 
# - add items from one set to another 
# - use the set union method
# - use the set intersection method
# - use the set difference method
# - use the set symmetric difference method.  
# 
# 
# Play and pause the video to follow along with the demonstration.

# ### 1. Create two sets

# In[ ]:


# Create two sets.
set1 = set([1, 2, 3, 4, 4, 2])
set2 = {5, 6, 7, 7, 6, 5}


# ### 2. Add items to a set

# In[ ]:


# Example of adding an item to a set
# Use the .add() method.
set1.add('cake')

# View the set.
print(set1)


# ### 3. Add items from one set to another set

# In[ ]:


# Example of adding an item to a set.
# Use the update() method.
set1.update(set2)

# View the set.
print(set1)


# ### 4. The set union method

# In[ ]:


# Example of the union() method
# Create two new sets.
set3 = {'apple', 'banana', 'cherry'}
set4 = {'google', 'microsoft', 'apple'}

# View set1, set3, and set4.
print(set1)
print(set3)
print(set4)


# In[ ]:


# Syntax: set.union(set1, set2...).
set5 = set1.union(set3, set4)

# View the set.
print(set5)


# ### 5. The set intersection method

# In[ ]:


# View the sets.
print(set3)
print(set4)


# In[ ]:


# Example of the intersection() method.
# Use the intersection() method.
# Syntax: set.intersection(set1, set2 ... etc).
z = set3.intersection(set4)

# View the set.
print(z)


# ### 6. The set difference method

# In[ ]:


# Example of the .difference() method.
# Syntax: set.difference(set).
x = set4.difference(set3)

# View the set.
print(x)


# ### 7. The set symmetric difference method

# In[ ]:


# Example of the symmetric_difference() method.
# Syntax: set.symmetric_difference(set).
a = set1.symmetric_difference(set2)

# View the set.
print(a)

