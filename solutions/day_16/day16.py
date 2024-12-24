
import heapq
from collections import defaultdict

#real = j, imag = i

grid = open('input.txt','r').read().split('\n')

dir_map = {">":1,"^":-1j,"<":-1,"v":1j}

G = {c+1j*r:v for r,l in enumerate(grid) for c,v in enumerate(l.strip())}

s = next(k for k,v in G.items() if v=="S")
e = next((k for k,v in G.items() if v == 'E'))

in_board = lambda p: 0<=p.real<len(grid[0]) and 0<=p.imag<len(grid)

def get_neighbors(p):
    directions = [-1 + 0j, 1 + 0j, 0 - 1j, 0 + 1j]
    return [(1,p+d) for d in directions if in_board(p+d) and G[p+d]!='#']  # a graph where every edge is 1

graph = {v:get_neighbors(v) for v in G}

def is_turn(p1:complex,p2:complex,face:str)->bool:

    target_vector = p2-p1

    return target_vector == dir_map[face]*1j or target_vector == dir_map[face]*(-1j)


def reconstruct_path(start,goal,prev):
    

    for d in dir_map:
        if (goal,d) in prev:
            temp = (goal,d)
            break
    path = []

    while temp in prev:
        path.append(temp[0])
        temp = prev[temp]
    path.append((start,'>'))
    path.reverse()
    return path

def a_star(graph,start, goal):

    
    
    prev = {v:None for v in graph}
    dist = defaultdict(lambda: float('inf'))

    dist[start,'>'] = 0
    frontier = []  #(priority, (real, imag, direction))
    start_priority = dist[start,'>'] 
    heapq.heappush(frontier,(start_priority,(start.real,start.imag,'>')))

    closed = set()
    
    while frontier:

        _,(re,im,face) = heapq.heappop(frontier)
        current = complex(re,im)
        state = (current,face)
        if state in closed:
            continue
        closed.add(state)

        if current == goal:
            total_cost = dist[state]
            break
        for edge_weight,node in graph[current]:
       
            alt_dist = dist[state] + edge_weight

            new_face = next((key for key,value in dir_map.items() if value==node-current))   

            if new_face != face:
                alt_dist+=1000 # heuristic

            if alt_dist < dist[node,new_face]:
           
                dist[node,new_face] = alt_dist

                prev[node,new_face] = state
                
                heapq.heappush(frontier, (alt_dist,(node.real,node.imag,new_face)))
    print(total_cost)

   

a_star(graph,start=s,goal=e)



