import sys
import re


with open('input.txt','r') as file:
    puzzle_input = file.read()


# a1*A + b1*B = k1
# a2*A + b2*B = k2

pattern = re.compile(r'\d+')
offset = 0.0001
res =0 
for machine in puzzle_input.split('\n\n'):
    
    a1,a2,b1,b2,k1,k2 = map(int,pattern.findall(machine))
    k1+= 10**13 #part2
    k2+=10**13  #part2
    A = (b2*k1-b1*k2)/(a1*b2-a2*b1)
    B = (a2*k1-a1*k2)/(a2*b1-a1*b2)

    if abs(A-round(A)) < offset and abs(B-round(B)) < offset:
        res+= 3*A + B
print(int(res))



    