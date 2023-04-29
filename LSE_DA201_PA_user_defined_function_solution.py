#!/usr/bin/env python
# coding: utf-8

# ### LSE Data Analytics Online Career Accelerator
# 
# # DA201: Data Analytics Using Python

# ## Practical activity: Write and apply user-defined functions

# **This is the solution to the activity.**
# 
# Mandisa Nkosi is working with with a political party that needs to decide how best to invest its available advertising budget. Mandisa believes she can gain some insights into potential advertising avenues by analysing films that are available on streaming platforms. 
# 
# This analysis uses the `movies_merge.xlsx` and `ott_merge.csv` data sets. To help the political party make the decision about advertisements, Mandisa comes up with a few questions she feels will be possible to explore from the available data and useful for the political party:
# 
# - What is the average rating per movie?
# - How many movies were released per content rating (age)?
# - How many movies were released per year?
# 
# The insights gained from the analysis will inform the campaign, promotional materials, slogans, and language the political party will use to reach potential voters.

# ### Prepare your workstation

# In[1]:


# Import Pandas.
import pandas as pd
import numpy as np

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


# # 

# ## Question 1: What is the average rating per movie?

# In[2]:


# View IMDb and Rotten Tomatoes columns.
mov_ott_ratings = mov_ott[['ID', 'IMDb', 'Rotten Tomatoes']]

# View the DataFrame.
mov_ott_ratings


# In[3]:


# Replace missing values with 0.
mov_ott_ratings_final = mov_ott_ratings.fillna(0)

# View the DataFrame.
mov_ott_ratings_final


# In[4]:


# Add a new column to the DataFrame indicating average rating.
# Average rating is ((IMDb/10) + Rotten Tomaties)/n.
# Write a user defined function.
def av_col2(df1,df2):
    df = (df1/10 + df2)/2
    return df

mov_ott_ratings_final['Rating'] = av_col2(mov_ott_ratings_final['IMDb'],
                                          mov_ott_ratings_final['Rotten Tomatoes'])

# View the DataFrame.
mov_ott_ratings_final                    


# # 

# ## Question 2: How many movies were released per content rating (age)?

# In[5]:


# Categorical count. 
def cat_cnt(df1):
    print(df1.value_counts())

# Number of movies released per 'Age'.
df = mov_ott['Age'].astype('category')

# View the output.
cat_cnt(df)


# # 

# ## Question 3: How many movies were released per year?

# In[6]:


# Categorical count. 
def cat_cnt(df1):
    print(df1.value_counts())

# Number of movies released per 'Year'.
df = mov_ott['Year'].astype('category')

# View the output.
cat_cnt(df)


# In[ ]:




