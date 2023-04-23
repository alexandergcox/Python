#!/usr/bin/env python
# coding: utf-8

# ### LSE Data Analytics Online Career Accelerator
# 
# # DA201: Data Analytics using Python

# ## Practical activity: Handle missing data

# **This is the solution to the activity.**
# 
# Canopy is a new boutique streaming company that is looking to create an app to provide recommendations for each user based on their recently watched movies. You are working with the team to better understand the data. 
# 
# You have access to the data sets `movies.xlsx` and `ott.csv` from Canopy.

# ### 1. Import Pandas

# In[1]:


# Import the necessary packages
import pandas as pd


# ### 2. Import data sets

# In[2]:


# Import the movies data set
movies = pd.read_excel('movies.xlsx')

# View the DataFrame
movies.head()


# In[3]:


# Import the ott data set
ott = pd.read_csv('ott.csv')

# View the DataFrame
ott.head()


# ## 3. Calculate sum of missing data in Age column

# In[4]:


# Determine the sum of missing values
movies['Age'].isnull().sum()


# ## 4. Assign a specific value to missing data

# In[5]:


# Replace the missing values in Age column with a set value
movies['Age'][movies['Age'].isna()] = 'Others'


# In[6]:


# Replace the missing values in the directors, genres, country and language with others
movies['Directors'][movies['Directors'].isna()] = "Others"

movies['Genres'][movies['Genres'].isna()] = "Others"

movies['Country'][movies['Country'].isna()] = "Others"

movies['Language'][movies['Language'].isna()] = "Others"

# View the DataFrame
movies


# ## Advanced problem 

# In[ ]:


# Missing values for IMDb and Rotten Tomatoes
print(movies['IMDb'].isnull().sum())

print(movies['Rotten Tomatoes'].isnull().sum())


# In[ ]:


# Replace missing values with mean
movies['IMDb'].fillna(movies['IMDb'].mean(),inplace=True)

movies['Rotten Tomatoes'].fillna(movies['Rotten Tomatoes'].mean(),inplace=True)


# In[ ]:


# View the missing values for IMDb and Rotten Tomatoes
print(movies['IMDb'].isnull().sum())

print(movies['Rotten Tomatoes'].isnull().sum())


# In[ ]:




