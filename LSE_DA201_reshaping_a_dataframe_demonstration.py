#!/usr/bin/env python
# coding: utf-8

# ### LSE Data Analytics Online Career Accelerator 
# 
# # DA201:  Data Analytics with Python

# ## Reshaping a DataFrame (tutorial video)

# This file contains the code snippets that are introduced in the 'Reshaping a DataFrame' video. 
# Follow along with the demonstration to: 
# - stack a DataFrame
# - unstack a DataFrame
# - melt a DataFrame.
# 
# Play and pause the video to follow along with the demonstration.

# ### 1. Import pandas and create DataFrames

# In[1]:


# Import Pandas.
import pandas as pd

# Read the CSV files from the current working directory.
transactions = pd.read_csv('transactions_2010.csv')
products = pd.read_csv('products.csv')

# View the DataFrames.
print(transactions.shape)
print(transactions.columns)

print(products.shape)
print(products.columns)


# ### 2. Combine the DataFrames into a new DataFrame

# In[2]:


# Stack the customers.csv from DataFrame to Series.
trans_prod = pd.merge(transactions, products, how='left', on='StockCode')

# View the new DataFrame.
print(trans_prod.columns)
print(trans_prod.shape)


# ### 3. Stacking a DataFrame

# In[3]:


# Stack the transactions DataFrame from DataFrame to Series.
transactions_stack = transactions.stack()

# View the output.
transactions_stack


# In[4]:


# Compare the transactions_stack output to the original DataFrame.
print(transactions)


# In[5]:


# Confirm the change.
# View the data type(s).
print(type(transactions_stack))
# View the specified index.
print(transactions_stack.index)


# ### 4. Unstacking a DataFrame.

# In[6]:


# Unstack the transactions_stack DataFrame.
transactions_1 = transactions_stack.unstack()

# View the DataFrame.
transactions_1.head()


# In[7]:


# Compare the transactions_1 output to the original DataFrame.
transactions.head


# In[8]:


# Confirm the change.
# View the data type(s).
print(type(transactions_1))
# View the specified index.
print(transactions_1.index)


# ### 5. Melting a DataFrame

# In[9]:


# Melt the trans_prod DataFrame.
trans_prod.melt(id_vars='StockCode', value_vars='Description')


# In[10]:


# Compare the output to the original DataFrame.
print(trans_prod)


# In[ ]:




