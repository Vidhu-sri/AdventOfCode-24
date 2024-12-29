from collections import deque
import sys

start,goal = None,None
grid = []
for idx,line in enumerate(sys.stdin):
    line = list(line.rstrip('\n'))

    if not start or not goal:
        if 'S' in line:
            start = (idx,line.index('S'))
        if 'E' in line:
            goal = (idx,line.index('E'))
    grid.append(line)

in_board = lambda x,y : 0<=x<len(grid) and 0<=y<len(grid[0])    

def get_neighbors(node):
    x,y = node
    neighbors = [(x+1,y),(x-1,y),(x,y+1),(x,y-1)]
    for neighbor in neighbors:
        if (
            in_board(*neighbor) and
            grid[neighbor[0]][neighbor[1]] in '.SE'
        ):
            yield neighbor

def bfs(start):

    Q = deque([[0,start]])
    visited = {}

    while Q:

        distance, node = Q.popleft()
        
        if node in visited:
            continue
        visited[node] = distance
        for neighbor in get_neighbors(node):
            Q.append((distance+1,neighbor))
    return visited

cheats = 0
threshold = 100
visited = bfs(goal)
# for (x, y), t1 in visited.items():
#     for i, j in [(x+2, y), (x-2, y), (x, y-2), (x, y+2)]:
#         if visited.get((i, j), 0) - t1 >= target+2:
#             cheats += 1

path = sorted(visited, key=visited.get)
for t2 in range(threshold, len(path)):
    for t1 in range(t2 - threshold):
        x1, y1 = path[t1]
        x2, y2 = path[t2]
        distance = abs(x1-x2) + abs(y1-y2)
        if distance <= 20 and t2 - t1 - distance >= threshold:
            cheats += 1

        
print(cheats)





