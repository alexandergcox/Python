#!/usr/bin/env python
# coding: utf-8

# ### LSE Data Analytics Online Career Accelerator
# 
# # DA201: Data Analytics Using Python

# ## Writing a lambda function

# This Notebook accompanies the 'Writing a lambda function' demonstration video. In the video you will be introduced to the basics of writing lambda functions in Python.
# 
# Follow along with the demonstration to learn:
# - how to write a simple lambda function
# - how to employ the lambda function as part of a user-defined function
# - how to employ multiple arguments within a lambda function.

# ### 1. Prepare your workstation

# In[1]:


# Import the libraries.
import pandas as pd
import numpy as np

# Import the CSV file.
products = pd.read_csv('products.csv')

# View the DataFrame.
products


# ### 2. User-defined functions

# In[2]:


# How many products have the word 'glass' in their description?
# Use the keyword def.
# function_name = contains_glass
# argument = x

# User-defined function to determine the word glass in product descriptions.
def contains_glass(x):
    # docstring
    """does the product contain glass?"""
    y = x.lower()
    # execute the function
    return "glass" in y

# Apply the function.
fc = products['Description'].apply(contains_glass)

# Filter product for glass.
products[fc]


# ### 3. Lambda functions

# In[ ]:


# Lambda function
# lambda argument : expression


# In[3]:


# Write a lambda function to get the same result as with the user-defined function.
products[products['Description'].apply(lambda x:
                                     'glass' in x.lower())]


# In[4]:


# Investigate with only a Series.
products['Description'].apply(lambda x: 'glass' in x.lower())


# In[ ]:




