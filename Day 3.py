#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().run_line_magic('pylab', 'inline')
import pandas as pd
from Memory import Storage


# https://adventofcode.com/2021/day/3#part2

# In[2]:


with open('data/day3.txt') as fid:
    lines=fid.readlines()


# In[3]:


lines[:10]


# In[5]:


bins=[]
for line in lines:
    bits=[int(_) for _ in line.strip()]
    bins.append(bits)
    
bins=array(bins)
bins


# In[8]:


gamma_binary=median(bins,axis=0)
gamma_binary


# In[10]:


p=arange(len(gamma_binary)-1,-1,-1)
p


# In[11]:


gamma=(gamma_binary*2**p).sum()
gamma


# In[13]:


epsilon=((1-gamma_binary)*2**p).sum()
epsilon


# In[14]:


gamma*epsilon


# In[15]:


median([0,1])


# In[16]:


bins


# In[17]:


c=0


# In[22]:


m=median(bins[:,0])
if m>0:
    m=1
else:
    m=0


# In[23]:


bins2=bins[bins[:,0]==m]


# In[24]:


bins2


# In[33]:


lines="""
00100
11110
10110
10111
10101
01111
00111
11100
10000
11001
00010
01010
""".strip().split('\n')


# In[61]:


with open('data/day3.txt') as fid:
    lines=fid.readlines()


# In[62]:


bins=[]
for line in lines:
    bits=[int(_) for _ in line.strip()]
    bins.append(bits)
    
bins=array(bins)
bins


# In[ ]:





# In[63]:


c=0
print(bins.shape[0])
while bins.shape[0]>1:
    m=median(bins[:,c])
    if m>0:
        m=1
    else:
        m=0   
        
    bins=bins[bins[:,c]==m]
    print(bins.shape[0])
    c+=1
    
bins


# In[64]:


O2=(bins*2**p).sum()
O2


# In[65]:


lines="""
00100
11110
10110
10111
10101
01111
00111
11100
10000
11001
00010
01010
""".strip().split('\n')


# In[66]:


with open('data/day3.txt') as fid:
    lines=fid.readlines()


# In[67]:


bins=[]
for line in lines:
    bits=[int(_) for _ in line.strip()]
    bins.append(bits)
    
bins=array(bins)
bins


# In[68]:


c=0
print(bins.shape[0])
while bins.shape[0]>1:
    m=median(bins[:,c])
    m=1-m # least popular
    if m<1:
        m=0
    else:
        m=1   
        
    
    #print(c,m,median(bins[:,c]),bins[:,c])
    bins=bins[bins[:,c]==m]
    #print(bins)
    print(bins.shape[0])
    c+=1
    
bins


# In[69]:


CO2=(bins*2**p).sum()
CO2


# In[70]:


O2*CO2


# In[ ]:




