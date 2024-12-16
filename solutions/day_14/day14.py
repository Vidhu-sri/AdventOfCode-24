import sys
import re
from collections import defaultdict


m,n = 101,103

quadrant = defaultdict(int)
x_div,y_div = m//2,n//2
def pos(x,y,dx,dy):
    

    x = (x+100*dx)%m
    y = (y+100*dy)%n

    return (x,y)

def get_quadrant(x,y):

    if x == x_div or y == y_div:
        return None
    return (x < x_div) * 2  + (y < y_div)

def main():
    pattern = re.compile(r'(-?\d+)')
    for line in sys.stdin:
        
        matches = pattern.findall(line)    
        x,y,dx,dy = map(int,matches)
        final_pos = pos(x,y,dx,dy)
        quad = get_quadrant(*final_pos)
        if quad != None:
            quadrant[quad]+=1
    res = 1
    
   
    for points in quadrant:
        
        
        res*=quadrant[points]
    

    print(res)

main()







#224438715
