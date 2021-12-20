#!/usr/bin/env python
# coding: utf-8

# https://www.geeksforgeeks.org/minimum-cost-path-left-right-bottom-moves-allowed/

# ```c++
# // C++ program to get least cost path in a grid from
# // top-left to bottom-right
# #include <bits/stdc++.h>
# using namespace std;
#  
# #define ROW 5
# #define COL 5
#  
# // structure for information of each cell
# struct cell
# {
#     int x, y;
#     int distance;
#     cell(int x, int y, int distance) :
#         x(x), y(y), distance(distance) {}
# };
#  
# // Utility method for comparing two cells
# bool operator<(const cell& a, const cell& b)
# {
#     if (a.distance == b.distance)
#     {
#         if (a.x != b.x)
#             return (a.x < b.x);
#         else
#             return (a.y < b.y);
#     }
#     return (a.distance < b.distance);
# }
#  
# // Utility method to check whether a point is
# // inside the grid or not
# bool isInsideGrid(int i, int j)
# {
#     return (i >= 0 && i < ROW && j >= 0 && j < COL);
# }
#  
# // Method returns minimum cost to reach bottom
# // right from top left
# int shortest(int grid[ROW][COL], int row, int col)
# {
#     int dis[row][col];
#  
#     // initializing distance array by INT_MAX
#     for (int i = 0; i < row; i++)
#         for (int j = 0; j < col; j++)
#             dis[i][j] = INT_MAX;
#  
#     // direction arrays for simplification of getting
#     // neighbour
#     int dx[] = {-1, 0, 1, 0};
#     int dy[] = {0, 1, 0, -1};
#  
#     set<cell> st;
#  
#     // insert (0, 0) cell with 0 distance
#     st.insert(cell(0, 0, 0));
#  
#     // initialize distance of (0, 0) with its grid value
#     dis[0][0] = grid[0][0];
#  
#     // loop for standard dijkstra's algorithm
#     while (!st.empty())
#     {
#         // get the cell with minimum distance and delete
#         // it from the set
#         cell k = *st.begin();
#         st.erase(st.begin());
#  
#         // looping through all neighbours
#         for (int i = 0; i < 4; i++)
#         {
#             int x = k.x + dx[i];
#             int y = k.y + dy[i];
#  
#             // if not inside boundary, ignore them
#             if (!isInsideGrid(x, y))
#                 continue;
#  
#             // If distance from current cell is smaller, then
#             // update distance of neighbour cell
#             if (dis[x][y] > dis[k.x][k.y] + grid[x][y])
#             {
#                 // If cell is already there in set, then
#                 // remove its previous entry
#                 if (dis[x][y] != INT_MAX)
#                     st.erase(st.find(cell(x, y, dis[x][y])));
#  
#                 // update the distance and insert new updated
#                 // cell in set
#                 dis[x][y] = dis[k.x][k.y] + grid[x][y];
#                 st.insert(cell(x, y, dis[x][y]));
#             }
#         }
#     }
#  
#     // uncomment below code to print distance
#     // of each cell from (0, 0)
#     /*
#     for (int i = 0; i < row; i++, cout << endl)
#         for (int j = 0; j < col; j++)
#             cout << dis[i][j] << " ";
#     */
#     // dis[row - 1][col - 1] will represent final
#     // distance of bottom right cell from top left cell
#     return dis[row - 1][col - 1];
# }
#  
# // Driver code to test above methods
# int main()
# {
#     int grid[ROW][COL] =
#     {
#         31, 100, 65, 12, 18,
#         10, 13, 47, 157, 6,
#         100, 113, 174, 11, 33,
#         88, 124, 41, 20, 140,
#         99, 32, 111, 41, 20
#     };
#  
#     cout << shortest(grid, ROW, COL) << endl;
#     return 0;
# }
# ```

# In[3]:


get_ipython().run_line_magic('pylab', 'inline')


# In[5]:


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


# In[9]:


iinfo(arr.dtype).max


# In[29]:


def shortest(arr,r,c):
    maxval=9223372036854775807
    distances=ones((r,c),int)*maxval
    R,C=arr.shape
    
    S=[]
    S.append(cell(0,0,0))
    distances[0,0]=arr[0,0]

    while S:

        k=S.pop()
        for x,y in [[k.x-1,k.y],[k.x+1,k.y],[k.x,k.y-1],[k.x,k.y+1]]:
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


# In[30]:


R,C=arr.shape
shortest(arr,R,C)


# In[31]:


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


# In[35]:


with open('data/day15.txt') as fid:
    text=fid.read()
lines=text.strip().split('\n')
arr_str=[[int(_) for _ in line] for line in lines]
arr=array(arr_str)
arr    


# In[36]:


R,C=arr.shape
shortest(arr,R,C)-arr[0,0]  # take off the start


# In[ ]:




