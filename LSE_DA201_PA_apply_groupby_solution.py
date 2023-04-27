#!/usr/bin/env python
# coding: utf-8

# ### LSE Data Analytics Online Career Accelerator
# 
# # DA201: Data Analytics Using Python

# ## Practical activity: Use groupby() and aggregate() functions

# **This is the solution to the activity.**
# 
# Mandisa Nkosi is working with with a political party that needs to decide how best to invest its available advertising budget. Mandisa believes she can gain some insights into potential advertising avenues by analysing films that are available on streaming platforms. 
# 
# This analysis uses the `movies_merge.xlsx` and `ott_merge.csv` data sets. At this stage, you will answer the questions:
# 
# - How many films from each year (released from 2012 to the present) were watched on Netflix?
# - What is the average runtime of movies released each year?
# - What are the best and worst reviews that movies released each year received on Rotten Tomatoes?
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


# ## Question 1: How many films from each year (released from 2012 to the present) were watched on Netflix?

# In[2]:


# Determine the number of movies watched on Netflix since 2012.
mo_gpby = mov_ott.groupby(['Year'])['Netflix'].agg('sum').reset_index()
mo_gpby[mo_gpby['Year'] >= 2012]


# ## Question 2: What is the average runtime of movies released each year?

# In[3]:


# Determine the average runtime of movies released since 2012.
mo_gpby1 = mov_ott.groupby(['Year'])['Runtime'].agg('mean').reset_index()
mo_gpby1[mo_gpby1['Year'] >= 2012]


# ## Question 3: What are the best and worst reviews that movies released each year received on Rotten Tomatoes?

# In[4]:


# Determine what was the maximum and minimum review received by Rotten Tomatoes for any movie per year since 2012?
mo_gpby2 = mov_ott.groupby(['Year'])['Rotten Tomatoes'].agg(['min','max']).reset_index()
mo_gpby2[mo_gpby2['Year'] >= 2012]


# In[ ]:




