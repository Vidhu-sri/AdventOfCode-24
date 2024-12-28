import heapq
import sys

size = 71
bytes = 1024

graph = {r+1j*c:'.' for c in range(size) for r in range(size)}


def get_neighbors(point):

    neighbors = [1,-1,1j,-1j]
    for dx in neighbors:
        if (
            point+dx in graph and
            graph[point+dx] != '#'
        ):
            yield point+dx

def djikstra(start,goal,graph):
    visited = set()
    prev = {v:None for v in graph}
    dist = {v:float('inf') for v in graph}
    dist[start] = 0
    frontier = [(0,(start.real,start.imag))]

    while frontier:
        

        _,(re,im) = heapq.heappop(frontier)
        current = complex(re,im)

        if current in visited:
            continue
        visited.add(current)

        if current == goal:
            break

        for neighbor in get_neighbors(current):
            alt_distance = dist[current]+1

            if alt_distance < dist[neighbor]:
                dist[neighbor] = alt_distance
                prev[neighbor] = current
                heapq.heappush(frontier,(alt_distance,(neighbor.real,neighbor.imag)))

        

    return dist[goal]



#part2
for idx,line in enumerate(sys.stdin):
    print(idx)
    x,y = map(int,line.split(','))
    graph[complex(x,y)] = '#'
    d = djikstra(0+0j,complex(size-1,size-1), graph)
    if d== float('inf'):
        print(x,y)
        break




    

