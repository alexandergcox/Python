#!/usr/bin/env python
# coding: utf-8

# ### LSE Data Analytics Online Career Accelerator 
# 
# # DA201:  Data Analytics with Python

# ## Subsetting a data set with Pandas (tutorial video)

# This file contains the code snippets that are introduced in the Subsetting a data set with Pandas video. Follow along with the demonstration to:
# - try the five different options for subsetting a large data set
# - understand the advantages of subsetting a large data set.
# 
# Play and pause the video to follow along with the demonstration.

# ### 1. Import Pandas and the data

# **Hint**: Upload the data file first if it is not yet in the same directory.

# In[2]:


# Import libraries with standard conventions
import pandas as pd

# Subset the data set with the header() function
# Read the FAO_raw.csv file
food = pd.read_csv('FAO_raw.csv')

# View the DataFrame
food.head()


# In[ ]:


# Dimensions of data set
food.shape


# In[3]:


# Determine the column names
col_names = list(food)

# View the DataFrame
col_names


# ## 2. Filter/subset data by columns

# In[4]:


# Column names with the read function
# Read the FAO_raw.csv file
food_usecols = pd.read_csv('FAO_raw.csv', 
                   usecols=['Area', 'Item', 'Element',
                            'Unit', 'latitude', 'longitude',])

# View the DataFrame
food_usecols.head()


# ## 3. Filter/subset data by rows

# In[5]:


# Number of rows with read function
# Read the FAO_raw.csv file
food_nrows = pd.read_csv('FAO_raw.csv', nrows=10)

# View the DataFrame
food_nrows


# ## 4. Filter/subset data with skiprows

# In[6]:


# Skiprows with read function
# Read the FAO_raw.csv file
food_skiprows = pd.read_csv('FAO_raw.csv', skiprows=3)

# View the DataFrame
food_skiprows.head()


# ## 5. Filter/subset data with skipfooter

# In[ ]:


# Determine if we have rows at the bottom of DataFrame.
food.tail()


# In[7]:


# Skipfooter with read function
# Read the FAO_raw.csv file
food_skipfooter = pd.read_csv('FAO_raw.csv', skipfooter=1)

# View the DataFrame
food_skipfooter.tail()


# In[ ]:




