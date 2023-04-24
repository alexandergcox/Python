#!/usr/bin/env python
# coding: utf-8

# ### LSE Data Analytics Online Career Accelerator
# 
# # DA201: Data Analytics using Python

# ## Practical activity: Filter the data

# **This is the solution to the activity.**
# 
# Canopy is a new boutique streaming company that is looking to create an app to provide recommendations for each user based on their recently watched movies. You are working with the team to better understand the data. 
# 
# You have access to the datasets `movies.xlsx` and `ott.csv` from Canopy.

# ### 1. Import Pandas, data sets and validate

# In[1]:


# Import the necessary packages.
import pandas as pd

# Import the movies data set.
movies = pd.read_excel('movies.xlsx')

# View the DataFrame.
movies.head()


# In[2]:


# Import the ott data set.
ott = pd.read_csv('ott.csv')

# View the DataFrame.
ott.head()


# In[3]:


# Validate the data types.
print(movies.dtypes)
print(ott.dtypes)


# In[4]:


# Determine the column names.
print(list(movies.columns))
print(list(ott.columns))


# ## 2. Filter the DataFrame for only numeric variables

# In[6]:


# Filter the DataFrame according to numeric variables.
movies_num = movies.select_dtypes('number')
movies_num = movies_num.drop('Year', axis = 1)


# ## 3. Calculate the IQR for each column except Year

# In[7]:


# Calculate Q1 and Q3.
Q1 = movies_num.quantile(0.25)
Q3 = movies_num.quantile(0.75)

# View the output
print(Q1)
print(Q3)


# In[ ]:


# Calculate the IQR.
IQR = Q3 - Q1

# View the output.
print(IQR)


# ## 4. Evaluate the range of the data set

# In[8]:


# Determine the descriptive statistics.
movies_num.describe()


# In[ ]:




