import heapq
from collections import defaultdict
import sys

#real = j, imag = i

grid = open('input.txt','r').read().split('\n')

dir_map = {">":1,"^":-1j,"<":-1,"v":1j}

G = {c+1j*r:v for r,l in enumerate(grid) for c,v in enumerate(l.strip())}

s = next(k for k,v in G.items() if v=="S")
e = next((k for k,v in G.items() if v == 'E'))

in_board = lambda p: 0<=p.real<len(grid[0]) and 0<=p.imag<len(grid)

def get_neighbors(p):
    directions = [-1 + 0j, 1 + 0j, 0 - 1j, 0 + 1j]
    return [p+d for d in directions if in_board(p+d) and G[p+d]!='#']  # a graph where every edge is 1

graph = {v:get_neighbors(v) for v in G}

def is_turn(p1:complex,p2:complex,face:str)->bool:

    target_vector = p2-p1

    return target_vector == dir_map[face]*1j or target_vector == dir_map[face]*(-1j)


all_min_paths = set()
min_cost= float('inf')
curr_path = set()


def backtrack(point,goal,face,cost):
    global min_cost

    if (point,face) in curr_path:
        return
    
    if cost > min_cost:
        return
    
    curr_path.add((point,face))
    if point == goal:
        if cost < min_cost:
            min_cost = cost
            all_min_paths.clear()
        
        if cost == min_cost:
            all_min_paths.update({pos for (pos,_) in curr_path})

        curr_path.remove((point,face))
        return
    neighbors = get_neighbors(point)

    for p in neighbors:
        new_face  = next((key for key,value in dir_map.items() if value==p-point),face)
        new_cost = cost + 1 + (1000 if new_face != face else 0)

        backtrack(p,goal,new_face,new_cost)

    curr_path.remove((point,face))
backtrack(s,e,'>',0)
print(min_cost)
print(len(all_min_paths))
           

     
        

        
 



