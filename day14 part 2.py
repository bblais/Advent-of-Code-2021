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
        continue
    key=m.split("->")[0].strip()
    char=m.split("->")[1].strip()    
    insertion_rules[key]=char


# In[17]:


def pairs(S):
    for c1,c2 in zip(S[:-1],S[1:]):
        yield c1+c2


# In[98]:


def get_pair_counts(start):
    pair_counts={}
    for p in pairs(start):
        if not p in pair_counts:
            pair_counts[p]=1
        else:
            pair_counts[p]+=1

    return pair_counts    


# In[100]:


pair_counts=get_pair_counts(start)
pair_counts


# In[101]:


def step_pair(pair_counts):
    new_pair_counts={}

    for pair in pair_counts:
        insert_char=insertion_rules[pair]
        
        for p in [pair[0]+insert_char,insert_char+pair[1]]:
#             print(p)
            if not p in new_pair_counts:
                new_pair_counts[p]=pair_counts[pair]
            else:
                new_pair_counts[p]+=pair_counts[pair]
#             print("\t",new_pair_counts)
        
        
    return new_pair_counts

def step(start):
    new_str=""
    for p in pairs(start):
        insert_char=insertion_rules[p]
        new_str=new_str+p[0]+insert_char

    new_str=new_str+p[1]
    return new_str


# In[102]:



new_pc=pair_counts
new_pc,start


# In[103]:


step(start)


# In[104]:


step_pair(new_pc)


# In[105]:


strings=[]
strings.append(start)
new_str=start
for i in range(2):
    new_str=step(new_str)
    strings.append(new_str)


# In[106]:


strings[-1]


# In[107]:


charset=set(strings[-1])
counts=[strings[-1].count(c) for c in charset]
counts,charset


# In[108]:


max(counts)-min(counts)


# In[109]:


new_pc=pair_counts
print(new_pc)
for i in range(2):
    new_pc=step_pair(new_pc)
print(new_pc)
    


# In[110]:


get_pair_counts(strings[-1])


# In[120]:


fake_str=""
keys=list(new_pc.keys())

c='N'
e='B'
for key in keys:
    if key.endswith(e) and not key.startswith(c):
        break
end_key=key

while keys:
    if keys==[end_key]:
        key=end_key
    else:
        for key in keys:
            if key.startswith(c) and key!=end_key:
                break
            
    keys.remove(key)
    fake_str+=key*new_pc[key]
    c=key[1]
    


# In[121]:


start


# In[122]:


fake_str


# In[123]:


get_pair_counts(fake_str)


# In[112]:


charset=set(fake_str)
counts=[fake_str.count(c) for c in charset]
counts,charset


# In[82]:


pair_counts={}
for p in pairs(fake_str):
    if not p in pair_counts:
        pair_counts[p]=1
    else:
        pair_counts[p]+=1
        
pair_counts


# In[ ]:




