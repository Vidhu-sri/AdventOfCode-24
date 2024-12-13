import sys
from collections import defaultdict
import numpy as np


antennas = defaultdict(list)


grid = [list(line.rstrip('\n')) for line in sys.stdin]

for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] != '.':
            antennas[grid[i][j]].append((i,j))


def get_antinodes(p1,p2):
    in_board = lambda x,y: 0<=x<len(grid) and 0<=y<len(grid[0])
    nodes = []
    r1,c1 = p1
    r2,c2 = p2

    node1 = (2*r2-r1, 2*c2-c1)
    node2 = (2*r1-r2, 2*c1-c2)

    if in_board(node1[0],node1[1]):
        nodes.append(node1)
    if in_board(node2[0],node2[1]):
        nodes.append(node2)
    return nodes






antinodes = set()

for antenna in antennas:
    points = antennas[antenna]

    for i in range(len(points)):
       
        for j in range(i+1, len(points)):
            
            nodes = get_antinodes(points[i], points[j])

            for node in nodes:
                antinodes.add(node)

print(len(antinodes))

            


