#!/usr/bin/env python
# coding: utf-8

# ### LSE Data Analytics Online Career Accelerator
# 
# # DA201: Data Analytics using Python

# ## Loops in Python (tutorial video)

# *Use this Jupyter Notebook to follow along with the tutorial video. You can pause the video to make notes as comments or text blocks.*
# 
# Through control flow structures we can first introduce the conditions in the program and then, based on the condition, the corresponding statement is either executed or skipped. Python uses `if`, `elif`, `else`, `for`, and `while` keywords to control the structure flow in your program. Remember keywords are reserved words in Python that tell the program what action to take. Almost like verbs in the English language.
# 
# In this tutorial video, we will explore the `for`, and `while` loops. Loops are used to iterate over a sequence, for example, lists, dictionaries, tuples, and sets.

# ## 1. The `while` loop statement

# In[1]:


# JUST FOR ILLUSTRATIVE PURPOSES.
# IF YOU RUN THIS CODE YOU WILL GET AN ERROR.

# The while loop.
while condition:
    executable code
    executable code
    
executable code


# In[2]:


# Create a variable.
counter = 0

# Press enter to create an open line.
# Use the while keyword.
# State the condition as counter<5.
# Insert a colon.
# Press enter.
while counter < 5:
    # Python automatically inserts the correct indentation (4 spaces).
    # Indicate that the condition counter should be printed and press Enter.
    print(counter)
    # Insert what the condition should equal.
    # For example, in each loop, the value of the counter will be increased with 1.
    counter = counter + 1
    # Execude the code.


# In[3]:


# Create a variable.
counter = 0

# Press Enter to create an open line.
# Use the while keyword.
# State the condition as counter<5.
# Insert a colon.
# Press Enter.
while counter < 5:
    # Python automatically inserts the correct indentation (4 spaces).
    # Indicate that the condition counter should be printed and press Enter.
    print(counter)
    # Insert what the condition should equal.
    # For example, in each loop, the value of the counter will be increased with 1.
    counter = counter + 1
    
# Insert a print statement outside the loop.
print("This will print once")
# Execude the code.


# ## 2. The `for` loop

# In[ ]:


# JUST FOR ILLUSTRATIVE PURPOSES.
# IF YOU RUN THIS CODE YOU WILL GET AN ERROR.

# The for loop.
for condition:
    executable code
    executable code
    
executable code


# In[4]:


# Use the for keyword.
# State the condition as counter<5.
# Insert a colon.
# Press Enter.
for i in range(5):
    # Python automatically inserts the correct indentation (4 spaces).
    # Indicate that the condition should be printed and press Enter.
    print("hello world")


# In[5]:


# Use the for keyword.
# State the condition as counter<5.
# Insert a colon.
# Press Enter.
for i in range(5):
    # Python automatically inserts the correct indentation (4 spaces).
    # Indicate that the condition should be printed and press Enter.
    print("hello world :", i)


# In[6]:


# Insert a list.
# Use the for keyword.
# State the condition as counter<5.
# Insert a colon.
# Press Enter.
for i in [10, 100, 1000]:
    # Python automatically inserts the correct indentation (4 spaces).
    # Indicate that the condition should be printed and press Enter.
    print("hello world :", i)


# ### Summary:
# - while loop = logical condition
# - for loop = replace a simple list command

# In[ ]:




