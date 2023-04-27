#!/usr/bin/env python
# coding: utf-8

# ### LSE Data Analytics Online Career Accelerator 
# 
# # DA201:  Data Analytics with Python

# ## The split-apply-combine method (tutorial video)

# This file contains the code snippets that are introduced in the 'Split-apply-combine method' video. 
# Follow along with the demonstration to:
# - split data from a data set
# - apply criteria to values in a data set
# 
# Play and pause the video to follow along with the demonstration.

# ### 1. Import Pandas and create a DataFrame

# In[1]:


# Import Pandas.
import pandas as pd

# Read CSV files from the current working directory.
classlist_a = pd.read_csv('classlist_a.csv')
classlist_b = pd.read_csv('classlist_b.csv')
classlist_c = pd.read_csv('classlist_c.csv')
classlist_d = pd.read_csv('classlist_d.csv')

# Print the shape of each DataFrame.
print(classlist_a.shape)
print(classlist_b.shape)
print(classlist_c.shape)
print(classlist_d.shape)

# Merge four DataFrames into one DataFrame.
classlist_final = pd.concat([classlist_a, classlist_b,
                             classlist_c, classlist_d]) 

# View the DataFrame.
classlist_final.shape


# ### 2. Split data to create groups

# In[5]:


# Create Group 1.
group_surname = classlist_final.groupby('Surname')

# View the DataFrame.
group_surname


# In[4]:


# Create Group 2.
group_marks = classlist_final.groupby('Final mark')

# View the DataFrame.
group_marks


# In[6]:


# Create Group 3.
group_surname_marks = classlist_final.groupby(['Surname', 'Final mark'])

# View the DataFrame.
group_surname_marks


# ### 3. Create a criteria

# In[7]:


# Create splitting within groups.
group_surname_marks.sum()


# In[ ]:




