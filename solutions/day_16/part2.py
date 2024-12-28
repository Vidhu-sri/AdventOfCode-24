import heapq
from collections import defaultdict

grid = open('input.txt','r').read().split('\n')

dir_map = {">":1,"^":-1j,"<":-1,"v":1j}

G = {c+1j*r:v for r,l in enumerate(grid) for c,v in enumerate(l.strip())}

s = next(k for k,v in G.items() if v == "S")
e = next(k for k,v in G.items() if v == "E")

in_board = lambda p: 0 <= p.real < len(grid[0]) and 0 <= p.imag < len(grid)

def get_neighbors(p):
    directions = [-1+0j, 1+0j, 0-1j, 0+1j]
    return [(1, p+d) for d in directions if in_board(p+d) and G[p+d] != '#']

graph = {v: get_neighbors(v) for v in G}

def is_turn(p1: complex, p2: complex, face: str) -> bool:
    target_vector = p2 - p1
    return target_vector == dir_map[face] * 1j or target_vector == dir_map[face] * (-1j)


def a_star(graph, start, goal):
    
    TURN_PENALTY = 1000
    dist = defaultdict(lambda: float('inf'))
    prev = defaultdict(set)
    dist[(start, '>')] = 0
    frontier = []
    start_priority = dist[(start, '>')] 
    heapq.heappush(frontier, (start_priority, (start.real, start.imag, '>')))
    
    closed = set()
    found_cost = None  # min cost to reach goal
    best_states_at_goal = []
    
    while frontier:
        _, (re, im, face) = heapq.heappop(frontier)
        current = complex(re, im)
        state = (current, face)
        
        if state in closed:
            continue
        closed.add(state)
        
        if current == goal:
            cost_here = dist[state]
            if found_cost is None:
                found_cost = cost_here
                best_states_at_goal = [state]
            elif cost_here == found_cost:
                best_states_at_goal.append(state)
            continue

        for edge_weight, node in graph[current]:
            alt_dist = dist[state] + edge_weight
            
            new_face = next((d for d,v in dir_map.items() if v == node - current), face)
            if new_face != face:
                alt_dist += TURN_PENALTY
            
            
            if alt_dist < dist[(node, new_face)]:
                dist[(node, new_face)] = alt_dist
                prev[(node, new_face)] = {state}
                heapq.heappush(frontier, (alt_dist, (node.real, node.imag, new_face)))
            
          
            elif alt_dist == dist[(node, new_face)]:
              
                prev[(node, new_face)].add(state)
               
    

    
    

    all_pts = set()
    
    stack = []
    for gs in best_states_at_goal:
        stack.append((gs, [gs[0]]))
    
    while stack:
        cur_state, path_so_far = stack.pop()
        
        all_pts.update(path_so_far)
        if cur_state not in prev or len(prev[cur_state]) == 0:
            continue
        for p in prev[cur_state]:
            stack.append((p, path_so_far + [p[0]]))
    
   
    

    grid_data = [list(line) for line in grid]
    
    for p in all_pts:
        r = int(p.imag)
        c = int(p.real)
        if grid_data[r][c] not in ('S','E'):
            grid_data[r][c] = 'O'
    

    grid_data = [''.join(row) for row in grid_data]
    for line in grid_data:
        print(line)
    
    print(f"\nCost of minimal paths: {found_cost}")
    print(f"Number of distinct points in at least one minimal path: {len(all_pts)}")


a_star(graph, start=s, goal=e)
