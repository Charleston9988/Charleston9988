#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
AppleStore = pd.read_csv("C:/Users/EMEKA/Downloads/AppleStore.csv")
googleplaystore = pd.read_csv("C:/Users/EMEKA/Downloads/googleplaystore.csv")
AppleStore.info()
googleplaystore.info()


# In[2]:


googleplaystore.describe(include = "all")


# In[3]:


pd.DataFrame(googleplaystore)
googleplaystore.columns
#Used for displaying columns in horizontal way
for col in googleplaystore:
    print (col)
#displays columns in a vertical manner


# In[4]:


googleplaystore.iloc[10472]
googleplaystore.drop(10472)
#Do not repeat this line of code again. Else another row will be deleted


# In[15]:


googleplaystore.iloc[5]


# In[22]:


for hit in googleplaystore:
    name = hit[0]
    if name == "Coloring book moana":
        print (hit)
        
      


# In[1]:


input_1 = int(input())
input_2 = int(input())
print (input_1 + input_2)

