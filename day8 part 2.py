#!/usr/bin/env python
# coding: utf-8

# In[1]:


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


# In[7]:


def find_mapping(val):
    from itertools import permutations
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


# In[8]:


def convert_number(S,reverse_mapping):
    
    Sp=S.split()
    
    result=[]
    for S in Sp:

        mapped=''.join(sorted([reverse_mapping[_] for _ in S]))
        locs=['abcefg','cf','acdeg','acdfg','bcdf','abdfg','abdefg','acf','abcdefg','abcdfg']
    
        result.append(locs.index(mapped))
        
    return sum([r*10**p for r,p in zip(result,range(len(result)-1,-1,-1))])
    


# In[9]:


line="acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab | cdfeb fcadb cdfeb cdbaf"
input_val=line.split("|")[0].strip()
output_val=line.split("|")[1].strip()


# In[11]:


mapping,reverse_mapping=find_mapping(input_val)
convert_number(output_val,reverse_mapping)


# In[17]:


with open('data/day8.txt') as fid:
    text=fid.read()


# In[13]:


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


# In[14]:


vals=[]
for line in text.split('\n'):
    input_val=line.split("|")[0].strip()
    output_val=line.split("|")[1].strip()    
    mapping,reverse_mapping=find_mapping(input_val)
    vals.append(convert_number(output_val,reverse_mapping))
    
    


# In[15]:


vals


# In[16]:


sum(vals)


# In[18]:


with open('data/day8.txt') as fid:
    text=fid.read()


# In[20]:


from tqdm import tqdm


# In[23]:


vals=[]
for line in tqdm(text.strip().split('\n')):
    input_val=line.split("|")[0].strip()
    output_val=line.split("|")[1].strip()    
    mapping,reverse_mapping=find_mapping(input_val)
    vals.append(convert_number(output_val,reverse_mapping))
    
print(sum(vals))


# In[22]:


line


# In[ ]:




