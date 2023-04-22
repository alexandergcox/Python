#!/usr/bin/env python
# coding: utf-8

# ### LSE Data Analytics Online Career Accelerator
# 
# # DA201: Data Analytics using Python

# ## Practical activity: Pandas Series

# **This is the solution to the activity.**
# 
# Create flashcards for training purposes on best practices and ‘what to do’ scenarios, use Pandas Series to create these flashcards. Use the information provided by HR:

# `RAW DATA`
# 
# - Emergency numbers: Law Enforcement (123), Fire and Rescue Services (224), Emergency Medical Services (101), Emergency Management (999), and Public Works (900).
# - Emergency protocols: Prevention, mitigation, preparedness, response, and recovery.
# - Emergency checklist: Check pulse (neck), breathing (nose), obstructions (nose, ears, mouth), pupils (responsive), consciousness, contact details, and allergies.

# ### 1. List of emergency number

# In[ ]:


# Emergency numbers: Law Enforcement (123), Fire and Rescue Services (224), 
# Emergency Medical Services (101), Emergency Management (999), and Public Works (900).

# Import the library
import pandas as pd

# Create a dictionary
dict_1 = {'123': 'Law Endorcement',
          '224': 'Fire and Rescue Service',
          '101': 'Emergency Meducal Service',
          '999': 'Emergency Management',
          '900': 'Public Works'}

# Create a Series 
emergency_numbers = pd.Series(dict_1)

# View the result by passing or calling the print() function
print(emergency_numbers)


# # 

# ### 2. List of emergency protocols

# In[ ]:


# Emergency protocols: Prevention, mitigation, preparedness, response, and recovery.

# Create a numbered list
emergency_protocols = pd.Series(['Prevention', 'Mitigation',
                                 'Preparedness', 'Response', 
                                 'Recovery'],
                                index = ['1', '2', '3', '4', '5'])

# View the DataFrame
print(emergency_protocols)


# # 

# ### 3. Checklist for patients arriving at the emergency entrance

# In[ ]:


# Emergency checklist: Check pulse (neck), breathing (nose), 
# obstructions (nose, ears, mouth), pupils (responsive), 
# consciousness, contact details, and allergies.

# Create a Series from a list
checklist = ['Check carotid pulse (neck)', 'Check breathing (nose)',
             'Check for obstructions (nose, ears, mouth)', 
             'Check pupils (responsive)', 'Consciousness',
             'Contact details', 'Any allergies']

emergency_checklist = pd.Series(checklist)

# View the DataFrame
print(emergency_checklist)


# In[ ]:




