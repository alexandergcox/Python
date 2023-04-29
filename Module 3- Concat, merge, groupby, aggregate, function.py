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


# In[10]:


# Create a DataFrame.
cars_3 = pd.DataFrame({'VW': ['Polo', 'T-Cross', 'Tiguan', 'Toureg'],
                    'Toyota': ['Agya', 'Corolla', 'Rav4', 'Land Cruiser'],
                    'Honda': ['Brio', 'Jazz', 'HRV', 'CRV'],
                    'BMW': ['BMW1', 'BMW2', 'BMW3', 'BMW4']},
                      index = [0, 1, 2, 3])

# View the DataFrame.
cars_3


# In[ ]:


motorcycles_3 = pd.DataFrame({'VW': ['-', '-', '-', '-'],
                    'Toyota': ['-', '-', '-', '-'],
                    'Honda': ['Shine', 'Activa', 'Comfort Travel', 'Adventure Sport'],
                    'BMW': ['Sport', 'Roadster', 'Heritage', 'Adventure']},
                   index = [0, 1, 2, 3])

# View the DataFrame.
motorcycles_3


# In[13]:


# Merge the DataFrames.
products_3 = pd.merge(cars_3, motorcycles_3)

# View the DataFrame.
products_3


# In[15]:


# Merge class lists ab and cd
classlist_final = pd.merge(classlist_ab, classlist_cd,
                          how='outer', on='Student number')

# View the DataFrame.
print(classlist_final.shape)
classlist_final


# In[16]:


# Import pandas
import pandas as pd

# Read CSV file from the current working directory.
transactions_2010 = pd.read_csv('transactions_2010.csv')

# View the DataFrame.
print(transactions_2010.shape)
transactions_2010.head()


# In[17]:


# Determine the length of the DataFrame.
print(len(transactions_2010))

# How many rows?
print(f"{transactions_2010.shape[0]} rows for transactions_2010")


# In[18]:


# Read the CSV file from the current working directory.
transactions_2011 = pd.read_csv('transactions_2011.csv')

# How many rows?
print(f"{transactions_2011.shape[0]} rows for transactions_2011")

# View the DataFrame.
print(transactions_2011.shape)
print(len(transactions_2011))
transactions_2011.head()


# In[19]:


# Combine the two DataFrames with the concat() function.
# The two DataFrames are transactions_2010 and transactions_2011.
transactions = pd.concat([transactions_2010, transactions_2011], axis=0)

# How many rows?
print(f"{transactions.shape[0]} rows for all transactions")

# View the DataFrame.
transactions.shape


# In[22]:


# Read the CSV file from the current working directory.
products = pd.read_csv('products.csv')

# Use the left join to merge the two DataFrames.
transactions_description = pd.merge(transactions, products, on='StockCode', how='left')

# View the new DataFrame.
transactions_description.head()


# In[25]:


# Read the CSV file from the current working directory.
customers = pd.read_csv('customers.csv')

# Use the left join to merge the two DataFrames.
transactions_description_country = pd.merge(transactions_description, customers,
                                          on = 'CustomerID', how='left')

# View the new DataFrame
transactions_description_country.head()


# In[26]:


# Group by syntax
df.groupby(by='None',
          axis = 0,
          level = 'None',
          as_index='True',
          sort='True',
          group_keys='True',
          squeeze='False')


# In[27]:


# import Pandas.
import pandas as pd

# Read the CSV files from the current working directory.
transactions_2010 = pd.read_csv('transactions_2010.csv')
transactions_2011 = pd.read_csv('transactions_2011.csv')
products = pd.read_csv('products.csv')
customers = pd.read_csv('customers.csv')

# Concatenate the two DataFrames: transactions_2010 and transactions_2011.
transactions = pd.concat([transactions_2010, transactions_2011], axis=0)
transactions.shape

# Use the left join to merge transactions_description with customers.
transactions_description = pd.merge(transactions, products, on='StockCode', how='left')

# Use the left join to merge transactions_description with customers.
transactions_description_country = pd.merge(transactions_description, customers, 
                                           on = 'CustomerID', how = 'left')

# View the DataFrame.
print(transactions_description_country.shape)
transactions_description_country.head()


# In[28]:


# Transaction total.
transactions_description_country['SaleTotal'] = transactions_description_country['Quantity'] * transactions_description_country['UnitPrice']

# Total sales by country.
transactions_description_country.groupby('Country')[['SaleTotal']].sum()


# In[29]:


# Total sales by country.
# The \ indicates a line break without interrupting the code snippet.
transactions_description_country.groupby('Country')[['SaleTotal']].sum().sort_values('SaleTotal', ascending=False)


# In[30]:


# Total and mean sales by country.
transactions_description_country.groupby('Country')[['SaleTotal']].agg(['sum','mean'])


# In[32]:


# Sort total and average sales by country.
transactions_description_country.groupby('Country')[['SaleTotal']].agg(['sum', 'mean']).sort_values([('SaleTotal', 'sum')], ascending=False)


# In[33]:


# Top selling product
transactions_description_country.groupby('Description')[['SaleTotal']].sum().sort_values('SaleTotal', ascending=False)


# In[35]:


# Import the libraries.
import pandas as pd
import numpy as np

# Read the CSV file from the current working directory.
transactions_2010 = pd.read_csv('transactions_2010.csv')

# View DataFrame.
print(transactions_2010.shape)

# Calculate the mean quantity and price.
transactions_2010[['Quantity', 'UnitPrice']].apply(np.mean)


# In[36]:


def calculator(a,b):
    print("Addtion:", a+b)
    print("Subtraction:", a-b)
    print("Multiplication:", a*b)
    print("Division", a/b)
    return;

calculator(25,5)


# In[37]:


# Write a user-defined function.
def f(x):
    y = (x * 2) + 10
    return y

# Stipulate what to calculate

f(x=3)


# In[38]:


# Read the CSV file from the current working directory.
products = pd.read_csv('products.csv')
# View the DataFrame.
products.shape


# In[39]:


# Create a user-defined function:
def contains_glass(x):
    """does the product contain glasss?"""
    y = x.lower()
    return "glass" in y

# View the output.
print(contains_glass(x="Glass bottle"))
print(contains_glass(x="glass bottle"))
print(contains_glass(x="bottle"))


# In[41]:


# Use the apply() function
fc = products['Description'].apply(contains_glass)
#View the DataFrame
print(fc)

products[fc]


# In[42]:


# lambda function practice

f = lambda x, y: x * y

f(5, 7)


# In[44]:


# Basic lambda example

example = lambda x: x * 2

example(10)


# In[45]:


# Basic lambda example: multiple arguments.
example_2 = lambda x, y, z: x * 2 + y - z
example_2 (5, 10, 15)


# In[46]:


# Create a list.
sequence = [10, 2, 8, 7, 5, 4, 3, 11, 0, 1]

# Lambda and filet function.
filter_answer = filter( lambda x: x > 6, sequence)

list(filter_answer)


# In[48]:


# Create a list.
sequence_2 = [10, 2, 8, 7, 5, 4, 11]

# Lambda and map function,
squared_result = map(lambda x: x*x, sequence_2)

list(squared_result)


# In[49]:


# Combine two values into one with lambda.
full_name = lambda fn, ln: fn.strip().title() + " " + ln.strip(). title()

full_name( "Vincent", "Van Gogh")


# In[ ]:




