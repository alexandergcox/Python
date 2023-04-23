#!/usr/bin/env python
# coding: utf-8

# ### LSE Data Analytics Online Career Accelerator 
# 
# # DA201:  Data Analytics with Python

# ## Filtering and sorting values (tutorial video)

# This file contains the code snippets that are introduced in the Filtering and sorting values video. Follow along with the demonstration to:
# - filter and sort data from a Series
# - filter and sort fata from a DataFrame.
# 
# Play and pause the video to follow along with the demonstration.
# 
# Note that the first two code blocks are from the on-page content: 'Preparing your workstation' and 'Mapping a series'.
# You will need to start following the demonstration from '3. Filter a Series'.

# ### 1. Prepare your workstation

# In[1]:


# Import the Pandas package.
import pandas as pd

# Create the data for the DataFrame
raw_data = {'Name': ['Thando Sinuka', 'Divya Patterson',
                     'Simon De Wit', 'Peter Black',
                     'Noncedo Dlamini', 'David Ackerman',
                     'Eugene du Toit', 'Amaira Patteri',
                     'Monica Le Blanc', 'Richard Fortress'],
            'Age':[29, 26, 25, 23, 30, 35, 25, 27, 24, 32],
            'Qualification': ['PhD', 'MSc', 'MBA', 'BSc',
                              'MCom', 'BCom', 'PhD', 'MBA', 
                              'MCom', 'BCom'],
            'Country': ['South Africa', 'Singapore', 'United Kingdom',
                        'Australia', 'Lesotho', 'United Kingdom',
                        'Canada', 'India', 'France', 'Canada']}

# Specify the row_labels.
row_labels = ['2021/0562/3215', '2021/2136/2132',
              '2021/0021/5987', '2021/3165/0468',
              '2021/0132/5496', '2021/3698/1346',
              '2021/0147/9632', '2021/6549/1324',
              '2021/9513/3579', '2021/3491/7916']

# Specify the column names.
students_updated = pd.DataFrame (raw_data,
                                 columns = ['Name', 'Age', 'Qualification',
                                            'Country', 'Test 1', 'Tutorial 1',
                                            'Test 2', 'Tutorial 2', 'Test 3',
                                            'Tutorial 3', 'Final mark', 'Pass'],

                                 # Specify index = row_labels
                                 index = row_labels)


students_updated ['Test 1'] = [82, 90, 75, 70, 88, 65, 72, 76, 85, 68]
students_updated ['Tutorial 1'] = [80, 75, 79, 69, 82, 68, 90, 84, 83, 79]

students_updated


# ### 2. Mapping a series

# In[4]:


# Students tutorial 2 mark.
students_updated ['Tutorial 2'] = [80, 75, 79, 69, 82, 68, 90, 84, 83, 79]

# Map method on tut 2.
# Create new series.
tut_2 = {80:80, 75:75, 79:76, 69:74, 82:80,
         68:75, 90:80, 84:84, 83:81, 79:80}

# Add new series to current DataFrame.
students_updated['tut_2'] = students_updated ['Tutorial 2'].map(tut_2)

# Reorder columns.
students_updated = students_updated [['Name', 'Age', 'Qualification', 
                                     'Country', 'Test 1', 'Tutorial 1',
                                     'Test 2', 'Tutorial 2', 'tut_2', 
                                     'Test 3', 'Tutorial 3', 'Final mark',
                                     'Pass']]

students_updated


# ### 3. Filter a Series

# In[2]:


# Create a class list with all the students. 
class_list = pd.Series(['Thando', 'Divya', 'Simon',
                  'Peter', 'Noncedo', 'David',
                  'Eugene', 'Amaira', 'Monica', 'Richard'],
            index=['2021/0562/3215', '2021/2136/2132',
                    '2021/0021/5987', '2021/3165/0468',
                  '2021/0132/5496', '2021/3698/1346',
                  '2021/0147/9632', '2021/6549/1324',
                    '2021/9513/3579', '2021/3491/7916'])

# Filter the Series for 'Divya' using the ! operator.
class_list [class_list != 'Divya']


# ### 4. Filter a column from a DataFrame

# In[5]:


# Filter columns Tutorial 2 and tut_2.
tuts_2 = students_updated [['Tutorial 2', 'tut_2']]

tuts_2


# ### 5. Filter rows from a DataFrame

# In[6]:


# Filter rows tut_2.
marks_adjusted = students_updated[students_updated['tut_2'] <80]

marks_adjusted


# ### 6. Sorting a Series with index

# In[7]:


# Sort index.
# Ascending order is default.
class_list.sort_index()


# In[8]:


# Sort index in descending order.
class_list.sort_index(ascending=False)


# ### 7. Sorting a single column

# In[9]:


# Sorting the Name column using the sort_values() method. 
# Ascending order, or A to Z, is default.
students_updated.sort_values(by=['Name'], inplace=True)

students_updated


# ### 8. Sorting by multiple columns

# In[10]:


# Sorting the Test 1 and Tutorial 1 columns using the sort_values() method. 
students_updated.sort_values(by=['Test 1', 'Tutorial 1'], inplace=True)

students_updated


# In[ ]:




