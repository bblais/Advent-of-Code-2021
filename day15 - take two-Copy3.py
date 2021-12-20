#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().run_line_magic('pylab', 'inline')


# https://pypi.org/project/astar-python/

# In[18]:


class Astar:

    def __init__(self, matrix):
        self.mat = self.prepare_matrix(matrix)

    class Node:
        def __init__(self, x, y, weight=0):
            self.x = x
            self.y = y
            self.weight = weight
            self.heuristic = 0
            self.parent = None

        def __repr__(self):
            return str(self.weight)

    def print(self):
        for y in self.mat:
            print(y)

    def prepare_matrix(self, mat):
        matrix_for_astar = []
        for y, line in enumerate(mat):
            tmp_line = []
            for x, weight in enumerate(line):
                tmp_line.append(self.Node(x, y, weight=weight))
            matrix_for_astar.append(tmp_line)
        return matrix_for_astar

    def equal(self, current, end):
        return current.x == end.x and current.y == end.y

    def heuristic(self, current, other):
        return abs(current.x - other.x) + abs(current.y - other.y)

    def neighbours(self, matrix, current):
        neighbours_list = []
        # commenting diagonals
#         if current.x - 1 >= 0 and current.y - 1 >= 0 and matrix[current.y - 1][current.x - 1].weight is not None:
#             neighbours_list.append(matrix[current.y - 1][current.x - 1])
        if current.x - 1 >= 0 and matrix[current.y][current.x - 1].weight is not None:
            neighbours_list.append(matrix[current.y][current.x - 1])
#         if current.x - 1 >= 0 and current.y + 1 < len(matrix) and matrix[current.y + 1][
#             current.x - 1].weight is not None:
#             neighbours_list.append(matrix[current.y + 1][current.x - 1])
        if current.y - 1 >= 0 and matrix[current.y - 1][current.x].weight is not None:
            neighbours_list.append(matrix[current.y - 1][current.x])
        if current.y + 1 < len(matrix) and matrix[current.y + 1][current.x].weight is not None:
            neighbours_list.append(matrix[current.y + 1][current.x])
#         if current.x + 1 < len(matrix[0]) and current.y - 1 >= 0 and matrix[current.y - 1][
#             current.x + 1].weight is not None:
#             neighbours_list.append(matrix[current.y - 1][current.x + 1])
        if current.x + 1 < len(matrix[0]) and matrix[current.y][current.x + 1].weight is not None:
            neighbours_list.append(matrix[current.y][current.x + 1])
#         if current.x + 1 < len(matrix[0]) and current.y + 1 < len(matrix) and matrix[current.y + 1][
#             current.x + 1].weight is not None:
#             neighbours_list.append(matrix[current.y + 1][current.x + 1])
        return neighbours_list

    def build(self, end):
        node_tmp = end
        path = []
        while (node_tmp):
            path.append([node_tmp.x, node_tmp.y])
            node_tmp = node_tmp.parent
        return list(reversed(path))

    def run(self, point_start, point_end):
        matrix = self.mat
        start = self.Node(point_start[0], point_start[1])
        end = self.Node(point_end[0], point_end[1])
        closed_list = []
        open_list = [start]

        while open_list:
            current_node = open_list.pop()

            for node in open_list:
                if node.heuristic < current_node.heuristic:
                    current_node = node

            if self.equal(current_node, end):
                return self.build(current_node)

            for node in open_list:
                if self.equal(current_node, node):
                    open_list.remove(node)
                    break

            closed_list.append(current_node)

            for neighbour in self.neighbours(matrix, current_node):
                if neighbour in closed_list:
                    continue
                if neighbour.heuristic < current_node.heuristic or neighbour not in open_list:
                    neighbour.heuristic = neighbour.weight + self.heuristic(neighbour, end)
                    neighbour.parent = current_node
                if neighbour not in open_list:
                    open_list.append(neighbour)

        return None


# In[19]:


arr=array([    31, 100, 65, 12, 18,
        10, 13, 47, 157, 6,
        100, 113, 174, 11, 33,
        88, 124, 41, 20, 140,
        99, 32, 111, 41, 20])
arr=arr.reshape(5,5)
arr


# In[20]:


R,C=arr.shape
astar = Astar(arr)
result = astar.run([0, 0], [C-1, R-1])


# In[21]:


[arr[y,x] for x,y in result]


# In[22]:


sum([arr[y,x] for x,y in result])


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


# In[ ]:


R,C=arr.shape
shortest(arr,R,C)-arr[0,0]  # take off the start


# In[ ]:




