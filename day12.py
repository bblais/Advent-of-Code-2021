#!/usr/bin/env python
# coding: utf-8

# In[53]:


get_ipython().run_line_magic('pylab', 'inline')


# In[1]:


D={}


# In[58]:


text="""
start-A
start-b
A-c
A-b
b-d
A-end
b-end
"""


# In[59]:


lines=text.strip().split('\n')


# In[60]:


D={}
for line in lines:
    parts=line.split('-')
            
    if not parts[0] in D:
        D[parts[0]]=[]
    D[parts[0]].append(parts[1])
    if parts[0]!='start' and parts[1]!='end':
        if not parts[1] in D:
            D[parts[1]]=[]
        D[parts[1]].append(parts[0])
        
D


# In[41]:



def paths(path_so_far):
    
    next_nodes=D[path_so_far[-1]]
    
    saved_paths=[]
    for node in next_nodes:
        
        if node=="end":
            saved_paths.append(path_so_far+[node])
            continue
        
        if node.lower()==node and node in path_so_far:  # already visited:
            continue
        
        saved_paths.extend(paths(path_so_far+[node]))
        
        
    return saved_paths
                           
                           
        
        
            
    
    


# In[42]:


result=paths(["start"])


# In[43]:


len(result)


# In[44]:


text="""
dc-end
HN-start
start-kj
dc-start
dc-HN
LN-dc
HN-end
kj-sa
kj-HN
kj-dc
"""
lines=text.strip().split('\n')


# In[45]:


D={}
for line in lines:
    parts=line.split('-')
            
    if not parts[0] in D:
        D[parts[0]]=[]
    D[parts[0]].append(parts[1])
    if parts[0]!='start' and parts[1]!='end':
        if not parts[1] in D:
            D[parts[1]]=[]
        D[parts[1]].append(parts[0])
        
D


# In[46]:


result=paths(["start"])
len(result)


# In[47]:


text="""
KF-sr
OO-vy
start-FP
FP-end
vy-mi
vy-KF
vy-na
start-sr
FP-lh
sr-FP
na-FP
end-KF
na-mi
lh-KF
end-lh
na-start
wp-KF
mi-KF
vy-sr
vy-lh
sr-mi
"""


# In[48]:


lines=text.strip().split('\n')
D={}
for line in lines:
    parts=line.split('-')
            
    if not parts[0] in D:
        D[parts[0]]=[]
    D[parts[0]].append(parts[1])
    if parts[0]!='start' and parts[1]!='end':
        if not parts[1] in D:
            D[parts[1]]=[]
        D[parts[1]].append(parts[0])
        
D


# In[49]:


result=paths(["start"])
len(result)


# ## Part 2

# In[76]:


text="""
start-A
start-b
A-c
A-b
b-d
A-end
b-end
"""


# In[77]:


lines=text.strip().split('\n')
D={}
for line in lines:
    parts=line.split('-')
            
    if not parts[0] in D:
        D[parts[0]]=[]
    D[parts[0]].append(parts[1])
    if parts[0]!='start' and parts[1]!='end':
        if not parts[1] in D:
            D[parts[1]]=[]
        D[parts[1]].append(parts[0])
        
D


# In[78]:



def new_paths(path_so_far):
    
    next_nodes=D[path_so_far[-1]]
    
    saved_paths=[]
    for node in next_nodes:
        
        if node=="end":
            saved_paths.append(path_so_far+[node])
            continue
        
        new_path=path_so_far+[node]
        counts={}
        for n in new_path:
            if n.lower()==n:
                counts[n]=new_path.count(n)

        c=array([counts[_] for _ in counts])
        if any(c>2):
            continue
        if (c==2).sum()>1:
            continue
                
        
        saved_paths.extend(new_paths(new_path))
        
        
    return saved_paths
                           
                           
        
        
            
    
    


# In[79]:


result=new_paths(["start"])
len(result)


# In[80]:


result


# In[81]:


text="""
KF-sr
OO-vy
start-FP
FP-end
vy-mi
vy-KF
vy-na
start-sr
FP-lh
sr-FP
na-FP
end-KF
na-mi
lh-KF
end-lh
na-start
wp-KF
mi-KF
vy-sr
vy-lh
sr-mi
"""


# In[82]:


lines=text.strip().split('\n')
D={}
for line in lines:
    parts=line.split('-')
            
    if not parts[0] in D:
        D[parts[0]]=[]
    D[parts[0]].append(parts[1])
    if parts[0]!='start' and parts[1]!='end':
        if not parts[1] in D:
            D[parts[1]]=[]
        D[parts[1]].append(parts[0])
        
D


# In[83]:


result=new_paths(["start"])
len(result)


# In[84]:


result[:10]


# ## check if they are all valid

# In[85]:


D


# In[86]:


from tqdm import tqdm


# In[88]:


for res in tqdm(result):
    for node,next_node in zip(res[:-1],res[1:]):
        if next_node not in D[node]:
            raise ValueError
        


# In[91]:


keys=list(D.keys())
keys


# In[92]:


for key in D:
    for c in D[key]:
        if c not in keys:
            raise ValueError


# In[94]:


lower_keys=[k for k in keys if k.lower()==k]
lower_keys.remove('start')
lower_keys.remove('end')
lower_keys


# In[95]:


for res in tqdm(result):
    assert res.count("start")==1
    assert res.count("end")==1


# In[96]:


res


# ## fix the duplicate start

# In[97]:


lines=text.strip().split('\n')
D={}
for line in lines:
    parts=line.split('-')
            
    if parts[1]=="start":
        parts=parts[1],parts[0]  # swap it
    if not parts[0] in D:
        D[parts[0]]=[]
    D[parts[0]].append(parts[1])
    if parts[0]!='start' and parts[1]!='end':
        if not parts[1] in D:
            D[parts[1]]=[]
        D[parts[1]].append(parts[0])
        
D


# In[98]:


result=new_paths(["start"])
len(result)


# In[ ]:




