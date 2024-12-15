import sys
from collections import defaultdict

grid = [list(line.rstrip('\n')) for line in sys.stdin]
regions = defaultdict(set)


in_board = lambda x,y : 0<=x<len(grid) and 0<=y<len(grid[0])

def get_corners(i,j):

   
    
    NW, W, SW, N, S, NE, E, SE = [
        in_board(i+x,j+y) and grid[i+x][j+y] == grid[i][j] 
        for x in range(-1,2)
        for y in range(-1,2)
        if x or y
    ]
   
        

    return sum(
        [
            N and W and not NW, 
            N and E and not NE,
            S and W and not SW,
            S and E and not SE,
            not (N or E),
            not (N or W),
            not (S or E),
            not (S or W)
        ]
    )




def get_region(i,j,count):
    

    regions[count].add((i,j))
    visited.add((i,j))

    neighbors = [(i+1,j), (i-1,j), (i,j+1), (i,j-1)]

    for neighbor in neighbors:
        x,y = neighbor

       
        if in_board(x,y) and grid[x][y] == grid[i][j]  and (x,y) not in regions[count]:
            get_region(x,y,count)
            

    return len(regions[count])*sum([get_corners(*point) for point in regions[count]])




count = 0
res =0 
visited = set()
for i in range(len(grid)):
    for j in range(len(grid[0])):

        if (i,j) not in visited:
            res+= get_region(i,j,count)
            count+=1

print(res)


        
    


        


