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

# In[1]:


locs=['abcefg','cf','acdeg','acdfg','bcdf','abdfg','abdefg','acf','abcdefg','abcdfg']


# In[7]:


for L in locs:
    missing=set('abcdefg')-set(L)
    S='abcdefg'
    for m in missing:
        S=S.replace(m,'X')
    print(S)


# In[78]:


val='be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb'
val


# In[ ]:





# work one out by hand to hopefully get an idea
# 
# (2)
# be = cf
# 
# (7) - doesn't tell us anything
# cfbegad=abcdefg
# 
# (4)
# cgeb = bcdf
# 
# (3)
# edb = acf
# 
# d -> a. (whatever was in 3 but not in 2 is a)
# cg = bd (whatever was 4 but not in 2 is bd)
# 
# (6)
# cbdgef    = abcefg
# agebfd    = abdefg     
# fgaecd    = abcdfg
# 
# they all share abfg
# 
# 
# 
# (5)
# fdcge = acdeg
# fecdb = acdfg
# fabcd = abdfg
# 
# what they all share is agd
# fcd=agd
# 
# 

# In[49]:


(set("cbdgef")-(set("cbdgef")&set("agebfd"))) | (set("agebfd")-(set("cbdgef")&set("agebfd")))


# In[44]:


list(zip(locs,[len(x) for x in locs]))


# In[15]:


from itertools import permutations
perm = permutations('abcdefg')


# In[51]:


for i,p in enumerate(perm):
    pass


# In[52]:


print(i)


# In[53]:


p


# In[20]:


mapping={a:b for a,b in zip('abcdefg',p)}


# In[54]:


items=[]
for L in locs:
    items.append(''.join(sorted([mapping[a] for a in L])))
items=set(items)


# In[56]:


items,locs


# In[57]:


val=' '.join(items)


# In[59]:


val


# In[ ]:





# In[105]:


found=False
perm = permutations('abcdefg')
for i,p in enumerate(perm):
    from itertools import permutations
    mapping={a:b for a,b in zip('abcdefg',p)}
    items=[]
    for L in locs:
        items.append(''.join(sorted([mapping[a] for a in L])))
    items=set(items)

    vals=[]
    for L in val.split():
        vals.append(''.join(sorted(L)))
    vals=set(vals)

    if vals==items:
        found=True
        break
        
print(found)
vals,items
    


# In[106]:


def find_mapping(val):
    found=False
    perm = permutations('abcdefg')
    locs=['abcefg','cf','acdeg','acdfg','bcdf','abdfg','abdefg','acf','abcdefg','abcdfg']
    for i,p in enumerate(perm):
        mapping={a:b for a,b in zip('abcdefg',p)}
        items=[]
        for L in locs:
            items.append(''.join(sorted([mapping[a] for a in L])))
        items=set(items)

        vals=[]
        for L in val.split():
            vals.append(''.join(sorted(L)))
        vals=set(vals)

        if vals==items:
            found=True
            break
            
    if not found:
        raise ValueError("Not found!")
        
    reverse_mapping={b:a for (a,b) in mapping.items()}
        
        
    return mapping,reverse_mapping


# In[87]:


line="acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab | cdfeb fcadb cdfeb cdbaf"
input_val=line.split("|")[0].strip()
output_val=line.split("|")[1].strip()


# In[89]:


mapping,reverse_mapping=find_mapping(input_val)
mapping,reverse_mapping


# In[103]:


def convert_number(S,reverse_mapping):
    
    Sp=S.split()
    
    result=[]
    for S in Sp:

        mapped=''.join(sorted([reverse_mapping[_] for _ in S]))
        locs=['abcefg','cf','acdeg','acdfg','bcdf','abdfg','abdefg','acf','abcdefg','abcdfg']
    
        result.append(locs.index(mapped))
        
    return sum([r*10**p for r,p in zip(result,range(len(result)-1,-1,-1))])
    


# In[104]:


convert_number('cdfeb fcadb cdfeb cdbaf',reverse_mapping)


# In[66]:


vals=[]
for L in val.split():
    vals.append(''.join(sorted(L)))
vals=set(vals)
vals


# In[60]:


p


# In[40]:


set('ab')==set('ba')


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




