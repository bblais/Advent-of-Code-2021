#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().run_line_magic('pylab', 'inline')


# In[11]:


text=open('data/day7.txt').read()
a=array([int(_) for _ in text.split(',')])
print(text)
a


# In[12]:


a=array([16,1,2,0,4,2,7,1,2,14])
a


# In[13]:


a=array([16,1,2,0,4,2,7,1,2,14])
fuel=[]
for x in range(20):
    fuel.append(abs(x-a).sum())
    
plot(fuel,'-o')
fuel,argmin(fuel)


# In[16]:


a=array([int(_) for _ in text.split(',')])
fuel=[]
for x in range(2000):
    fuel.append(abs(x-a).sum())
    
plot(fuel,'-o')
argmin(fuel),min(fuel)


#     1 step in horizontal position costs 1 more unit of fuel than the last: the first step costs 1, the second step costs 2, the third step costs 3, and so on.

# In[19]:


N=10
(1+N)*N//2


# In[22]:


sum(range(1,10+1))


# In[ ]:


a=array([16,1,2,0,4,2,7,1,2,14])
x=5
N=abs(x-a)
F=(1+N)*N//2


# In[23]:


a=array([16,1,2,0,4,2,7,1,2,14])
fuel=[]
for x in range(20):
    N=abs(x-a)
    F=(1+N)*N//2
    
    
    fuel.append(F.sum())
    
plot(fuel,'-o')
fuel,argmin(fuel)


# In[24]:


a=array([int(_) for _ in text.split(',')])
fuel=[]
for x in range(2000):
    N=abs(x-a)
    F=(1+N)*N//2
    
    
    fuel.append(F.sum())
    
plot(fuel,'-o')
argmin(fuel),min(fuel)


# In[ ]:




