#!/usr/bin/env python
# coding: utf-8

# In[2]:


# Create a DataFrane fir the car models
# Import Pandas
import pandas as pd

# Create a DataFrame.
cars = pd.DataFrame({'VW': ['Polo', 'T-Cross', 'Tiguan', 'Toureg'],
                    'Toyota': ['Agya', 'Corolla', 'Rav4', 'Land Cruiser'],
                    'Honda': ['Brio', 'Jazz', 'HRV', 'CRV'],
                    'BMW': ['BMW1', 'BMW2', 'BMW3', 'BMW4']},
                   index = [0, 1, 2, 3])

# View the DataFrame.
cars


# In[3]:


# Create a DataFrame for the motorcyle models,
motorcycles = pd.DataFrame({'VW': ['-', '-', '-', '-'],
                    'Toyota': ['-', '-', '-', '-'],
                    'Honda': ['Shine', 'Activa', 'Comfort Travel', 'Adventure Sport'],
                    'BMW': ['Sport', 'Roadster', 'Heritage', 'Adventure']},
                   index = [4, 5, 6, 7])

#View the DataFrame.
motorcycles


# In[4]:


# Concatenate two DataFrames.
products = pd.concat([cars, motorcycles])

# View the DataFrame.
products


# In[5]:


# Create cars_2 DataFrame.

cars_2 = pd.DataFrame({'VW': ['Polo', 'T-Cross', 'Tiguan', 'Toureg'],
                    'Toyota': ['Agya', 'Corolla', 'Rav4', 'Land Cruiser'],
                    'Honda': ['Brio', 'Jazz', 'HRV', 'CRV'],
                    'BMW': ['BMW1', 'BMW2', 'BMW3', 'BMW4']},
                   index = ['car1', 'car2', 'car3', 'car4'])

# Create motorcycles_2 DataFrame.
motorcycles_2 = pd.DataFrame({'VW': ['-', '-', '-', '-'],
                    'Toyota': ['-', '-', '-', '-'],
                    'Honda': ['Shine', 'Activa', 'Comfort Travel', 'Adventure Sport'],
                    'BMW': ['Sport', 'Roadster', 'Heritage', 'Adventure']},
                   index = ['mcycle1', 'mcycle2', 'mcycle3', 'mcycle4'])

# Concatenate the two DataFrames.
products_2 = pd.concat([cars_2, motorcycles_2])

# Concatenate the DataFrame.
products_2


# In[2]:


# Import Pandas.
import pandas as pd

# Read the CSV file.
classlist_a = pd.read_csv('classlist_a.csv')

# Determine shape of classlist.
print(classlist_a.shape)
classlist_a.head()


# In[4]:


# Read the csv files.
classlist_b = pd.read_csv('classlist_b.csv')

# Determine shape of classlist.
print(classlist_b.shape)
classlist_b.head()


# In[5]:


# Concat class list a and b.
classlist_ab = pd.concat([classlist_a, classlist_b])

# View the DataFrame.
print(classlist_ab.shape)
classlist_ab


# In[6]:


# Read the csv files.
classlist_c = pd.read_csv('classlist_c.csv')

# Determine shape of classlist.
print(classlist_c.shape)
classlist_c.head()


# In[7]:


# Read the csv files.
classlist_d = pd.read_csv('classlist_d.csv')

# Determine shape of classlist.
print(classlist_d.shape)
classlist_d.head()


# In[8]:


# Concat class list a and b.
classlist_cd = pd.concat([classlist_c, classlist_d])

# View the DataFrame.
print(classlist_cd.shape)
classlist_cd


# In[9]:


# Concat class list a and b.
classlist = pd.concat([classlist_ab, classlist_cd])

# View the DataFrame.
print(classlist.shape)
classlist


# In[ ]:




