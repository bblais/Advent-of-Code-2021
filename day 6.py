#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().run_line_magic('pylab', 'inline')


#     Initial state: 3,4,3,1,2
#     After  1 day:  2,3,2,0,1
#     After  2 days: 1,2,1,6,0,8
#     After  3 days: 0,1,0,5,6,7,8
#     After  4 days: 6,0,6,4,5,6,7,8,8
#     After  5 days: 5,6,5,3,4,5,6,7,7,8
#     After  6 days: 4,5,4,2,3,4,5,6,6,7
#     After  7 days: 3,4,3,1,2,3,4,5,5,6
#     After  8 days: 2,3,2,0,1,2,3,4,4,5
#     After  9 days: 1,2,1,6,0,1,2,3,3,4,8
#     After 10 days: 0,1,0,5,6,0,1,2,2,3,7,8
#     After 11 days: 6,0,6,4,5,6,0,1,1,2,6,7,8,8,8
#     After 12 days: 5,6,5,3,4,5,6,0,0,1,5,6,7,7,7,8,8
#     After 13 days: 4,5,4,2,3,4,5,6,6,0,4,5,6,6,6,7,7,8,8
#     After 14 days: 3,4,3,1,2,3,4,5,5,6,3,4,5,5,5,6,6,7,7,8
#     After 15 days: 2,3,2,0,1,2,3,4,4,5,2,3,4,4,4,5,5,6,6,7
#     After 16 days: 1,2,1,6,0,1,2,3,3,4,1,2,3,3,3,4,4,5,5,6,8
#     After 17 days: 0,1,0,5,6,0,1,2,2,3,0,1,2,2,2,3,3,4,4,5,7,8
#     After 18 days: 6,0,6,4,5,6,0,1,1,2,6,0,1,1,1,2,2,3,3,4,6,7,8,8,8,8

# In[4]:


a=array([3,4,3,1,2])
a


# In[5]:


a-=1
a


# In[6]:


a-=1


# In[7]:


a


# In[9]:


a[a==-1]=6


# In[10]:


a


# In[11]:


a=r_[a,8]


# In[12]:


a


# In[13]:


def step(a):
    a=a.copy()
    a-=1
    N=len(a[a==-1])
    if N:
        a[a==-1]=6
        a=r_[a,[8]*N]
    return a


# In[15]:


a=array([3,4,3,1,2])
print(a)
for i in range(18):
    a=step(a)
    print(a)


# In[20]:


a=array([3,4,3,1,2])
for i in range(80):
    a=step(a)
print(len(a))


# In[48]:


a=array([3,4,3,1,2])
N=[len(a)]
for i in range(100):
    a=step(a)
    N.append(len(a))
print(len(a))
N=array(N)
plot(N)


# In[49]:


plot(log(N))
polyfit(arange(len(N)),log(N),1)


# In[52]:


exp(0.08727819*150+1.70403646)


# In[50]:


a=array([3,4,3,1,2])
N=[len(a)]
for i in range(150):
    a=step(a)
    N.append(len(a))
print(len(a))
N=array(N)
plot(N)


# In[51]:


plot(log(N))
polyfit(arange(len(N)),log(N),1)


# In[45]:


N1=N[:-50:50]
N2=N[50::50]
N2/N1


# In[16]:


text=open('data/day6.txt').read()


# In[19]:


a=array([int(_) for _ in text.split(',')])
print(text)
a


# In[22]:


a=array([int(_) for _ in text.split(',')])
for i in range(80):
    a=step(a)
print(len(a))


# In[30]:


a=array([int(_) for _ in text.split(',')])
N=[len(a)]
for i in range(130):
    a=step(a)
    N.append(len(a))
print(len(a))
plot(N)


# In[29]:


a[10]


# ## a different representation -- because this one blows up

# In[56]:


a=[3,4,3,1,2]
N=[0]*9
for i in range(8+1):
    N[i]=a.count(i)
    
a,N


# In[57]:


N0=N[0]
N1=N[1:]+[0]
N0,N1


# In[58]:


N1[6]+=N0
N1[8]+=N0


# In[65]:


def a2N(a):
    a=list(a)
    N=[0]*9
    for i in range(8+1):
        N[i]=a.count(i)    
    return N


# In[66]:


def stepN(N):
    N0=N[0]
    N1=N[1:]+[0]    
    N1[6]+=N0
    N1[8]+=N0    
    return N1


# In[69]:


a=array([3,4,3,1,2])
N=a2N(a)
print(a,N)
for i in range(18):
    a=step(a)
    N=stepN(N)
    print(a,a2N(a),N)


# In[70]:


sum(N)


# In[73]:


a=array([3,4,3,1,2])
N=a2N(a)
for i in range(80):
    a=step(a)
    N=stepN(N)
print(len(a),sum(a2N(a)),sum(N))


# ## on to the solution

# In[74]:


text=open('data/day6.txt').read()


# In[75]:


a=array([int(_) for _ in text.split(',')])
N=a2N(a)
for i in range(80):
    a=step(a)
    N=stepN(N)
    
print(len(a),sum(a2N(a)),sum(N))


# In[77]:


#a=array([int(_) for _ in text.split(',')])
a=array([3,4,3,1,2])
N=a2N(a)
for i in range(256):
    N=stepN(N)
    
print(sum(N))


# In[78]:


a=array([int(_) for _ in text.split(',')])
#a=array([3,4,3,1,2])
N=a2N(a)
for i in range(256):
    N=stepN(N)
    
print(sum(N))


# In[ ]:




