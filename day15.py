#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().run_line_magic('pylab', 'inline')


# In[55]:


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


# In[56]:


arr=tuple([tuple(row) for row in arr])
arr


# https://www.geeksforgeeks.org/min-cost-path-dp-6/
# 
# 1) Optimal Substructure 
# The path to reach (m, n) must be through one of the 3 cells: (m-1, n-1) or (m-1, n) or (m, n-1). So minimum cost to reach (m, n) can be written as “minimum of the 3 cells plus cost[m][n]”.
# minCost(m, n) = min (minCost(m-1, n-1), minCost(m-1, n), minCost(m, n-1)) + cost[m][n]

# In[57]:


# A Naive recursive implementation of MCP(Minimum Cost Path) problem
R = 3
C = 3
import sys

# Returns cost of minimum cost path from (0,0) to (m, n) in mat[R][C]
def minCost(cost, m, n):
	if (n < 0 or m < 0):
		return sys.maxsize
	elif (m == 0 and n == 0):
		return cost[m][n]
	else:
		return cost[m][n] + min3( minCost(cost, m-1, n-1),
								minCost(cost, m-1, n),
								minCost(cost, m, n-1) )

#A utility function that returns minimum of 3 integers */
def min3(x, y, z):
	if (x < y):
		return x if (x < z) else z
	else:
		return y if (y < z) else z


# Driver program to test above functions
cost= [ [1, 2, 3],
		[4, 8, 2],
		[1, 5, 3] ]
print(minCost(cost, 2, 2))

# This code is contributed by
# Smitha Dinesh Semwal


# In[58]:


from functools import lru_cache
visited=[]

@lru_cache(maxsize=None)
def min_cost(arr,x,y):
    R,C=len(arr),len(arr[0])
    maxval=10**500
    if x<0 or y<0:
        return maxval
    if x>=C or y>=R:
        return maxval
    
    
    elif x==0 and y==0:  # starting point
        return arr[y][x]
    else:
        
        mc1=min_cost(arr,x-1,y)
        mc2=min_cost(arr,x+1,y)
        mc3=min_cost(arr,x,y-1)
        mc4=min_cost(arr,x,y+1)
        
        val=min(mc1,mc2,mc3,mc4)

        return arr[y][x]+ val
    


# In[59]:


R,C=len(arr),len(arr[0])
R,C


# In[60]:


min_cost(arr,C-1,R-1)-arr[0][0]


# In[45]:


with open('data/day15.txt') as fid:
    text=fid.read()


# In[49]:


lines=text.strip().split('\n')
arr_str=[[int(_) for _ in line] for line in lines]
arr=array(arr_str)
arr


# In[50]:


arr=tuple([tuple(row) for row in arr])


# In[51]:


R,C=len(arr),len(arr[0])
R,C


# In[52]:


min_cost(arr,C-1,R-1)-arr[0][0]


# In[53]:


arr[0][0]


# In[ ]:




