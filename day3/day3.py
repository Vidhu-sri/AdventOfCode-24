import sys
import re



def calc(s):
    s = s[s.index('(')+1:s.index(')')].split(',')
   
    return int(s[0])*int(s[1])    

string = ''

for line in sys.stdin:
    string+=line

pattern = re.compile(r'do\(\)|don\'t\(\)|mul\(\d{1,3},\d{1,3}\)')
matches = pattern.finditer(string)

res = 0
matches = [match.group(0) for match in matches]

stack = ['do()']

for match in matches:
    if match == 'do()' or match == 'don\'t()':
        stack.append(match)
    else:
        if stack[-1] == 'do()':
            res+=calc(match)
    

print(res)