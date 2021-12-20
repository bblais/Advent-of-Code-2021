#!/usr/bin/env python
# coding: utf-8

# In[27]:


get_ipython().run_line_magic('pylab', 'inline')


# ### restricting to just down and right

# In[28]:


from dataclasses import dataclass

@dataclass
class cell:
    x:int
    y:int
    distance:float
    
    def __lt__(self, other):
        
        if self.distance==other.distance:
            if self.x!=other.x:
                return self.x<other.x
            else:
                return self.y<other.y
        else:
            return self.distance<other.distance
        
    
arr=array([    31, 100, 65, 12, 18,
        10, 13, 47, 157, 6,
        100, 113, 174, 11, 33,
        88, 124, 41, 20, 140,
        99, 32, 111, 41, 20])
arr=arr.reshape(5,5)
arr


# In[29]:


iinfo(arr.dtype).max


# In[30]:


def shortest(arr,r,c):
    maxval=9223372036854775807
    distances=ones((r,c),int)*maxval
    R,C=arr.shape
    
    S=[]
    S.append(cell(0,0,0))
    distances[0,0]=arr[0,0]

    while S:

        k=S.pop()
#        for x,y in [[k.x-1,k.y],[k.x+1,k.y],[k.x,k.y-1],[k.x,k.y+1]]:
        for x,y in [[k.x+1,k.y],[k.x,k.y-1],[k.x,k.y+1]]:
            if x<0 or y<0 or x>=C or y>=R:
                continue
                
            if distances[y,x]> distances[k.y,k.x]+ arr[y,x]:
                if distances[y,x]!=maxval:
                    findcell=[kk for kk in S if kk.x==x and kk.y==y and kk.distance==distances[y,x]]
                    if findcell:
                        assert len(findcell)==1,(findcell,S,x,y)
                        S.remove(findcell[0])
                    
                distances[y,x]=distances[k.y,k.x]+ arr[y,x]
                S.append(cell(x,y,distances[y,x]))
                
    return distances[r-1,c-1]


# In[31]:


R,C=arr.shape
shortest(arr,R,C)


# In[32]:


text="""
1163751742
1381373672
2136511328
3694931569
7463417111
1319128137
1359912421
3125421639
1293138521
2311944581
""".strip()
lines=text.strip().split('\n')
arr_str=[[int(_) for _ in line] for line in lines]
arr=array(arr_str)
arr


# In[33]:


R,C=arr.shape
shortest(arr,R,C)-arr[0,0]  # take off the start


# In[34]:


with open('data/day15.txt') as fid:
    text=fid.read()
lines=text.strip().split('\n')
arr_str=[[int(_) for _ in line] for line in lines]
arr=array(arr_str)
arr    


# ## only down and right and up

# In[35]:


R,C=arr.shape
shortest(arr,R,C)-arr[0,0]  # take off the start


# In[ ]:




