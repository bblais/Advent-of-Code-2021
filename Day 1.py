#!/usr/bin/env python
# coding: utf-8

# In[3]:


get_ipython().run_line_magic('pylab', 'inline')
import pandas as pd


# In[5]:


data=loadtxt('data/day1.txt')
data


# In[8]:


sum(diff(data)>0)


# In[9]:


get_ipython().run_line_magic('pinfo', 'convolve')


# In[12]:


new_data=convolve(data,[1,1,1],'valid')


# In[13]:


sum(diff(new_data)>0)


# In[ ]:




