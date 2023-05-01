#!/usr/bin/env python
# coding: utf-8

# ### LSE Data Analytics Online Career Accelerator 
# 
# # DA201:  Data Analytics with Python

# ## Application of the map() function (tutorial video)

# This file contains the code snippets that are introduced in the 'Application of the map() function' video. 
# Follow along with the demonstration to: 
# - change data types in a DataFrame
# - change a column heading in a DataFrame.
# 
# Play and pause the video to follow along with the demonstration.

# ### 1. Import pandas and create a DataFrame

# In[1]:


# Import Pandas.
import pandas as pd

# Read the CSV files from the current working directory.
classlist_a = pd.read_csv('classlist_a.csv')
classlist_b = pd.read_csv('classlist_b.csv')
classlist_c = pd.read_csv('classlist_c.csv')
classlist_d = pd.read_csv('classlist_d.csv')

# Concatenate the four class lists.
classlist = pd.concat([classlist_a, classlist_b, classlist_c, classlist_d])

# View the new DataFrame.b
print(classlist.shape)
print(classlist.columns)
print(classlist.dtypes)


# ### 2. Change the values from strings to integers

# In[2]:


# Use the map() function only on a Pandas Series i.e. a single column.
# Change the values from strings to integers.
classlist['Class_num'] = classlist.Class.map({'A':0, 'E':1})

# View the DataFrame.
print(classlist.shape)
classlist.head()


# ### 3. Compare the two class columns

# In[3]:


# Compare the columns Class and Class_num with the loc() function.
print(classlist.loc[:, ['Class', 'Class_num']])

# Compare the columns Class and Class_num with the iloc() function.
classlist.iloc[:, 4:6]


# ### 4. Change the column heading

# In[4]:


classlist_final = classlist.rename(columns={'Final mark':'Final_mark'})

classlist_final.head()


# In[ ]:




