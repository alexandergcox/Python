#!/usr/bin/env python
# coding: utf-8

# ### LSE Data Analytics Online Career Accelerator 
# 
# # DA201:  Data Analytics with Python

# ## Application of the apply() function (tutorial video)

# This file contains the code snippets that are introduced in the 'Application of the apply() function' video. 
# Follow along with the demonstration to use the apply function to: 
# - calculate the length of a string in a DataFrame
# - calculate the sum of values in a DataFrame
# - calculate the maximum value in a DataFrame.
# 
# Play and pause the video to follow along with the demonstration.

# ### 1. Import Pandas and create a DataFrame

# In[1]:


# Import Pandas.
import pandas as pd

# Import the CSV files.
classlist_a = pd.read_csv('classlist_a.csv')
classlist_b = pd.read_csv('classlist_b.csv')
classlist_c = pd.read_csv('classlist_c.csv')
classlist_d = pd.read_csv('classlist_d.csv')

# Concatenate the four class lists.
classlist= pd.concat([classlist_a, classlist_b, classlist_c, classlist_d])

# View the DataFrame.
classlist.head()


# ### 2. Calculate the length of each string in the Surname column.

# In[2]:


# Use the apply() function to apply a function (len()) to each element within a Series (the Surname column).
# Find the length of each surname in the DataFrame.
classlist['Surname_length'] = classlist.Surname.apply(len)

# View the DataFrame.
classlist.head()


# ### 3. Import a CSV from a website and create a DataFrame

# In[3]:


# Import a CSV data set with a URL from a website.
drinks = pd.read_csv('http://bit.ly/drinksbycountry')

# View the DataFrame.
print(drinks.shape)
print(drinks.dtypes)
drinks.head()


# ### 4. What is the total beverage serving per country?

# In[4]:


# Create a new DataFrame.
# Use subset, all rows, and certain columns.
drinks_country = drinks.loc[:, 'country':'wine_servings']

# View the DataFrame.
drinks_country.head()


# In[5]:


# Find the total beverage serving per country.
drinks_country['country_total'] = drinks_country['beer_servings'] + drinks_country['spirit_servings'] + drinks_country['wine_servings']

# View the DataFrame.
drinks_country.head()


# ### 5. What is the maximum serving per beverage?

# In[6]:


# Pass the max() function to the selected rows and columns.
drinks_country.loc[:, 'beer_servings':'country_total'].apply(max, axis=0)


# In[7]:


# View which country each max value belongs to. 
print(drinks_country.sort_values('country_total', ascending=False))
print(drinks_country.sort_values('beer_servings', ascending=False))
print(drinks_country.sort_values('spirit_servings', ascending=False))
print(drinks_country.sort_values('wine_servings', ascending=False))


# In[ ]:




