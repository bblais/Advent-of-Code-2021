#!/usr/bin/env python
# coding: utf-8

# Dirac dice
# 
# 
# 
#     As you experiment with the die, you feel a little strange. An informational brochure in the compartment explains that this is a quantum die: when you roll it, the universe splits into multiple copies, one copy for each possible outcome of the die. In this case, rolling the die always splits the universe into three copies: one where the outcome of the roll was 1, one where it was 2, and one where it was 3.
# 
#     The game is played the same as before, although to prevent things from getting too far out of hand, the game now ends when either player's score reaches at least 21.
# 
#     Using the same starting positions as in the example above, player 1 wins in 444356092776315 universes, while player 2 merely wins in 341960390180808 universes.
# 
# 

# state = (loc1, loc2, score1, score2, current_player)

# In[1]:


universe_count={}


# In[ ]:


move=next(R)+next(R)+next(R)
die_count+=3

locs[player-1]+=move
locs[player-1]=(locs[player-1]-1)%10 + 1


# In[2]:


def initial_state():
    return (7,4,0,0,1)


# In[5]:


def possibilities():
    counts={}
    for r1 in range(3):
        for r2 in range(3):
            for r3 in range(3):
                key=r1+r2+r3+3
                if key in counts:
                    counts[key]+=1
                else:
                    counts[key]=1
                
    return counts


# In[8]:


counts=possibilities()
counts


# In[10]:


universe_wins=[0,0]


# In[11]:


def final_state(state):
    loc1,loc2,sc1,sc2,player=state
    if sc1>=21:
        return 1
    
    if sc2>=21:
        return 2
    
    return False


# In[12]:


def next_states(state,count):
    
    val=final_state(state)
    if val:
        universe_wins[val-1]+=count
        return []
    
    
    loc1,loc2,sc1,sc2,player=state
    other_player=3-player
    
    states=[]
    for move in possibilities():
        if player==1:
            new_loc1=((loc1+move)-1)%10+1
            new_sc1=sc1+new_loc1
            new_loc2=loc2
            new_sc2=sc2
        elif player==2:
            new_loc2=((loc2+move)-1)%10+1
            new_loc1=loc1
            new_sc2=sc2+new_loc2
            new_sc1=sc1
            
        states.append((new_loc1,new_loc2,new_sc1,new_sc2,other_player))
            
    return states
    
    
    


# In[ ]:


def solve(state):
    if state in visited_states:
        return []

    visited_states.append(state)

    if final_state(state):
        return [state]

    ns=next_states(state)
    for next in ns:
        solution=solve(next)
        if solution:
            return solution+[state]

    return []

