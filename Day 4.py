#!/usr/bin/env python
# coding: utf-8

# https://adventofcode.com/2021/day/4

# In[80]:


from Game import Board


# In[95]:


text=open('data/day4.txt').read()
#text=open('data/day4_example.txt').read()


# In[96]:


parts=text.split("\n\n")


# In[97]:


nums=[int(_) for _ in parts[0].split(",")]
print(nums)


# In[98]:


boards=[]
for line in parts[1:]:
    vals=[int(_) for _ in line.split()]
    b=Board(5,5)
    b.board=vals
    boards.append(b)


# In[99]:


boards[0]


# In[100]:


b


# In[101]:


def win(b):
    for col in b.cols():
        if all([_>=100 for _ in col]):
            return True
    for row in b.rows():
        if all([_>=100 for _ in row]):
            return True
    return False


# ## First to win

# In[102]:


boards=[]
for line in parts[1:]:
    vals=[int(_) for _ in line.split()]
    b=Board(5,5)
    b.board=vals
    boards.append(b)
    
for i,num in enumerate(nums):
    for b in boards:
        idx=b.find(num)
        if idx:
            assert len(idx)==1
            b[idx[0]]+=100
            
    for b in boards:
        if win(b):
            break 
            
    if win(b):
        break 
            
print(i,num)
print(b)


# In[103]:


s=0
for i in range(25):
    if b[i]<100:
        s+=b[i]
        
s*num


# In[104]:


win(b)


# ## Last to win

# In[105]:


boards=[]
for line in parts[1:]:
    vals=[int(_) for _ in line.split()]
    b=Board(5,5)
    b.board=vals
    boards.append(b)
    
won=[False]*len(boards)
for i,num in enumerate(nums):
    for b in boards:
        idx=b.find(num)
        if idx:
            assert len(idx)==1
            assert b[idx[0]]<100
            b[idx[0]]+=100
            
    for bi,b in enumerate(boards):
        if win(b):
            won[bi]=True
            if all(won):
                break
            
    if all(won):
        break 
            
print(i,num)
print(b)

s=0
for i in range(25):
    if b[i]<100:
        s+=b[i]
        
s*num


# In[106]:


b,idx


# In[92]:


won


# In[93]:


all(won)


# In[ ]:




