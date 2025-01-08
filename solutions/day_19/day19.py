
from functools import cache
with open('input.txt','r') as file:
    puzzle_input = file.read()

tools,words = puzzle_input.split('\n\n')
tools = [t.strip() for t in tools.split(',')]
words = [w.strip() for w in words.split('\n')]
maxim = len(max(tools,key=len))

def ispossible(i,target,patterns):

    if i == len(target):
        return True
    
    for j in range(i+1,i+maxim+1):
        if j<=len(target):
            if target[i:j] in patterns:
                if ispossible(j,target,patterns):
                    return True
    return False

#part2

@cache
def make(i,target,patterns):
    

    if i == len(target):
        return 1

    res = 0
    for j in range(i+1,i+maxim+1):
        if j<=len(target):
            if target[i:j] in patterns:
                res+= make(j,target,patterns)
            
    return res
res = 0
for word in words:
    patterns= tuple(tool for tool in tools if tool in word)
    res+=make(0,word,patterns)
print(res)

