#!/usr/bin/env python
# coding: utf-8

# ### LSE Data Analytics Online Career Accelerator 
# 
# # DA201:  Data Analytics with Python

# ## Pivoting a DataFrame (tutorial video)

# This file contains the code snippets that are introduced in the Pivoting a DataFrame video. 
# Follow along with the demonstration to:
# - create pivot tables using the pivot() function.
# 
# Play and pause the video to follow along with the demonstration.

# ### 1. Import pandas and create a DataFrame

# In[1]:


import pandas as pd

astronauts = pd.read_csv('astronauts.csv')

print(astronauts.shape)
print(astronauts.columns)


# ### 2. What is the status and number of space flights undertaken by each astronaut?

# In[2]:


astronauts.pivot(index='Name', columns='Status', values='Space Flights')


# ### 3. What is the status, number of spacewalks, and number of  space flights for each astronaut?

# In[3]:


astronauts.pivot(index='Name', columns='Status', values=['Space Walks', 'Space Flights'])


# In[ ]:




