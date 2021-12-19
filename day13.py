#!/usr/bin/env python
# coding: utf-8

# In[47]:


get_ipython().run_line_magic('pylab', 'inline')


# In[57]:


text="""
6,10
0,14
9,10
0,3
10,4
4,11
6,0
6,12
4,1
0,13
10,12
3,4
3,0
8,4
1,10
2,14
8,10
9,0

fold along y=7
fold along x=5
"""


# In[58]:


parts=text.split("\n\n")
parts


# In[67]:


arr_xy=array([(int(x),int(y)) for x, y in  [_.split(",") for _ in parts[0].strip().split('\n')]])
arr_xy


# In[69]:


arr_xy.max(axis=0)


# In[74]:





# In[81]:


C,R=arr_xy.max(axis=0)+1
im=zeros((R,C),int)


# In[82]:


for x,y in arr_xy:
    print(x,y)
    im[y,x]=1


# In[83]:


im


# In[84]:


imshow(im)


# In[85]:


def fold(arr,x=None,y=None):
    
    if not y is None:
        assert all(arr[y,:]==0)
        top=arr[:y,:]
        bottom=flipud(arr[y+1:,:])
        
        arr2=top+bottom
        arr2[arr2>1]=1
        
        return arr2
    
    if not x is None:
        assert all(arr[:,x]==0)
        left=arr[:,:x]
        right=fliplr(arr[:,x+1:])
        
        arr2=left+right
        arr2[arr2>1]=1
        
        return arr2
        
    raise ValueError("You can't get there from here")
        
        


# In[86]:


im


# In[87]:


y=7
arr=im
assert all(arr[y,:]==0)
top=arr[:y,:]
bottom=flipud(arr[y+1:,:])

arr2=top+bottom
arr2[arr2>1]=1
        


# In[88]:


arr2


#     like this:
# 
#     #.##..#..#.
#     #...#......
#     ......#...#
#     #...#......
#     .#.#..#.###
#     ...........
#     ...........
# 

# In[89]:


x=5
arr=arr2

assert all(arr[:,x]==0)
left=arr[:,:x]
right=fliplr(arr[:,x+1:])

arr2=left+right
arr2[arr2>1]=1


# In[90]:


arr2


# In[91]:


imshow(arr2)


# In[92]:


parts[1]


# In[93]:


fold_lines=parts[1].strip().split("\n")


# In[94]:


im


# In[97]:


im2=im.copy()
for line in fold_lines:
    fold_str=line.split()[-1]
    direction=fold_str.split("=")[0]
    loc=int(fold_str.split("=")[1])
    
    if direction=="y":
        im2=fold(im2,y=loc)
    elif direction=="x":
        im2=fold(im2,x=loc)
        
    else:
        raise ValueError("You can't get there from here")
imshow(im2)        


# In[98]:


with open('data/day13.txt') as fid:
    text=fid.read()


# In[99]:


parts=text.split("\n\n")
parts


# In[100]:


arr_xy=array([(int(x),int(y)) for x, y in  [_.split(",") for _ in parts[0].strip().split('\n')]])
arr_xy


# In[113]:


C,R=arr_xy.max(axis=0)+1
C,R=1311,895
im=zeros((R,C),int)


# In[114]:


for x,y in arr_xy:
    im[y,x]=1


# In[115]:


figure(figsize=(10,12))
imshow(im)


# In[116]:


fold_lines=parts[1].strip().split("\n")
fold_lines


# ## Part 1 - first fold

# In[117]:


im2=im.copy()
line=fold_lines[0]
fold_str=line.split()[-1]
direction=fold_str.split("=")[0]
loc=int(fold_str.split("=")[1])

if direction=="y":
    im2=fold(im2,y=loc)
elif direction=="x":
    im2=fold(im2,x=loc)

else:
    raise ValueError("You can't get there from here")
imshow(im2)        


# In[121]:


sum(im2)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[122]:


im2=im.copy()
for line in fold_lines:
    fold_str=line.split()[-1]
    direction=fold_str.split("=")[0]
    loc=int(fold_str.split("=")[1])
    
    if direction=="y":
        im2=fold(im2,y=loc)
    elif direction=="x":
        im2=fold(im2,x=loc)
        
    else:
        raise ValueError("You can't get there from here")
imshow(im2)        


# In[ ]:




