#!/usr/bin/env python
# coding: utf-8

# In[2]:


text="""
[({(<(())[]>[[{[]{<()<>>
[(()[<>])]({[<{<<[]>>(
{([(<{}[<>[]}>{[]{[(<()>
(((({<>}<{<{<>}{[]{[]{}
[[<[([]))<([[{}[[()]]]
[{[{({}]{}}([{[{{{}}([]
{<[[]]>}<{[{[{[]{()[[[]
[<(<(<(<{}))><([]([]()
<{([([[(<>()){}]>(<<{{
<{([{{}}[<[[[<>{}]]]>[]]
""".strip()
lines=text.strip().split('\n')


# In[3]:


lines


# In[4]:


line=lines[0]


# In[5]:


line


# In[8]:


scores={")":3,"]":57,"}":1197,">":25137}


# In[10]:


score=0
for line in lines:

    next_c=[]
    error=False
    for i,c in enumerate(line):
        if c=='[':
            next_c.append(']')
        elif c=='(':
            next_c.append(')')
        elif c=='{':
            next_c.append('}')
        elif c=='<':
            next_c.append('>')
        else:
            nc=next_c.pop()
            if nc!=c:
                error=True
                break

    if error:
        score+=scores[c]
        print(f"Error {c} at {i} for '{line}' {scores[c]} score {score}")


# In[12]:


with open('data/day10.txt') as fid:
    text=fid.read()
lines=text.strip().split('\n')    


# In[13]:


score=0
for line in lines:

    next_c=[]
    error=False
    for i,c in enumerate(line):
        if c=='[':
            next_c.append(']')
        elif c=='(':
            next_c.append(')')
        elif c=='{':
            next_c.append('}')
        elif c=='<':
            next_c.append('>')
        else:
            nc=next_c.pop()
            if nc!=c:
                error=True
                break

    if error:
        score+=scores[c]
        print(f"Error {c} at {i} for '{line}' {scores[c]} score {score}")


# ## Part 2

# In[15]:


scores2={")":1,"]":2,"}":3,">":4}


# In[18]:


from numpy import median


# In[19]:


score_lines=[]
for line in lines:
    score=0
    next_c=[]
    error=False
    for i,c in enumerate(line):
        if c=='[':
            next_c.append(']')
        elif c=='(':
            next_c.append(')')
        elif c=='{':
            next_c.append('}')
        elif c=='<':
            next_c.append('>')
        else:
            nc=next_c.pop()
            if nc!=c:
                error=True
                break

    if error:
        continue
    else:
        while next_c:
            c=next_c.pop()
            score*=5
            score+=scores2[c]
    
    score_lines.append(score)
print(median(score_lines))


# In[ ]:




