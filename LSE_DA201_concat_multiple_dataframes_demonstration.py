#!/usr/bin/env python
# coding: utf-8

# ### LSE Data Analytics Online Career Accelerator
# 
# # DA201: Data Analytics using Python

# ## Concatenating multiple DataFrames with Pandas

# This Notebbok accompanies the Concatenating multiple DataFrames with Pandas demonstration video. In the video Dr Blake Miller demonstrates a more concise and precise method to concatenate more than two DataFrames.
# 
# Follow along with the demonstration to learn:
# - how to use a shorter code snippet to concat() four DataFrames
# - the advantages of combining code snippets.
# 

# ### 1. Import the CSV files

# In[2]:


# Import Pandas.
import pandas as pd


# In[3]:


# Import the four CSV files.
classlist_a = pd.read_csv('classlist_a.csv')
classlist_b = pd.read_csv('classlist_b.csv')
classlist_c = pd.read_csv('classlist_c.csv')
classlist_d = pd.read_csv('classlist_d.csv')


# ### 2. Concatenate (combine) the four files

# In[4]:


# Create one DataFrame.
classlist_final = pd.concat([classlist_a, classlist_b,
                             classlist_c, classlist_d])

# View the DataFrame.
classlist_final


# ### 3. Sort/organise by surname or student name

# In[5]:


# Sort the DataFrame.
classlist_final_sort = classlist_final.sort_values(by='Surname')

# View the DataFrame.
classlist_final_sort


# ### 4. Sort by student number

# In[6]:


# Sort the DataFrame.
classlist_final_sort = classlist_final.sort_values(by='Student number')

# View the DataFrame.
classlist_final_sort


# ### 5. The sorted() function

# In[7]:


# Apply sort to a list.
sorted(classlist_final)


# In[8]:


# Sort the column names.
sorted(classlist_final.columns)


# In[9]:


# Sort the column names.
sorted(classlist_final.columns, reverse=True)


# In[ ]:




