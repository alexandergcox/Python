#!/usr/bin/env python
# coding: utf-8

# ### LSE Data Analytics Online Career Accelerator 
# 
# # DA201:  Data Analytics with Python

# ## Application of the applymap function (tutorial video)

# This file contains the code snippets that are introduced in the 'Application of the applymap function' video. 
# Follow along with the demonstration to use the applymap function to: 
# - apply a function to every element within a DataFrame
# 
# Play and pause the video to follow along with the demonstration.

# ### 1. Import pandas and create a DataFrame

# In[1]:


# Import Pandas.
import pandas as pd

# Import a CSV data set with a URL from a website.
drinks = pd.read_csv('http://bit.ly/drinksbycountry')

# View the DataFrame.
print(drinks.shape)
print(drinks.dtypes)


# ### 2. Change integer values to floats using applymap()

# In[2]:


# Employ the applymap function to specified columns.
drinks_new = drinks.loc[:, 'beer_servings':'wine_servings'].applymap(float)

# View the DataFrame.
drinks_new.head()


# In[ ]:




