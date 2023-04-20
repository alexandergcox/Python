#!/usr/bin/env python
# coding: utf-8

# ### LSE Data Analytics Online Career Accelerator
# 
# # DA201: Data Analytics using Python

# ## The IF statement in Python (tutorial video)

# *Use this Jupyter Notebook to follow along with the tutorial video. You can pause the video to make notes as comments or text blocks.*
# 
# Through control flow structures we can first introduce the conditions in the program and then, based on the condition, the corresponding statement is either executed or skipped. Python uses `if`, `elif`, `else`, `for`, and `while` keywords to control the flow of structure in your program. Remember keywords are reserved words in Python used to define syntax and structure. Almost like verbs in the English language.
# 
# In this tutorial video, we will explore the `if`, `elif`, and `else` keywords.

# ## 1. The `if` statement

# In[1]:


# Create two variables.
a=10
b=5

# Use the if keyword.
# State the condition as a>b.
# Insert a colon to indicate the end of the if statement.
# Press enter.
if a>b:
    # Python automatically inserts the correct indentation (4 spaces).
    print("a is greater than b")
    # Execude the code.


# In[3]:


# Create two variables.
a=10
b=5

# Use the if keyword.
# State the condition as a<b.
# Insert a colon to indicate the end of the if statement.
# Press enter.
if a<b:
    # Python automatically inserts the correct indentation (4 spaces).
    print("a is greater than b")
    # Execude the code.


# ### Python did not return an output as the `if` statement was not true.

# # 

# ## 2. The `elif` statement

# In[4]:


# Create two variables.
a=10
b=5

# Use the if keyword.
# State the condition as a>b.
# Insert a colon to indicate the end of the if statement.
# Press enter.
if a>b:
    # Python automatically inserts the correct indentation (4 spaces).
    print("a is greater than b")
    
# Use the elif keyword.
# State the conditions as a<b.
# Insert a colon to indicate the end of the if statement.
# Press enter.
elif a<b:
    # Python automatically inserts the correct indentation (4 spaces).
    print("a is less than b")
    # Execude the code.


# #### The `if` statement is still true and ignored the `elif` statement.

# In[5]:


# Create two variables.
a=10
b=50

# Use the if keyword.
# State the condition as a>b.
# Insert a colon to indicate the end of the if statement.
# Press enter.
if a>b:
    # Python automatically inserts the correct indentation (4 spaces).
    print("a is greater than b")
    
# Use the elif keyword.
# State the conditions as a<b.
# Insert a colon to indicate the end of the if statement.
# Press enter.
elif a<b:
    # Python automatically inserts the correct indentation (4 spaces).
    print("a is less than b")
    # Execude the code.


# #### The `if` statement is false and Python returned the `elif` statement.

# # 

# ## 3. The `else` statement

# In[6]:


# Create two variables.
a=50
b=50

# Use the if keyword.
# State the condition as a>b.
# Insert a colon to indicate the end of the if statement.
# Press enter.
if a>b:
    # Python automatically inserts the correct indentation (4 spaces).
    print("a is greater than b")
    
# Use the elif keyword.
# State the conditions as a<b.
# Insert a colon to indicate the end of the if statement.
# Press enter.
elif a<b:
    # Python automatically inserts the correct indentation (4 spaces).
    print("a is less than b")
    
# Use the else keyword.
# Insert a colon to indicate the end of the if statement.
# Press enter.
else:
    # Python automatically inserts the correct indentation (4 spaces).
    print("a is equal to b")
    # Execude the code.


# ### The `if` and `elif` statements were false and Python returned the `else` statement.

# # 

# # Summary:
# Python ignores a statement if the condition is false, but will return the first condition that is true.

# In[ ]:




