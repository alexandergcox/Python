#!/usr/bin/env python
# coding: utf-8

# ### LSE Data Analytics Online Career Accelerator
# 
# # DA201: Data Analytics using Python

# ## Week 2: Getting started with Pandas demonstrations

# The focus this week is on introducing, setting up, and exploring Pandas. You will use this Notebook to follow along with the demonstrations throughout the week.
# 
# Learn about using your Jupyter Notebook here: https://jupyter-notebook.readthedocs.io/en/latest/ui_components.html
# 
# This is your Notebook. Use it to follow along with the demonstrations, test ideas and explore what is possible. The hands-on experience of writing your own code will accelerate your learning!

# ### 2.1 Data ingestion with Pandas

# In[1]:


# import Pandas library
import pandas as pd


# In[2]:


# create the variable colours
# Pass an array of data
colours = pd.Series(['green', 'red', 'yellow', 'blue', 'black', 'white'])

# Print the series.
print(colours)


# In[3]:


# Create a list
example_list = [1, 2, 3, 4, 5, 6]

# Create series from a list.
numbers = pd.Series(example_list)

# Print the series.
print(numbers)


# In[4]:


# Create a dictionary.
# Specify the dictionary as dict_1.
dict_1 = {'AU' : 'Australian Dollar',
         'US': 'US Dollar',
         'IN' : 'Indian Rupee',
         'DK' : 'Danish Krone',
         'SW' : 'Swiss Franc'}

# Name and create the series.
economics = pd.Series(dict_1)

# Print the series.
print(economics)


# In[5]:


# Emergency numbers: Law Enforcement (123), Fire and Rescue Service (224), 
# Emergency Medical Services (101), Emergency Management (999), and public works (900)

# create a dictionary
dict_1 = {'123' : 'Law Enforcement',
         '224' : 'Fire and rescue services',
         '101' : 'Emergency medical services',
          '999' : 'Emergency management',
          '900' : 'Public works',}

# create series
emergency_numbers = pd.Series(dict_1)

print(emergency_numbers)


# In[6]:


# Emergency protocols : Prvention, mitigation, preparedness, response, and recovery

# Create a numbered list
emergency_protocols = pd.Series(['Prevention', 'Mitigation', 'Preparedness', 'Response', 'Recovery'],
                               index= ['1', '2', '2', '4', '5'])

print(emergency_protocols)


# In[7]:


# Emergency checklistL check pulse (neck), breathing(nose),
# Obstructions (nose, ears, mouth), pupils (responsive), 
# consciousness, contact details, and allergies.

# Create a series from a list
checklist = ['Check carotid pulse (neck)', 'Check breathing (nose)',
            'Check for obstructions (nose, ears, mouth)',
            'Check pupils (responsive)', 'Consciousness',
            'Contact Details', 'Any allergies']

emergency_checklist = pd.Series(checklist)

print(emergency_checklist)


# In[8]:


# import pandas
import pandas as pd

# create a DataFrame from a dictionary
data = {'Name' : ['Shen Lee', 'Leon Buhle', 'Tracy Adams',
                 'Lebo Sinuka', 'Lauren Pierce', 'Monika Bond', 
                 'Natahs Allsopp', 'Nicholes Winter', 
                 'Christopher Eckson', 'Siobhan OMalley'],
       'Annual' : [23, 20, 15, 19, 21, 21, 10, 15, 16, 23],
       'Sick' : [10, 8, 10, 9, 7 ,10, 9, 10, 8, 5],
       'Personal' : [5, 4, 5, 0, 5, 2, 5, 4, 2, 5],
       'Bonus' : [3, 0, 0, 3, 3, 6, 0, 3, 6, 3]}
row_labels = [215, 216, 217, 218, 219, 220, 221, 222, 223, 224]
leave_cycle = pd.DataFrame(data, columns = ['Name', 'Annual', 'Sick', 'Personal', 'Bonus'],
                          index = row_labels)
leave_cycle.index.name = 'Personnel_ID'

leave_cycle


# In[14]:


# import pandas
import pandas as pd

# create a DataFrame from a dictionary
data = {'Name' : ['Shen Lee', 'Leon Buhle', 'Tracy Adams',
                 'Lebo Sinuka', 'Lauren Pierce', 'Monika Bond', 
                 'Natahs Allsopp', 'Nicholes Winter', 
                 'Christopher Eckson', 'Siobhan OMalley'],
       'Annual' : [23, 20, 15, 19, 21, 21, 10, 15, 16, 23],
       'Sick' : [10, 8, 10, 9, 7 ,10, 9, 10, 8, 5],
       'Personal' : [5, 4, 5, 0, 5, 2, 5, 4, 2, 5],
       'Bonus' : [3, 0, 0, 3, 3, 6, 0, 3, 6, 3],
       'Total Leave taken' : [0, 3, 5, 10, 5, 8, 11, 9, 15, 5],
       'Total leave available' : [38, 32, 30, 28, 33, 33, 24, 29, 26, 33],
       'Annual total' : [38, 35, 35, 38, 38, 41, 35, 38, 41, 38]}

row_labels = [215, 216, 217, 218, 219, 220, 221, 222, 223, 224]
leave_cycle = pd.DataFrame(data, columns = ['Name', 'Annual', 'Sick', 'Personal', 'Bonus', 
                                            'Total leave taken', 'Total leave available', 'Annual total'],
                          index = row_labels)
leave_cycle.index.name = 'Personnel_ID'

leave_cycle


# In[15]:


# Import pandas
import pandas as pd

# Read the CSV file
# Assign a variable.
# Use the pd.read_csv() function.
# Specify the name fo the CSV file
fitness = pd.read_csv('daily_activity.csv')

# Print the DataFrame.
fitness


# In[16]:


# Import package.
import pandas as pd

# Read the CSV file.
fitness = pd.read_csv('daily_activity.csv')

print(fitness.shape)
print(fitness.dtypes)


# In[17]:


# View data in the DataFrame.
# Instead of 5, we can use any integer.
print(fitness.head())

# View the last 5 rows.
print(fitness.tail())


# In[19]:


# View data in the DataFrame.
# Instead of 5, we can use any integer.
fitness.head()

# View the last 5 rows.
fitness.tail()


# In[20]:


# Print the entire DataFrame.
print(fitness)


# In[21]:


# Import the Pandas library.
import pandas as pd

# Read the csv from the current working directory.
# Specify that there is no header in the data set using header=None.
fitness = pd.read_csv('daily_activity.csv', header=None)

# View the DataFrame.
fitness


# In[22]:


# Specify that header should be col_names (alphabetic letters).
col_names = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o']

# Read the CSV file.
fitness = pd.read_csv('daily_activity.csv', names=col_names)

# View the DataFrame.
fitness


# In[23]:


# Rename the index column to observation.
fitness.index.names = ['observation']

# View the DataFrame.
fitness


# In[24]:


# Create a hierarchical index.
col_names2 = ['I1', 'I2', 'c', 'd', 'e', 'f', 'g',
             'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o']

# Read the CSV file.
fitness = pd.read_csv('daily_activity.csv', names=col_names2,
                     index_col=['I1','I2'])

# View the DataFrame
fitness


# In[25]:


# Skip specific rows.
fitness = pd.read_csv('daily_activity.csv', skiprows =[0, 1, 2, 5, 10])

# View the DataFrame.
fitness


# In[26]:


# Skip specific rows.
fitness = pd.read_csv('daily_activity.csv', skiprows =[1, 2, 5, 10])

# View the DataFrame.
fitness


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# # 

# ### 2.2 Pandas built-in functions

# In[1]:


# Import package
import pandas as pd

# Read CSV file from the current working directory.
fitness = pd.read_csv('daily_activity.csv')

fitness


# In[2]:


#  Use the head() function to subset data set.
fitness.head()


# In[3]:


# Option 1
my_list = fitness.columns.values.tolist()

print(my_list)


# In[4]:


# Option 2 
my_list = list(fitness)

my_list


# In[6]:


# Selecting few columns,
fitness_fcol = pd.read_csv('daily_activity.csv',
                          usecols=['Id', 'ActivityDate', 'TotalSteps'])

# Print DataFrame.
fitness_fcol.head()


# In[7]:


# Only return the first 10 rows.
fitness_nrows = pd.read_csv('daily_activity.csv', nrows=10)

# Print the DataFrame
fitness_nrows


# In[8]:


# Shape of data frame.
print(fitness.shape)

# Skiprows parameter.
fitness_skiprows = pd.read_csv('daily_activity.csv', skiprows = 500)

# Print the DataFrame.
print(fitness_skiprows.shape)


# In[9]:


# Prepare workstation
import pandas as pd

# Read CSV file from the current working directory.
fitness = pd.read_csv('daily_activity.csv')

# Column names of data set.
my_list = fitness.columns.values.tolist()

my_list


# In[11]:


# Add cloumn cal-Cat to calculate the middle number of calories.
fitness['cal-cat'] = fitness['Calories'] - fitness['Calories'].mean()

# Sense check values of cal_cat column.
print(fitness['cal_cat'])

# Print to sense check column was added.
print(fitness.head())


# In[ ]:


# Sort column from low to high to determine.
print(fitness['cal_cat'].sort_values())

# Determine min value (statistical method).
print(fitness['cal_cat'].min())


# In[12]:


# Import package.
import pandas as pd
#Read CSV files from the current working directory.
fitness_raw = pd.read_csv('daily_activity_raw.csv')

#View the DataFrame.
fitness_raw_head()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# # 

# ### 2.3 Analysing data in Pandas

# In[1]:


# Importing Pandas package
import pandas as pd

# Create series with explicit labelling.
class_list = pd.Series(['Thando', 'Divya', 'Simon', 'Peter', 'Noncedo', 'David',
                       'Eugene', 'Amaira', 'Monica', 'Richard'],
                      index = ['2021/0562/3215', '2021/2136/2132', '2021/0021/5987', 
                              '2021/3165/0468', '2021/0132/5496', '2021/3698/1346',
                              '2021/0147/9632', '2021/6549/1324', '2021/9513/3579',
                              '2021/3491/7916'])
class_list


# In[2]:


# Determine the values.
print(class_list.values)

# Determine the index.
print(class_list.index)


# In[3]:


# Retrieve values with an index.
class_list['2021/2136/2132']


# In[4]:


# Separate with comma.
print(class_list ['2021/2136/2132'], class_list ['2021/3165/0468'],
     class_list ['2021/3491/7916'])

# Write as one code snippet.
print(class_list[['2021/2136/2132', '2021/3165/0468', '2021/3491/7916']])


# In[5]:


# Create a dictionary
# Import Pandas if it is a new session.
import pandas as pd

raw_data = {'Name': ['Thando Sinuka', 'Divya Patterson',
                    'Simon de Wit', 'Peter Black',
                    'Noncedom Dlamini', 'David Ackerman',
                    'Eugene du Toit', 'Amaira Patteri',
                    'Monica Le Blanc', 'Richard Fortress'],
           'Age' : [29, 26, 25, 23, 30, 35, 25, 27, 24, 32],
           'Qualification' : ['PhD', 'MSc', 'MBA', 'BSc', 
                             'MCom', 'BCom', 'PhD', 'MBA', 
                             'MCom', 'BCom'],
           'Country' : ['South Africa', 'Singapore', 'United Kingdom', 
                       'Australia', 'Lesotho', 'United Kingdom', 
                       'Canada', 'India', 'France', 'Canada']}

students = pd.DataFrame(raw_data)

students


# In[7]:


raw_data = {'Name': ['Thando Sinuka', 'Divya Patterson',
                    'Simon de Wit', 'Peter Black',
                    'Noncedom Dlamini', 'David Ackerman',
                    'Eugene du Toit', 'Amaira Patteri',
                    'Monica Le Blanc', 'Richard Fortress'],
           'Age' : [29, 26, 25, 23, 30, 35, 25, 27, 24, 32],
           'Qualification' : ['PhD', 'MSc', 'MBA', 'BSc', 
                             'MCom', 'BCom', 'PhD', 'MBA', 
                             'MCom', 'BCom'],
           'Country' : ['South Africa', 'Singapore', 'United Kingdom', 
                       'Australia', 'Lesotho', 'United Kingdom', 
                       'Canada', 'India', 'France', 'Canada']}

# Specify the row labels.
row_labels = ['2021/0562/3215', '2021/2136/2132', '2021/0021/5987', '2021/3165/0468',
       '2021/0132/5496', '2021/3698/1346', '2021/0147/9632', '2021/6549/1324',
       '2021/9513/3579', '2021/3491/7916']

# Specify the column names.
students_updated = pd.DataFrame (raw_data,
                                columns = ['Name', 'Age', 'Qualification', 
                                          'Country', 'Test 1', 'Tutorial 1',
                                          'Test 2', 'Tutorial 2', 'Test 3',
                                          'Tutorial 3', 'Final mark', 'Pass'],
                                
                                # Specify index = row_labels
                                index = row_labels)

students_updated


# In[9]:


# All the students the same mark.
students_updated ['Test 1'] = 80

students_updated


# In[10]:


# Students have different marks.
students_updated ['Test 1'] = [82, 90, 75, 70, 88, 65, 72, 76, 85, 68]

students_updated


# In[11]:


# Add tutorial marks
students_updated ['Tutorial 1'] = [80,75, 79, 69, 82, 68, 90, 84, 83, 79]

students_updated


# In[12]:


# Retrieve selected columns and rows
print(students_updated[['Test 1', 'Tutorial 1']])


# In[13]:


print(students_updated.iloc[:,4:6])


# In[14]:


print(students_updated.loc['2021/2136/2132'])


# In[15]:


Divya = students_updated.iloc[1]
print(Divya)


# In[18]:


raw_data = {'Name': ['Thando Sinuka', 'Divya Patterson',
                    'Simon de Wit', 'Peter Black',
                    'Noncedom Dlamini', 'David Ackerman',
                    'Eugene du Toit', 'Amaira Patteri',
                    'Monica Le Blanc', 'Richard Fortress'],
           'Age' : [29, 26, 25, 23, 30, 35, 25, 27, 24, 32],
           'Qualification' : ['PhD', 'MSc', 'MBA', 'BSc', 
                             'MCom', 'BCom', 'PhD', 'MBA', 
                             'MCom', 'BCom'],
           'Country' : ['South Africa', 'Singapore', 'United Kingdom', 
                       'Australia', 'Lesotho', 'United Kingdom', 
                       'Canada', 'India', 'France', 'Canada']}

# Specify the row labels.
row_labels = ['2021/0562/3215', '2021/2136/2132', '2021/0021/5987', '2021/3165/0468',
       '2021/0132/5496', '2021/3698/1346', '2021/0147/9632', '2021/6549/1324',
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


# In[19]:


# Students tut 2 mark.
students_updated ['Tutorial 2'] = [80, 75, 79, 69, 82, 68, 90, 84, 83, 79]

# Map method on tut 2.
# Create new Series.
tut_2 = {80:80, 75:75, 79:76, 69:74, 82:80, 
        68:75, 90:80, 84:84, 83:81, 79:80}

# Add new series to current DataFrame.
students_updated['tut_2'] = students_updated ['Tutorial 2'].map(tut_2)

# Reorder columns.
students_updated = students_updated[['Name', 'Age', 'Qualification',
                                    'Country', 'Test 1', 'Tutorial 1',
                                    'Test 2', 'Tutorial 2', 'tut_2',
                                    'Test 3', 'Tutorial 3', 'Final mark',
                                    'Pass']]

students_updated


# In[1]:


# import workstation
import pandas as pd

# Read CSV file from current working directory.
fitness = pd.read_csv('daily_activity.csv')

print(fitness.shape)

# Desciptive statistics.
fitness.describe()


# In[2]:


# max = Returns max of a column
print(fitness['TotalDistance'].max())

# min = Returns min of a column
print(fitness['TotalDistance'].min())

# sum = Returns sum of a column
print(fitness['TotalDistance'].sum())


# 

# In[3]:


q1 = fitness['TotalSteps'].quantile(0.25)
q3 = fitness['TotalSteps'].quantile(0.75)

iqr_TotalSteps = q3 - q1

iqr_TotalSteps


# In[4]:


# Variance of the DataFrame.
print(fitness.var())

# Variance of total distance.
print(fitness['TotalDistance'].var())


# # 
