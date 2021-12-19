#!/usr/bin/env python
# coding: utf-8

# In[1]:


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


# In[2]:


parts=text.split("\n\n")
parts


# In[6]:


start=parts[0].strip()
insertion_rules={}
for m in parts[1].strip().split("\n"):
    if not m:
        continue
    key=m.split("->")[0].strip()
    char=m.split("->")[1].strip()    
    insertion_rules[key]=char


# In[7]:


insertion_rules


# In[8]:


def pairs(S):
    for c1,c2 in zip(S[:-1],S[1:]):
        yield c1+c2


# In[9]:


for p in pairs("NNCB"):
    print(p)


# In[12]:


def step(start):
    new_str=""
    for p in pairs(start):
        insert_char=insertion_rules[p]
        new_str=new_str+p[0]+insert_char

    new_str=new_str+p[1]
    return new_str


# In[14]:


new_str=step(start)
new_str


# In[15]:


step(new_str)


# In[16]:


start


# In[22]:


strings=[]
strings.append(start)
new_str=start
for i in range(10):
    new_str=step(new_str)
    strings.append(new_str)


# In[23]:


strings,[len(_) for _ in strings]


# In[26]:


charset=set(strings[-1])
counts=[strings[-1].count(c) for c in charset]
counts


# In[27]:


max(counts)-min(counts)


# ## actual input

# In[29]:


with open('data/day14.txt') as fid:
    text=fid.read()
parts=text.split("\n\n")
parts  


# In[30]:


start=parts[0].strip()
insertion_rules={}
for m in parts[1].strip().split("\n"):
    if not m:
        continue
    key=m.split("->")[0].strip()
    char=m.split("->")[1].strip()    
    insertion_rules[key]=char


# In[31]:


strings=[]
strings.append(start)
new_str=start
for i in range(10):
    new_str=step(new_str)
    strings.append(new_str)


# In[32]:


charset=set(strings[-1])
counts=[strings[-1].count(c) for c in charset]


# In[33]:


max(counts)-min(counts)


# ## part 2 - 40 steps!

# In[42]:


from tqdm import tqdm


# not sure if it is speed or memory, so try speed first

# In[ ]:


def pairs(S):
    for c1,c2 in zip(S[:-1],S[1:]):
        yield c1+c2


# In[44]:


from numba import njit


# In[53]:


@njit
def step2(start):
    new_str=""
    keys=['KO', 'SO', 'BF', 'VN', 'OV', 'VH', 'KV', 'KB', 'NB', 'HS', 'PF', 'HB', 'OC', 'FS', 'VV', 'KF', 'FN', 'KP', 'HO', 'NH', 'OO', 'FB', 'BP', 'CH', 'SN', 'KN', 'CV', 'CC', 'VB', 'PH', 'CO', 'KS', 'BK', 'FH', 'PV', 'CB', 'FO', 'BB', 'OB', 'HH', 'ON', 'FK', 'NF', 'SV', 'CP', 'SS', 'OP', 'NS', 'HK', 'BC', 'NV', 'VS', 'PC', 'CS', 'NP', 'PS', 'VC', 'KK', 'PO', 'HF', 'KC', 'SF', 'BV', 'FF', 'FV', 'BO', 'OS', 'OF', 'CN', 'NO', 'NC', 'VK', 'HN', 'PK', 'SK', 'HV', 'BH', 'OK', 'VO', 'BS', 'PP', 'SC', 'BN', 'FC', 'SB', 'SH', 'NN', 'NK', 'VF', 'CF', 'PB', 'SP', 'KH', 'VP', 'CK', 'HP', 'FP', 'HC', 'PN', 'OH']
    chars=['C', 'S', 'V', 'B', 'K', 'O', 'N', 'F', 'C', 'K', 'B', 'N', 'H', 'F', 'S', 'C', 'F', 'S', 'N', 'K', 'S', 'C', 'F', 'N', 'O', 'B', 'O', 'B', 'C', 'V', 'K', 'K', 'N', 'S', 'H', 'P', 'F', 'K', 'C', 'F', 'O', 'B', 'F', 'F', 'H', 'B', 'H', 'O', 'N', 'P', 'V', 'F', 'V', 'F', 'V', 'F', 'F', 'S', 'P', 'H', 'P', 'N', 'N', 'V', 'V', 'N', 'C', 'H', 'S', 'O', 'B', 'C', 'B', 'N', 'S', 'F', 'B', 'S', 'B', 'H', 'N', 'K', 'P', 'S', 'B', 'H', 'V', 'N', 'H', 'F', 'C', 'P', 'C', 'N', 'H', 'P', 'B', 'O', 'F', 'H']
    for i in range(len(start)-1):
        c1=start[i]
        c2=start[i+1]
        insert_char=chars[keys.index(c1+c2)]
        new_str=new_str+p[0]+insert_char

    new_str=new_str+p[1]
    return new_str


# In[54]:


keys=insertion_rules.keys()
chars=[insertion_rules[k] for k in keys]


# In[55]:


print(chars)


# In[ ]:


new_str=start
for i in tqdm(range(40)):
    new_str=step2(new_str)


# In[ ]:


charset=new_str
counts=[new_str.count(c) for c in charset]


# In[ ]:


max(counts)-min(counts)

