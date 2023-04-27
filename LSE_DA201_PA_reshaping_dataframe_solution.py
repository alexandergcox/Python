#!/usr/bin/env python
# coding: utf-8

# ### LSE Data Analytics Online Career Accelerator
# 
# # DA201: Data Analytics Using Python

# ## Practical activity: Reshaping a DataFrame

# **This is the solution to the activity.**
# 
# Mandisa Nkosi is working with with a political party that needs to decide how best to invest its available advertising budget. Mandisa believes she can gain some insights into potential advertising avenues by analysing films that are available on streaming platforms. 
# 
# This analysis uses the `movies_merge.xlsx` and `ott_merge.csv` data sets. Using the pivot() function, you will organise the DataFrame by:
# 
# - the film release date and content rating
# - the title of movies, the directors, and genres by content rating
# - the title of movies, the released year, and language by content rating
# - Netflix-screened movies based on language, runtime, and country
# - the title of movies, specified language, potential runtime, and genres by content rating.
# 
# The insights gained from the analysis will inform the campaign, promotional materials, slogans, and language the political party will use to reach potential voters.

# ## Prepare your workstation

# In[1]:


# Import Pandas.
import pandas as pd

# Load the Excel data using pd.read_excel.
movies = pd.read_excel('movies_merge.xlsx')

# Load the csv data using pd.read_csv.
ott = pd.read_csv('ott_merge.csv')

# Data imported correctly?
print(movies.columns)
print(movies.shape)
print(ott.columns)
print(ott.shape)

# Merge the two DataFrames.
mov_ott = pd.merge(movies, ott, how='left', on = 'ID')

# DataFrames merged correctly?
print(mov_ott.columns)
print(mov_ott.shape)


# In[2]:


# View the DataFrame.
mov_ott


# ## 1: The film release date and content rating

# In[3]:


# Determine movies per year and age group.
movies.pivot(index='Title', columns='Age', 
             values='Year')


# ## 2: The title of movies, the directors, and genres by content rating

# In[4]:


# Determine movies, directors, and genres per age group.
movies.pivot(index='Title', columns='Age', 
             values=['Directors', 'Genres'])


# ## 3: The title of movies, the released year, and language by content rating

# In[5]:


# Determine movies, year, and language per age group.
movies.pivot(index='Title', columns='Age', 
             values=['Year', 'Language'])


# ## 4: Netflix-screened movies based on language, runtime, and country

# In[6]:


# Determine the language, runtime, and country of movies screened by Netflix.
mov_ott.pivot(index='Title', columns='Netflix', 
              values=['Language', 'Runtime', 'Country'])


# ## 5: The title of movies, specified language, potential runtime, and genres by content rating

# In[7]:


# Determine the movies, language, runtime, and genres per age group.
mov_ott.pivot(index='Title', columns='Age', 
              values=['Language', 'Runtime','Genres'])


# In[ ]:




