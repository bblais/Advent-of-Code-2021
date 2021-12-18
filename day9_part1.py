#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().run_line_magic('pylab', 'inline')


# In[2]:


ex1="""
2199943210
3987894921
9856789892
8767896789
9899965678
""".strip()


# In[3]:


text=ex1


# In[4]:


lines=text.strip().split('\n')
arr_str=[[int(_) for _ in line] for line in lines]
arr=array(arr_str)
arr


# In[5]:


from numba import jit


# In[6]:


@jit(nopython=True)
def mins(arr):
    r,c=arr.shape
    
    vals=[]
    for i in range(r):
        for j in range(c):
            found=True
            val=arr[i,j]
            
            if i>0:
                if val>=arr[i-1,j]:
                    continue
            if i<r-1:
                if val>=arr[i+1,j]:
                    continue
            if j>0:
                if val>=arr[i,j-1]:
                    continue
            if j<c-1:
                if val>=arr[i,j+1]:
                    continue
                
            vals.append(val)
            
    return array(vals)
            


# In[7]:


mins(arr)


# In[8]:


sum(mins(arr)+1)


# In[9]:


with open('data/day9.txt') as fid:
    text=fid.read()


# In[10]:


lines=text.strip().split('\n')
arr_str=[[int(_) for _ in line] for line in lines]
arr=array(arr_str)
arr


# In[11]:


mins(arr)


# In[12]:


sum(mins(arr)+1)


# In[ ]:




