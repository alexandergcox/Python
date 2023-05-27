#!/usr/bin/env python
# coding: utf-8

# ### LSE Data Analytics Online Career Accelerator
# 
# # DA201: Data Analytics using Python

# # Practical activity: Preparing quantitative data

# **This is the solution to the practical activity**
# 
# A real estate developer, Derek, is planning to start a new project to build family homes. He has access to historical data for the region in which he acquired land for the project. The historical data includes the prices of houses sold in the area over a 10-year period. The data also includes information about the number of bedrooms in each house ranging from one to five. Derek has asked you to analyse the data for any trends that might be evident. He wants to know the optimal number of bedrooms to maximise profit for the project.
# 
# In this activity we will: 
# 
# - set up the workspace
# - get to know the data
# - define sub-data sets
# - detect outliers
# - remove outliers.

# ## Prepare your workstation

# In[1]:


# Import necessary libraries.
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()

from sklearn.metrics import r2_score, median_absolute_error, mean_absolute_error
from sklearn.metrics import median_absolute_error, mean_squared_error, mean_squared_log_error

import warnings
warnings.filterwarnings('ignore')

get_ipython().run_line_magic('matplotlib', 'inline')

## Get multiple outputs in the same cell.
from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = 'all'


# In[3]:


# Simple hacks to make plots look better: 

# Colour palette to make charts look better.
blue, = sns.color_palette("muted", 1) 

# Dark grid, white grid, dark, white, and ticks.
sns.set_style('whitegrid') 

# Font size of the axes titles.
plt.rc('axes', titlesize=18) 

# Font size of the x and y labels.
plt.rc('axes', labelsize=14)    

# Font size of the tick labels.
plt.rc('xtick', labelsize=13,color='#4f4e4e') 

# Font size of the tick labels.
plt.rc('ytick', labelsize=13,color='#4f4e4e')  

# Font size of the legend.
plt.rc('legend', fontsize=13)

# Default text size.
plt.rc('font', size=13)          


# In[4]:


# Import CSV file with Pandas.
data = pd.read_csv('raw_sales.csv', index_col=['datesold'], parse_dates=['datesold'])

# View DataFrame.
print(data.shape)
data.head()


# ## Get to know the data

# In[5]:


# Plot house prices as time series.
data.plot(figsize=(12, 4))
plt.legend(loc='best')
plt.title("Housing Prices")
plt.show(block=False);

# Check for missing values.
data.isna().sum()


# ## Checking the data set for the count of houses based on their bedrooms

# In[6]:


# Count the number of values in a specified column of the DataFrame.
print(data['bedrooms'].value_counts())

# Create a plot.
plt.title("Count of number of bedrooms")

sns.despine(left=True);
sns.countplot(x='bedrooms', data=data)


# ## Creating different data sets based on number of bedrooms

# In[7]:


# Create a copy of the original data for convenience. 
data_sub = data.copy()


# Data set consisting of houses with 1 bedroom: 
df_1 = data_sub[data_sub['bedrooms']==1]
print(df_1.shape)


# Data set consisting of houses with 2 bedrooms: 
df_2 = data_sub[data_sub['bedrooms']==2]
print(df_2.shape)


# Data set consisting of houses with 3 bedrooms: 
df_3 = data_sub[data_sub['bedrooms']==3]
print(df_3.shape)


# Data set consisting of houses with 4 bedrooms: 
df_4 = data_sub[data_sub['bedrooms']==4]
print(df_4.shape)


# Data set consisting of houses with 5 bedrooms: 
df_5 = data_sub[data_sub['bedrooms']==5]
print(df_5.shape)


# ## Detect outliers

# In[8]:


# Set plot size.
fig, axes = plt.subplots(nrows=3, ncols=2,figsize=(20, 20))

# 1 bedroom:
axes[0][0].hist(df_1['price'])
axes[0][0].title.set_text("1 bedroom price histogram")

# 2 bedrooms:
axes[0][1].hist(df_2['price'])
axes[0][1].title.set_text("2 bedroom price histogram")

# 3 bedrooms:
axes[1][0].hist(df_3['price'])
axes[1][0].title.set_text("3 bedroom price histogram")

# 4 bedrooms:
axes[1][1].hist(df_4['price'])
axes[1][1].title.set_text("4 bedroom price histogram")

# 5 bedrooms:
axes[2][0].hist(df_5['price'])
axes[2][0].title.set_text("5 bedroom price histogram")


fig.delaxes(axes[2][1])

plt.show()


# In[9]:


# Create a box plot for 1 bedroom.
# Set figure size.
fig = plt.figure(figsize=(18, 4))

# Create box plot.
ax = sns.boxplot(x=df_1['price'], whis=1.5)


# ## Remove outliers

# In[10]:


# The columns you want to search for outliers in.
cols = ['price'] 

# Calculate quantiles and IQR.
# Same as np.percentile but maps (0,1) and not (0,100).
Q1 = df_1[cols].quantile(0.25) 
Q3 = df_1[cols].quantile(0.75)
IQR = Q3 - Q1
IQR

# Return a boolean array of the rows with (any) non-outlier column values.
condition = ~((df_1[cols] < (Q1 - 1.5 * IQR)) | (df_1[cols] > (Q3 + 1.5 * IQR))).any(axis=1)

# Filter DataFrame based on condition.
df_1_non_outlier = df_1[condition]
df_1_non_outlier.shape


# In[11]:


# Plot to see if outliers have been removed: 
# whis = multiplicative factor
fig = plt.subplots(figsize=(12, 2))

ax = sns.boxplot(x=df_1_non_outlier['price'], whis=1.5)


# ## Additional code

# ### Data set with 2 bedrooms (`df_2`)

# In[12]:


# whis = multiplicative factor
fig = plt.subplots(figsize=(12, 2))
ax = sns.boxplot(x=df_2['price'], whis=1.5);


# In[13]:


# Histogram plot.
fig = df_2.price.hist(figsize = (12, 4))


# In[14]:


# Outlier removal from houses with 2 bedrooms.
# The columns you want to search for outliers in.
cols = ['price']

# Calculate quantiles and IQR.
# Same as np.percentile but maps (0,1) and not (0,100).
Q1 = df_2[cols].quantile(0.25)
Q3 = df_2[cols].quantile(0.75)
IQR = Q3 - Q1
IQR

# Return a boolean array of the rows with (any) non-outlier column values.
condition = ~((df_2[cols] < (Q1 - 1.5 * IQR)) | (df_2[cols] > (Q3 + 1.5 * IQR))).any(axis=1)

# Filter DataFrame based on condition.
df_2_non_outlier = df_2[condition]
df_2_non_outlier.shape


# In[15]:


# Plot to see if outliers have been removed: 
# whis = multiplicative factor
fig = plt.subplots(figsize=(12, 2))

ax = sns.boxplot(x=df_2_non_outlier['price'],whis=1.5);


# ### Data set with 3 bedrooms (`df_3`)

# In[16]:


# whis = multiplicative factor
fig = plt.subplots(figsize=(12, 2))

ax = sns.boxplot(x=df_3['price'], whis=1.5);


# In[17]:


# Histogram plot.
fig = df_3.price.hist(figsize = (12, 4))


# In[18]:


# Removing outliers from data set with 3 bedrooms: 
# The columns you want to search for outliers in.
cols = ['price'] 

# Calculate quantiles and IQR.
# Same as np.percentile but maps (0,1) and not (0,100).
Q1 = df_3[cols].quantile(0.25)
Q3 = df_3[cols].quantile(0.75)
IQR = Q3 - Q1
IQR

# Return a boolean array of the rows with (any) non-outlier column values.
condition = ~((df_3[cols] < (Q1 - 1.5 * IQR)) | (df_3[cols] > (Q3 + 1.5 * IQR))).any(axis=1)

# Filter DataFrame based on condition.
df_3_non_outlier = df_3[condition]
df_3_non_outlier.shape


# In[19]:


# Plot to see if outliers have been removed: 
# whis = multiplicative factor
fig = plt.subplots(figsize=(12, 2))

ax = sns.boxplot(x=df_3_non_outlier['price'],whis=1.5)


# ### Data set with 4 bedrooms (df_4)

# In[20]:


# whis = multiplicative factor
import seaborn as sns
fig = plt.subplots(figsize=(12, 2))

ax = sns.boxplot(x=df_4['price'], whis=1.5);


# In[21]:


# Histogram plot.
fig = df_4.price.hist(figsize = (12, 4))


# In[22]:


# Removing outliers from data set with 4 bedrooms.
# The columns you want to search for outliers.
cols = ['price'] 

# Calculate quantiles and IQR.
# Same as np.percentile but maps (0,1) and not (0,100).
Q1 = df_4[cols].quantile(0.25) 
Q3 = df_4[cols].quantile(0.75)
IQR = Q3 - Q1
IQR

# Return a boolean array of the rows with (any) non-outlier column values.
condition = ~((df_4[cols] < (Q1 - 1.5 * IQR)) | (df_4[cols] > (Q3 + 1.5 * IQR))).any(axis=1)

# Filter our DataFrame based on condition.
df_4_non_outlier = df_4[condition]
df_4_non_outlier.shape


# In[23]:


# Plot to see if outliers have been removed: 
# whis = multiplicative factor
fig = plt.subplots(figsize=(12, 2))

ax = sns.boxplot(x=df_4_non_outlier['price'], whis=1.5);


# ### Data set with 5 bedrooms (`df_5`)

# In[24]:


# whis = multiplicative factor
fig = plt.subplots(figsize=(12, 2))

ax = sns.boxplot(x=df_5['price'], whis=1.5)


# In[25]:


# Histogram plot.
fig = df_5.price.hist(figsize = (12, 4))


# In[26]:


# Removing outliers from data set with 5 bedrooms: 
# The columns you want to search for outliers in.
cols = ['price'] 

# Calculate quantiles and IQR.
# Same as np.percentile but maps (0,1) and not (0,100).
Q1 = df_5[cols].quantile(0.25) 
Q3 = df_5[cols].quantile(0.75)
IQR = Q3 - Q1
IQR

# Return a boolean array of the rows with (any) non-outlier column values.
condition = ~((df_5[cols] < (Q1 - 1.5 * IQR)) | (df_5[cols] > (Q3 + 1.5 * IQR))).any(axis=1)

# Filter DataFrame based on condition.
df_5_non_outlier = df_5[condition]
df_5_non_outlier.shape


# In[27]:


# Plot to see if outliers have been removed: 
fig = plt.subplots(figsize=(12, 2))

ax = sns.boxplot(x=df_5_non_outlier['price'], whis=1.5)


# In[ ]:




