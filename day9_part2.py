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


# In[4]:


text=ex1


# In[5]:


lines=text.strip().split('\n')
arr_str=[[int(_) for _ in line] for line in lines]
arr=array(arr_str)
arr


# In[26]:


def basin_locations(arr,visited=None,i=0,j=0):
    
    if visited is None:
        visited=zeros_like(arr)
        
    visited[i,j]=1
    r,c=arr.shape 
    if arr[i,j]==9:
        return [],visited

    locs=[(i,j)]
    for i2,j2 in ([i-1,j],[i+1,j],[i,j-1],[i,j+1]):
        if i2<0 or i2>=r or j2<0 or j2>=c:
            continue
            
        if visited[i2,j2]:
            continue
        elif arr[i2,j2]==9:
            visited[i2,j2]=1
            continue
        else:
            new_locs,_=basin_locations(arr,visited,i2,j2)
            locs.extend(new_locs)
            
    return locs,visited
        


# In[28]:


visited=None
r,c=arr.shape 
basins=[]
for i in range(r):
    for j in range(c):
        if not visited is None and visited[i,j]:
            continue
        
        locs,visited=basin_locations(arr,visited,i,j)
        if locs:
            basins.append(locs)


# In[34]:


L=[len(_) for _ in basins]
L


# In[41]:


sorted(L,reverse=True)[:3]


# In[42]:


val=prod(sorted(L,reverse=True)[:3])
val


# ## Now on the big one

# In[43]:


with open('data/day9.txt') as fid:
    text=fid.read()


# In[44]:


lines=text.strip().split('\n')
arr_str=[[int(_) for _ in line] for line in lines]
arr=array(arr_str)
arr


# In[45]:


visited=None
r,c=arr.shape 
basins=[]
for i in range(r):
    for j in range(c):
        if not visited is None and visited[i,j]:
            continue
        
        locs,visited=basin_locations(arr,visited,i,j)
        if locs:
            basins.append(locs)


# In[46]:


L=[len(_) for _ in basins]
val=prod(sorted(L,reverse=True)[:3])
val


# In[ ]:




