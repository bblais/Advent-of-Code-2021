#!/usr/bin/env python
# coding: utf-8

# In[3]:


get_ipython().run_line_magic('pylab', 'inline')


# In[4]:


ex1="""
2199943210
3987894921
9856789892
8767896789
9899965678
""".strip()


# In[5]:


text=ex1


# In[9]:


lines=text.strip().split('\n')
arr_str=[[int(_) for _ in line] for line in lines]
arr=array(arr_str)
arr


# In[10]:


from numba import jit


# In[14]:


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
            


# In[15]:


mins(arr)


# In[16]:


sum(mins(arr)+1)


# In[ ]:




