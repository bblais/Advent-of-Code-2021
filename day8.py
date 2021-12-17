#!/usr/bin/env python
# coding: utf-8

# In[20]:


text="""be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb |fdgacbe cefdb cefbgd gcbe
edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec |fcgedb cgb dgebacf gc
fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef |cg cg fdcagb cbg
fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega |efabcd cedba gadfec cb
aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga |gecf egdcabf bgf bfgea
fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf |gebdcfa ecba ca fadegcb
dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf |cefg dcbef fcge gbcadfe
bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd |ed bcgafe cdgba cbgef
egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg |gbdfcae bgc cg cgb
gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc |fgae cfgab fg bagce"""


#       0:      1:      2:      3:      4:
#      aaaa    ....    aaaa    aaaa    ....
#     b    c  .    c  .    c  .    c  b    c
#     b    c  .    c  .    c  .    c  b    c
#      ....    ....    dddd    dddd    dddd
#     e    f  .    f  e    .  .    f  .    f
#     e    f  .    f  e    .  .    f  .    f
#      gggg    ....    gggg    gggg    ....
# 
#       5:      6:      7:      8:      9:
#      aaaa    aaaa    aaaa    aaaa    aaaa
#     b    .  b    .  .    c  b    c  b    c
#     b    .  b    .  .    c  b    c  b    c
#      dddd    dddd    ....    dddd    dddd
#     .    f  e    f  .    f  e    f  .    f
#     .    f  e    f  .    f  e    f  .    f
#      gggg    gggg    ....    gggg    gggg
# 

# In[65]:


z0=set('abcefg')
z1=set('cf')
z2=set('acdeg')
z3=set('acdfg')
z4=set('bcdf')
z5=set('abdfg')
z6=set('abdefg')
z7=set('acf')
z8=set('abcdefg')
z9=set('abcdfg')

zs=[z0,z1,z2,z3,z4,z5,z6,z7,z8,z9]
[len(_) for _ in zs]


# In[ ]:


cf,bcdf,acf


# In[69]:


(z2-z3) , (z2-z5)


# In[73]:


z2&z5,z2&z3,z3&z5


# In[ ]:





# In[14]:


lines=text.split("\n")
output=[_.split('|')[1] for _ in lines]
n=[len(_) for _ in ' '.join(output).split()]

n.count(2)+n.count(4)+n.count(3)+n.count(7)


# In[15]:


with open('data/day8.txt') as fid:
    text=fid.read()


# In[21]:


lines=text.split("\n")
output_vals=[_.split('|')[1] for _ in lines if _]

n=[len(_) for _ in ' '.join(output_vals).split()]

n.count(2)+n.count(4)+n.count(3)+n.count(7)


# In[23]:


input_vals=[_.split('|')[0].strip() for _ in lines if _]
input_vals


# In[24]:


I=input_vals[0]


# In[25]:


I


# In[26]:


parts=I.split()


# In[27]:


parts


# In[28]:


connections={'a':None,'b':None,'c':None,'d':None,'e':None,'f':None,'g':None}


# In[45]:


n1=[len(_) for _ in parts].index(2)  # find the one
cf=set(parts[n1])


# In[46]:


n4=[len(_) for _ in parts].index(4)  # find the four
bcdf=set(parts[n4])


# In[47]:


cf,bcdf


# In[48]:


bd=bcdf-(cf&bcdf)


# In[50]:


n7=[len(_) for _ in parts].index(3)  # find the seven
acf=set(parts[n7])


# In[51]:


acf


# In[60]:


a=acf-cf
a


# In[61]:


connections['a']=list(a)[0]
connections


# In[62]:


n8=[len(_) for _ in parts].index(7)  # find the seven
abcdefg=set(parts[n8])


# In[ ]:




