import sys
import re
from itertools import count


pattern = re.compile(r'-?\d+')

robots = [list(map(int,pattern.findall(line))) for line in sys.stdin]
m,n = 103,101

for second in count(1):


    positions = set()
    overlap = False

    for r in range(len(robots)):
       
    
        x,y,dx, dy = robots[r]

        x  = (x+dx)%n
        y = (y+dy)%m

        robots[r][:2] = [x,y]

        if (x,y) in positions:
            overlap = True
        
        positions.add((x,y))


    if not overlap:
        print(second)
        sys.exit(0)
    

       

        

        

