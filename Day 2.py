#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().run_line_magic('pylab', 'inline')
import pandas as pd


# In[4]:


from Memory import Storage


# In[2]:


with open('data/day2.txt') as fid:
    lines=fid.readlines()


# In[5]:


S=Storage()
x=0
y=0
S+=x,y
for line in lines:
    command,distance=line.strip().split()
    distance=int(distance)
    
    if command=='forward':
        x+=distance
    elif command=='down':
        y-=distance
    elif command=='up':
        y+=distance
    else:
        raise ValueError("You can't get there from here.")        
        
    S+=x,y        
    
x,y=S.arrays()


# In[6]:


plot(x,y,'-o')


# In[7]:


x[-1]*abs(y[-1])


#     down X increases your aim by X units.
#     up X decreases your aim by X units.
#     forward X does two things:
#     It increases your horizontal position by X units.
#     It increases your depth by your aim multiplied by X.

# In[9]:


S=Storage()
x=0
y=0
a=0
S+=a,x,y
for line in lines:
    command,distance=line.strip().split()
    distance=int(distance)
    
    if command=='forward':
        x+=distance
        y-=a*distance
    elif command=='down':
        a+=distance
    elif command=='up':
        a-=distance
    else:
        raise ValueError("You can't get there from here.")        
        
    S+=a,x,y        
    
a,x,y=S.arrays()


# In[10]:


plot(x,y,'-o')


# In[11]:


x[-1]*abs(y[-1])


# In[ ]:




