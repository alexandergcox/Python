#!/usr/bin/env python
# coding: utf-8

# ### LSE Data Analytics Online Career Accelerator
# 
# # DA201: Data Analytics using Python

# # Time-series forecasting (tutorial video)

# This Jupyter Notebook is based on the time-series forecasting with Python tutorial video. Watch the video to explore time series forecasting with the simple moving average method in Python. In the video, you will explore:
# 
# - what a simple moving average is
# - how to calculate a simple moving average
# - how to calculate a simple moving average data set.

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
InteractiveShell.ast_node_interactivity = "all"


# In[2]:


# Simple hacks to make plots look better: 
# # Colour palette to make charts look better.
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

# Font size of the Legend.
plt.rc('legend', fontsize=13)

# Default text size.
plt.rc('font', size=13)          


# In[3]:


# Import CSV file with Pandas.
data = pd.read_csv('raw_sales.csv', index_col=['datesold'], parse_dates=['datesold'])

# View DataFrame.
print(data.shape)
data.head()


# In[4]:


# Creating a copy of the original data for convenience: 
data_sub = data.copy()

# Data set consisting of houses with 5 bedrooms: 
df_5 = data_sub[data_sub['bedrooms'] == 5]

# View output.
df_5.head


# In[5]:


# Determine outliers for 5 bedrooms.
# whis = multiplicative factor
import seaborn as sns

fig = plt.subplots(figsize=(12, 2))
ax = sns.boxplot(x=df_5['price'], whis=1.5);


# In[6]:


# Histogram of data set (5 bedrooms only).
fig = df_5.price.hist(figsize = (12, 4))


# In[7]:


# Outlier removal:
# Removing outliers from data set with 2 bedrooms:
# The columns you want to search for outliers in.
cols = ['price'] 

# Calculate quantiles and IQR.
# Same as np.percentile but maps (0,1) and not (0,100).
Q1 = df_5[cols].quantile(0.25) 
Q3 = df_5[cols].quantile(0.75)
IQR = Q3 - Q1
IQR

# # Return a boolean array of the rows with (any) non-outlier column values.
condition = ~((df_5[cols] < (Q1 - 1.5 * IQR)) | (df_5[cols] > (Q3 + 1.5 * IQR))).any(axis=1)

# Filter the DataFrame based on a condition.
df_5_non_outlier = df_5[condition]
df_5_non_outlier.shape


# In[8]:


# Plot to see if outliers have been removed: 
# whis = multiplicative factor
fig = plt.subplots(figsize=(12, 2))
ax = sns.boxplot(x=df_5_non_outlier['price'], whis=1.5);


# In[9]:


# Plotting the time-series data.
df_5_non_outlier.plot(figsize=(12, 4))
plt.legend(loc='best')
plt.title("Time-series plot for house with 5 bedrooms")
plt.show(block=False);


# In[10]:


# Resampling data set with 5 bedrooms: 
df_5_res = df_5_non_outlier.resample('M').mean()

# View the DataFrame.
df_5_res.head()


# In[11]:


# Dropping the missing values: 
df_5_res.dropna(inplace= True)

df_5_res.isna().sum()


# In[12]:


# Plotting the time-series data.
df_5_res.plot(figsize=(12, 4))
plt.legend(loc='best')
plt.title("Time-series plot after resampling")
plt.show(block=False);


# # 

# ## Calculate the Simple Moving Average (SMA) for houses with 5 bedrooms

# In[13]:


# This is a function to calculate and plot the simple moving average: 
def plot_moving_average(series, window, plot_intervals=False, scale=1.96):

    rolling_mean = series.rolling(window=window).mean()
    
    plt.figure(figsize=(12,4))
    plt.title("Moving average\n window size = {}".format(window))
    plt.plot(rolling_mean, 'g', label='Simple moving average trend')
    
    # Plot confidence intervals for smoothed values.
    if plot_intervals:
        mae = mean_absolute_error(series[window:], rolling_mean[window:])
        deviation = np.std(series[window:] - rolling_mean[window:])
        lower_bound = rolling_mean - (mae + scale * deviation)
        upper_bound = rolling_mean + (mae + scale * deviation)
        plt.plot(upper_bound, 'r--', label='Upper bound / Lower bound')
        plt.plot(lower_bound, 'r--')
            
    plt.plot(series[window:], label="Actual values")
    plt.legend(loc='best')
    plt.grid(True)


# In[14]:


# Calculate SMA for a window size of 5.
df_5_res['SMA_5'] = df_5_res.iloc[:, 1].rolling(window=5).mean()

# Print the first 15 rows of data.
print(df_5_res.head(15))


# In[15]:


# Smooth by the previous 5 days.
plot_moving_average(df_5_res.price, 5, plot_intervals=True)


# In[16]:


# Calculate SMA for a window size of 5.
df_5_res['SMA_30'] = df_5_res.iloc[:, 1].rolling(window=30).mean()

# Calculate SMA for a window size of 5.
df_5_res['SMA_90'] = df_5_res.iloc[:, 1].rolling(window=90).mean()

# Print the first 100 rows of data.
print(df_5_res.head(100))


# In[17]:


# Smooth by the previous month (30 days).
plot_moving_average(df_5_res.price, 30, plot_intervals=True)


# In[18]:


# Smooth by the previous quarter (90 days).
plot_moving_average(df_5_res.price, 90, plot_intervals=True)


# In[ ]:




