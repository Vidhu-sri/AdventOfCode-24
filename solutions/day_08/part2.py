import sys
from collections import defaultdict
import math


antennas = defaultdict(list)


grid = [list(line.rstrip('\n')) for line in sys.stdin]

for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] != '.':
            antennas[grid[i][j]].append((i,j))

lines = []  # y = mx+c
antinodes = set()

for antenna in antennas:
    points = antennas[antenna]

    for i in range(len(points)):
        r1,c1 = points[i]
        for j in range(i+1, len(points)):
            r2, c2 = points[j]

            if c1 != c2:

                m = (r2-r1) #slope
                c = (r1*(c2-c1) - c1*(r2-r1))
                
                lines.append((m,c,(r1,c1),(r2,c2)))
            else:
                lines.append((float('inf'),-1,(r1,c1), (r2,c2)))


def on_line(i,j,line):

    #i,j = y,x
    m,c,p1,p2 = line

    if m != float('inf'):
        return math.isclose(m*j+c,i*(p2[1]-p1[1]),rel_tol=1e-15)
    else:
        return j == p1[1]
    
antinodes  = set()
#print(antennas)

for i in range(len(grid)):
    for j in range(len(grid[0])):
        for line in lines:
            if on_line(i,j,line):
                antinodes.add((i,j))
                
                grid[i][j] = '#'
#print([''.join(l) for l in grid])
print(len(antinodes))


            



