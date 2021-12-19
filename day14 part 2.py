#!/usr/bin/env python
# coding: utf-8

# In[16]:


text="""
NNCB

CH -> B
HH -> N
CB -> H
NH -> C
HB -> C
HC -> B
HN -> C
NN -> C
BH -> H
NC -> B
NB -> B
BN -> B
BB -> N
BC -> B
CC -> N
CN -> C
"""
parts=text.split("\n\n")
start=parts[0].strip()
insertion_rules={}
for m in parts[1].strip().split("\n"):
    if not m:


# In[17]:


def pairs(S):
    for c1,c2 in zip(S[:-1],S[1:]):
        yield c1+c2


# In[130]:


def get_pair_counts(start):
    pair_counts={}
    for p in pairs(start):
        if not p in pair_counts:
            pair_counts[p]=1
        else:
            pair_counts[p]+=1
            
    charset=set(start)
    char_counts={c:start.count(c) for c in charset}
    

    return pair_counts,char_counts    


# In[131]:


pair_counts,char_counts=get_pair_counts(start)
pair_counts,char_counts


# In[132]:


def step_pair(pair_counts,char_counts):
    new_pair_counts={}
    new_char_counts=char_counts.copy()
    
    for pair in pair_counts:
        insert_char=insertion_rules[pair]
        
        if insert_char in char_counts:
            new_char_counts[insert_char]+=pair_counts[pair]
        else:
            new_char_counts[insert_char]=pair_counts[pair]
            
        for p in [pair[0]+insert_char,insert_char+pair[1]]:
            if not p in new_pair_counts:
                new_pair_counts[p]=pair_counts[pair]
            else:
                new_pair_counts[p]+=pair_counts[pair]
        
        
    return new_pair_counts,new_char_counts

def step(start):
    new_str=""
    for p in pairs(start):
        insert_char=insertion_rules[p]
        new_str=new_str+p[0]+insert_char

    new_str=new_str+p[1]
    return new_str


# In[133]:



new_pc,new_c=pair_counts,char_counts
new_pc,new_c,start


# In[134]:


step(start)


# In[135]:


step_pair(new_pc,new_c)


# In[136]:


strings=[]
strings.append(start)
new_str=start
for i in range(2):
    new_str=step(new_str)
    strings.append(new_str)


# In[137]:


strings[-1]


# In[138]:


charset=set(strings[-1])
counts=[strings[-1].count(c) for c in charset]
counts,charset


# In[139]:


max(counts)-min(counts)


# In[140]:


new_pc,new_c=pair_counts,char_counts
print(new_pc,new_c)
for i in range(2):
    new_pc,new_c=step_pair(new_pc,new_c)
print(new_pc,new_c)
    


# In[141]:


get_pair_counts(strings[-1])


# In[142]:


with open('data/day14.txt') as fid:
    text=fid.read()
parts=text.split("\n\n")
parts  


# In[143]:


start=parts[0].strip()
insertion_rules={}
for m in parts[1].strip().split("\n"):
    if not m:
        continue
    key=m.split("->")[0].strip()
    char=m.split("->")[1].strip()    
    insertion_rules[key]=char


# In[144]:


strings=[]
strings.append(start)
new_str=start
for i in range(10):
    new_str=step(new_str)
    strings.append(new_str)


# In[145]:


charset=set(strings[-1])
counts=[strings[-1].count(c) for c in charset]


# In[146]:


max(counts)-min(counts)


# In[147]:


pair_counts,char_counts=get_pair_counts(start)
pair_counts,char_counts


# In[148]:


new_pc,new_c=pair_counts,char_counts
for i in range(10):
    new_pc,new_c=step_pair(new_pc,new_c)  
    
counts=[new_c[k] for k in new_c]
max(counts)-min(counts)


# In[149]:


new_pc,new_c=pair_counts,char_counts
for i in range(40):
    new_pc,new_c=step_pair(new_pc,new_c)  
    
counts=[new_c[k] for k in new_c]
max(counts)-min(counts)


# In[ ]:




