#!/usr/bin/env python
# coding: utf-8

# In[13]:


def rand100(N=None):
    
    if N is None:        
        while True:
            for i in range(1,100+1):
                yield i
    else:
        count=0
        i=1
        while count<N:
            yield i
            count+=1
            i+=1
            if i>100:
                i=1


# In[16]:


for r in rand100(993):
    print(r,end=" ")
print()
    


# In[17]:


r100=rand100()


# In[21]:


next(r100)


# In[31]:


R=rand100()

player=1
other_player=2
scores=[0,0]
locs=[4,8]
die_count=0
while True:
    move=next(R)+next(R)+next(R)
    die_count+=3
    
    locs[player-1]+=move
    locs[player-1]=(locs[player-1]-1)%10 + 1

    
    scores[player-1]+=locs[player-1]
    
#     print(player,move,locs[player-1],scores[player-1])

    if scores[player-1]>=1000:
        print("Player ",player, "wins")
        break

    player,other_player=other_player,player
    
    
    
print(scores)
print(die_count*scores[other_player-1])


# In[29]:


die_count


# In[32]:


R=rand100()

player=1
other_player=2
scores=[0,0]
locs=[7,4]
die_count=0
while True:
    move=next(R)+next(R)+next(R)
    die_count+=3
    
    locs[player-1]+=move
    locs[player-1]=(locs[player-1]-1)%10 + 1

    
    scores[player-1]+=locs[player-1]
    
#     print(player,move,locs[player-1],scores[player-1])

    if scores[player-1]>=1000:
        print("Player ",player, "wins")
        break

    player,other_player=other_player,player
    
    
    
print(scores)
print(die_count*scores[other_player-1])


# In[ ]:




