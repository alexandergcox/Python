#!/usr/bin/env python
# coding: utf-8

# ### LSE Data Analytics Online Career Accelerator
# 
# # DA201: Data Analytics Using Python

# ## Practical activity: Create and merge the DataFrames

# **This is the solution to the activity.**
# 
# Mandisa Nkosi is working with with a political party that needs to decide how best to invest its available advertising budget. Mandisa believes she can gain some insights into potential advertising avenues by analysing films that are available on streaming platforms. 
# 
# This analysis uses the `movies_merge.xlsx` and `ott_merge.csv` data sets. Your objectives at this stage are to prepare for analysis by:
# 
# - importing the CSV files into DataFrames
# - viewing the DataFrames
# - describing the DataFrames to understand the structures and data types
# - merging the two DataFrames into a single DataFrame.
# 
# The insights gained from the analysis will inform the campaign, promotional materials, slogans, and language the political party will use to reach potential voters.

# ## 1. Import Pandas

# In[1]:


# Import necessary package.
import pandas as pd


# ## 2. Import Excel file

# In[4]:


# Load the Excel data using pd.read_excel.
movies = pd.read_excel('movies_merge.xlsx')

# View the column names.
print(movies.columns)


# ## 3. Import CSV file

# In[6]:


# Load the csv data using pd.read_csv.
ott = pd.read_csv('ott_merge.csv')

# View the column names.
print(ott.columns)


# ## 4. Validate the DataFrames

# In[7]:


# Data imported correctly?
print(movies.shape)
movies.head()


# In[8]:


# Data imported correctly?
print(ott.shape)
ott.head()


# ## 5. Describe the data types

# In[ ]:


# Determine the data types.
print(ott.dtypes)
print(movies.dtypes)


# ## 6. Combine the two DataFrames
# ### a) merge()

# In[9]:


# Merge the two DataFrames.
df_mov_ott = pd.merge(movies, ott, how='left', on = 'ID')

# View the new DataFrame.
print(df_mov_ott.shape)
df_mov_ott.head()


# ### b) concat()

# In[10]:


# Concatenate the two DataFrames.
mov_ott_concat = pd.concat([movies, ott], axis=0)

# View the new DataFrame.
print(mov_ott_concat.shape)
mov_ott_concat.head()


# In[ ]:




