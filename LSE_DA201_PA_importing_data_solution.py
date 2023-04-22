#!/usr/bin/env python
# coding: utf-8

# ### LSE Data Analytics Online Career Accelerator
# 
# # DA201: Data Analytics using Python

# ## Practical activity: Importing data

# **This is the solution to the activity.**
# 
# Canopy is a new boutique streaming company that is looking to create an app to provide recommendations for each user based on their recently watched movies. You are working with the team to better understand the data. 
# 
# You have access to the data sets `movies.xlsx` and `ott.csv` from Canopy.

# ## 1. Import Pandas

# In[ ]:


# Import the necessary packages
import pandas as pd


# In[ ]:


# Import the movies data set
movies = pd.read_excel('movies.xlsx')

# View the DataFrame
movies.head()


# In[ ]:


# Import the ott data set
ott = pd.read_csv('ott.csv')

# View the DataFrame
ott.head()


# # 

# ## 2. Validate data sets

# In[ ]:


# Validate the DataFrame with shape
print(movies.shape)

# View the DataFrame
print(ott.shape)


# In[ ]:


# Validate the DataFrame with the head() function
print(movies.head())

# View the DataFrame
print(ott.head())


# In[ ]:


# validate with tail()
print(movies.tail())

# View the DataFrame
print(ott.tail())


# # 

# ## 3. Describe the data sets

# In[ ]:


# Describe the data set
print(movies.dtypes)

# View the DataFrame
print(ott.dtypes)


# In[ ]:




