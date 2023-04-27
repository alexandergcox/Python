#!/usr/bin/env python
# coding: utf-8

# ### LSE Data Analytics Online Career Accelerator 
# 
# # DA201:  Data Analytics with Python

# ## Using aggregate functions on grouped data (tutorial video)

# This file contains the code snippets that are introduced in the Using aggregate functions on grouped data video. 
# Follow along with the demonstration to:
# - use the aggregate method as an operation on grouped data.
# 
# Play and pause the video to follow along with the demonstration.
# 
# Note: Steps 1 to 3 you completed in the demonstration video in '3.1.6 Introduction to groupby()'. These steps need to be run to complete this demonstration. The new code begins in Step 4.

# ### 1. Import pandas and create a DataFrame

# In[1]:


# Import Pandas.
import pandas as pd

# Read CSV files from the current working directory
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

# In[2]:


# Create group 1.
group_surname = classlist_final.groupby('Surname')

# View the DataFrame.
group_surname


# In[3]:


# Create group 2.
group_marks = classlist_final.groupby('Final mark')

# View the DataFrame.
group_marks


# In[4]:


# Create group 3.
group_surname_marks = classlist_final.groupby(['Surname', 'Final mark'])

# View the DataFrame.
group_surname_marks


# ### 3. Create a criteria

# In[5]:


# Create splitting within groups.
group_surname_marks.sum()


# ### 4. Determine the group sizes (option 1)

# In[6]:


# Use the size() function on the marks column.
group_surname_marks.size()


# In[7]:


# Use the size() function on the surname column.
group_surname.size()


# ### 5. Determine group sizes (option 2)

# In[8]:


# Create a group based on initials.
group_initials = classlist_final.groupby('Initials')

# Create group_surname_initials based on the surname and intials columns.
group_surname_initials = classlist_final.groupby(['Surname', 'Initials'])

# Find group size based on the initials and surname columns
group_surname_initials.size()


# ### 6. Determine group size using the count() function

# In[9]:


# Use the count() function.
group_surname_initials.count()


# In[ ]:




