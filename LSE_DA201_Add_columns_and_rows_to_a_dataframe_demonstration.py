#!/usr/bin/env python
# coding: utf-8

# ### LSE Data Analytics Online Career Accelerator 
# 
# # DA201:  Data Analytics with Python

# ## Adding columns and rows to a DataFrame (tutorial video)

# This file contains the code snippets that are introduced in the Adding columns and rows to a DataFrame video. 
# Follow along with the demonstration to:
# - add columns to a Dataframe
# - add rows to a DataFrame.
# 
# Play and pause the video to follow along with the demonstration.

# ### 1. Import packages and create a DataFrame

# In[ ]:


# Import packages.
import pandas as pd


# In[1]:


# Create a dictionary to hold the student data.
data = {'Name': ['Thando', 'Divya', 'Simon', 'Peter'],
        'Country': ['South Africa', 'Singapore', 'United Kingdom', 'Australia'],
        'Qualification': ['Phd', 'Diploma', 'BSc', 'MBA'],
        'Age': [29, 20, 25, 23]}

# Create a DataFrame from the dictionary.
students = pd.DataFrame(data)

# View the DataFrame
students


# ### 2. Reorder and add a column

# In[ ]:


# Re-order the columns.
students = pd.DataFrame(data, columns=['Name', 'Age', 'Qualification', 'Country'])

students


# In[2]:


# Add a column (Final mark).
students = pd.DataFrame(data, columns=['Name', 'Age', 'Qualification', 'Country', 'Final mark'])

students


# ### 3. Add new rows

# In[ ]:


# Create a new DataFrame with new data.
# Create a dictionary to hold the new student information.
new_data = {'Name': ['Noncedo', 'David', 'Eugene', 'Amaira', 'Monica', 'Richard'],
            'Age': [22, 23, 25, 24, 26, 22],
            'Qualification':['Diploma', 'BCom', 'Diploma', 'MCom', 'Phd', 'BCom'],
            'Country': ['Lesotho', 'United Kingdom', 'Australia', 'India', 'Poland', 'Germany']}

# Create a DataFrame from the dictionary.
students_2 = pd.DataFrame(new_data)

students_2


# In[ ]:


# Add rows with the append() function.
students_final = students.append(students_2, ignore_index=True)

students_final


# In[ ]:


# Add rows with the concat() function.
students_concat = pd.concat([students, students_2], ignore_index=True)

students_concat

