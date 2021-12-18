#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().run_line_magic('pylab', 'inline')


# In[56]:


text="""5483143223
2745854711
5264556173
6141336146
6357385478
4167524645
2176841721
6882881134
4846848554
5283751526
""".strip()

def text2arr(text):
    lines=text.strip().split('\n')
    arr_str=[[int(_) for _ in line] for line in lines]
    arr=array(arr_str)
    return arr

arr=text2arr(text)
arr


# In[19]:


from numba import njit


# In[44]:


# @njit
def step(arr):
    arr=arr.copy()
    r,c=arr.shape
    
    for i in range(r):
        for j in range(c):
            arr[i,j]+=1
            
    flash=True
    while flash:
        flash=False
        for i in range(r):
            for j in range(c):
                if arr[i,j]>9:
                    arr[i,j]=0  # flash!
                    flash=True

                    for i2 in [i-1,i,i+1]:
                        for j2 in [j-1,j,j+1]:
                            if i2<0 or j2<0 or i2>=r or j2>=c or (i2==i and j2==j):
                                continue
                            if arr[i2,j2]>0:
                                arr[i2,j2]+=1

    return arr


# In[45]:


arr


# In[46]:


arr1=step(arr)
arr1


# In[47]:


arr2=step(arr1)
arr2


# In[50]:


check_text="""
Before any steps:
5483143223
2745854711
5264556173
6141336146
6357385478
4167524645
2176841721
6882881134
4846848554
5283751526

After step 1:
6594254334
3856965822
6375667284
7252447257
7468496589
5278635756
3287952832
7993992245
5957959665
6394862637

After step 2:
8807476555
5089087054
8597889608
8485769600
8700908800
6600088989
6800005943
0000007456
9000000876
8700006848

After step 3:
0050900866
8500800575
9900000039
9700000041
9935080063
7712300000
7911250009
2211130000
0421125000
0021119000

After step 4:
2263031977
0923031697
0032221150
0041111163
0076191174
0053411122
0042361120
5532241122
1532247211
1132230211

After step 5:
4484144000
2044144000
2253333493
1152333274
1187303285
1164633233
1153472231
6643352233
2643358322
2243341322

After step 6:
5595255111
3155255222
3364444605
2263444496
2298414396
2275744344
2264583342
7754463344
3754469433
3354452433

After step 7:
6707366222
4377366333
4475555827
3496655709
3500625609
3509955566
3486694453
8865585555
4865580644
4465574644

After step 8:
7818477333
5488477444
5697666949
4608766830
4734946730
4740097688
6900007564
0000009666
8000004755
6800007755

After step 9:
9060000644
7800000976
6900000080
5840000082
5858000093
6962400000
8021250009
2221130009
9111128097
7911119976

After step 10:
0481112976
0031112009
0041112504
0081111406
0099111306
0093511233
0442361130
5532252350
0532250600
0032240000
"""


# In[52]:


arrs=[]
for text2 in check_text.split("\n\n"):
    arrs.append(text2arr(text2.split(":")[1]))


# In[53]:


arrs


# In[54]:


arr


# In[66]:


arr1=arr
flash_count=0
for i in range(10):
    if all(arr1==arrs[i]):
        print(f"{i} ok")
    else:
        print(f"{i} bad")
        break
        
    arr1=step(arr1)
    flash_count+=(arr1==0).sum()
    
flash_count


# In[67]:


arr1=arr
flash_count=0
for i in range(100):
    arr1=step(arr1)
    flash_count+=(arr1==0).sum()
    
flash_count


# In[68]:


with open('data/day11.txt') as fid:
    text=fid.read()
arr=text2arr(text)
arr


# In[69]:


arr1=arr
flash_count=0
for i in range(100):
    arr1=step(arr1)
    flash_count+=(arr1==0).sum()
    
flash_count


# ## part 2

# In[73]:


text="""5483143223
2745854711
5264556173
6141336146
6357385478
4167524645
2176841721
6882881134
4846848554
5283751526
""".strip()


# In[74]:


arr=text2arr(text)
arr


# In[75]:


arr1=arr
for i in range(200):
    arr1=step(arr1)
    if all(arr1==0):
        break
    
print(i)


# In[77]:


arr1=arr
i=0
while not all(arr1==0):
    arr1=step(arr1)
    i+=1
    
print(i)


# In[78]:


with open('data/day11.txt') as fid:
    text=fid.read()
arr=text2arr(text)
arr


# In[79]:


arr1=arr
i=0
while not all(arr1==0):
    arr1=step(arr1)
    i+=1
    
print(i)


# In[ ]:




